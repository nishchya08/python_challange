# Match_case

def day_of_the_week(day):
    match day:
      case "Saturday" | "Sunday":
        return True
      case "Tuesay" | "Wednesday" | "Thursday" | "Friday" | "Monday":
        return "False"
      case _:
        return False

print(day_of_the_week("Pizza"))