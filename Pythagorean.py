while True:  # Start a loop
    A = float(input("A is the short side: "))
    B = float(input("B is another short side: "))
    C = (A**2) + (B**2)  # Pythagorean theorem step 1
    C = C ** 0.5  # Take the square root

    Test = input(f"Are these numbers right? {A}, {B} (yes/no): ").lower()

    if Test == "yes":
        print("The Hypo is:", C)
        break  # Exit the loop if input is correct
    else:
        print("Let's try again.")
