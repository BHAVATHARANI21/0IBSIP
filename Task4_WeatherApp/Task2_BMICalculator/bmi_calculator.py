print("===== BMI CALCULATOR =====")

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values!")

    else:
        bmi = weight / (height ** 2)

        print("\n----- BMI RESULT -----")
        print(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Error: Please enter valid numbers!")

print("-----------------------")