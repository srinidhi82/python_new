role = input("Enter the role(admin, tech, hr):")
match role:
    case "admin":
        print("Admin can do everything")

    case "tech":
        print("This role csn code")

    case "hr":
        print("They can offer Job")

    case _:
        print("Unknown role")

print("I am " + "25 years old")