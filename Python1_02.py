h,w = input("Enter your High and Weight : ").split()
w = float(w)
h = float(h)
BMI = w / (h*h)

if BMI < 18.5 :
    print("Less Weight")
elif BMI >= 18.5 and BMI < 23 :
    print("Normal Weight")
elif BMI >= 23 and BMI < 25 :
    print("More than Normal Weight")
elif BMI >= 25 and BMI < 30 :
    print("Getting Fat")
elif BMI >= 30 :
    print("Fat")
