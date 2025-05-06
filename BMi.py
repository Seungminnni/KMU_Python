def main():
    print("This program reads data for two people")
    print("and computes their body mass index (BMI).")
    bmi_info()
    print()
    print("Have a nice day!")

def bmi_calc(h, w):
    return w/(h*h)*703

def bmi_lavel(bmi):
    if bmi <18.5:
        return "class 1"
    elif bmi <25.0:
        return "class 2"
    elif bmi <30.0:
        return "class 3"
    else:
        return "class 4"

def bmi_info():
    for i in range(1,3):
        print()
        print("Person " +str(i)+ " information:")
        h = float(input("height (in inches)? "))
        w = float(input("weight (in pounds)? "))
        bmi = bmi_calc(h, w)
        print(f"BMI = {bmi:.1f}")
        print(bmi_lavel(bmi))
        

main()