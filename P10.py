def weekday(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case _:
            print("Invalid day")
weekday(6)
