def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight (kg) and height (m).
    
    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.
    
    Returns:
        float: Calculated BMI.
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    Determine BMI category based on calculated BMI.
    
    Args:
        bmi (float): Calculated BMI.
    
    Returns:
        str: BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()

