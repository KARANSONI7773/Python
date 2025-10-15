while True:
    print("\nEnter a student's marks to find grade:")
    a = int(input("Enter marks (or -1 to stop): "))

    if a == -1:  # stop condition
        print("No marks remaining. Exiting program.")
        break

    if a > 100 or a < 0:
        print("Invalid input. Please enter marks between 0 and 100.")
    elif a > 90:
        print("O")
    elif a > 85:
        print("A+")
    elif a > 80:
        print("A")
    elif a > 70:
        print("B+")
    elif a > 60:
        print("B")
    elif a > 50:
        print("C")
    elif a > 40:
        print("P")
    else:
        print("F")
