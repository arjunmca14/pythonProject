def switch_case(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invalid month")

# Test cases
print(switch_case(1))  # Output: January
print(switch_case(6))  # Output: June
print(switch_case(13)) # Output: Invalid month
