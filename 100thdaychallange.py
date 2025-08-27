import sys, io, time, requests, pandas as pd, yfinance as yf
from datetime import datetime, date
import pytz

TZ = pytz.timezone("Asia/Kolkata")

SYMBOL_CSV_URLS = [
    "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
    "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
]

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15")

def fetch_symbol_master(timeout=20) -> pd.DataFrame:
    headers = {
        "User-Agent": UA,
        "Accept": "text/csv,*/*;q=0.9",
        "Referer": "https://www.nseindia.com/",
    }
    last_err = None
    for url in SYMBOL_CSV_URLS:
        try:
            r = requests.get(url, headers=headers, timeout=timeout)
            r.raise_for_status()
            df = pd.read_csv(io.BytesIO(r.content))
            # normalize
            rename_map = {c: c.strip().upper().replace("  ", " ") for c in df.columns}
            df = df.rename(columns=rename_map)
            series_col = "SERIES" if "SERIES" in df.columns else None
            status_col = "STATUS" if "STATUS" in df.columns else None
            if series_col:
                df = df[df[series_col].astype(str).str.strip() == "EQ"]
            if status_col:
                df = df[df[status_col].astype(str).str.upper().str.strip() == "ACTIVE"]
            symbol_col = "SYMBOL" if "SYMBOL" in df.columns else None
            name_col   = "NAME OF COMPANY" if "NAME OF COMPANY" in df.columns else None
            isin_col   = "ISIN NUMBER" if "ISIN NUMBER" in df.columns else None
            keep = [c for c in [symbol_col, name_col, isin_col, series_col] if c]
            df = df[keep].drop_duplicates().reset_index(drop=True)
            for c in keep:
                df[c] = df[c].astype(str).str.strip()
            df = df.sort_values(symbol_col).reset_index(drop=True)
            simple_map = {}
            if symbol_col: simple_map[symbol_col] = "SYMBOL"
            if name_col:   simple_map[name_col]   = "NAME"
            if isin_col:   simple_map[isin_col]   = "ISIN"
            if series_col: simple_map[series_col] = "SERIES"
            return df.rename(columns=simple_map)
        except Exception as e:
            last_err = e
    raise RuntimeError(f"Failed to fetch symbol master. Last error: {last_err}")

# ---------- LIVE NSE (robust) ----------
def nse_session():
    """Warm a session so NSE returns quote JSON reliably."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": UA,
        "Accept": "application/json,text/plain,*/*",
        "Referer": "https://www.nseindia.com/",
    })
    # Warm-up: hit homepage & quote page to get cookies
    try:
        s.get("https://www.nseindia.com/", timeout=10)
        s.get("https://www.nseindia.com/get-quotes/equity?symbol=TCS", timeout=10)
    except requests.RequestException:
        pass
    return s

def get_live_price_nse(symbol: str) -> float | None:
    """
    Live price via NSE JSON API.
    """
    s = nse_session()
    url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
    try:
        r = s.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        # priceInfo.lastPrice is the LTP; pChange/close for % etc if needed
        p = (data.get("priceInfo") or {}).get("lastPrice")
        return float(p) if p is not None else None
    except Exception:
        return None

# ---------- Yahoo fallback (NSE can be fussy sometimes) ----------
def get_latest_price_yahoo(symbol: str) -> float | None:
    """
    Delayed price via Yahoo. Tries 1m bars for today, then 5d/1m.
    """
    ysym = f"{symbol}.NS"
    try:
        # Try today's 1m
        df = yf.download(ysym, interval="1m", period="1d",
                         progress=False, prepost=False, auto_adjust=False)
        if df is not None and not df.empty:
            return df["Close"].iloc[-1].item()
    except Exception:
        pass
    # Second try: 5d window (some symbols only return in wider span)
    try:
        df = yf.download(ysym, interval="1m", period="5d",
                         progress=False, prepost=False, auto_adjust=False)
        if df is None or df.empty:
            return None
        # take last bar from today if available, else last bar overall
        if hasattr(df.index, "tz_localize"):
            idx = df.index.tz_convert("Asia/Kolkata")
        else:
            idx = df.index
        today_mask = pd.Series(idx.date == date.today(), index=df.index)
        df_today = df[today_mask] if today_mask.any() else df
        return df_today["Close"].iloc[-1].item()
    except Exception:
        return None

def get_latest_price(symbol: str):
    p = get_live_price_nse(symbol)
    if p is not None:
        return p, "NSE (live)"
    p = get_latest_price_yahoo(symbol)
    if p is not None:
        return p, "Yahoo (delayed)"
    return None, None

# ---------- Simple chooser ----------
def choose_stock(df: pd.DataFrame) -> str:
    print(f"Loaded {len(df)} NSE symbols (EQ series).")
    while True:
        q = input("\nType part of SYMBOL or NAME (or 'q' to quit): ").strip()
        if q.lower() in {"q", "quit", "exit"}: sys.exit(0)
        if not q: continue
        mask = df["SYMBOL"].str.contains(q, case=False, na=False) | df["NAME"].str.contains(q, case=False, na=False)
        hits = df[mask].head(20)
        if hits.empty:
            print("No matches. Try again."); continue
        print("\nMatches:")
        for i, r in enumerate(hits.itertuples(index=False), 1):
            print(f"{i:2d}. {r.SYMBOL:<12} [{getattr(r,'SERIES','')}]  {r.NAME}")
        sel = input("Pick a number (or 'r' to refine search): ").strip().lower()
        if sel in {"r", "refine"}: continue
        if not sel.isdigit(): print("Enter a number."); continue
        idx = int(sel)
        if not (1 <= idx <= len(hits)): print("Out of range."); continue
        return hits.iloc[idx - 1]["SYMBOL"]

def main():
    df = fetch_symbol_master()
    symbol = choose_stock(df)
    print(f"\nFetching latest price for: {symbol}")
    price, source = get_latest_price(symbol)
    now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S %Z")
    if price is None:
        print(f"[{now}] Could not fetch price for {symbol} from NSE or Yahoo."); sys.exit(2)
    print(f"[{now}] {symbol}: ₹{price:.2f}  (source: {source})")

if __name__ == "__main__":
    main()
