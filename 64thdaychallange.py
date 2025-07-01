# args and Kwards excercise


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Nishchya", "kataria",
               street= "123 Fake st.",
               pobox = "123 Fake pobox.",
               state = "SF",
               zip= "12345")