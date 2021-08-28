weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))
height_m = height_cm/100                #Converting height from cm to m.
try:
    a = weight/(height_m*height_m)      #Calculating BMI.
except:
    print("Please enter the weight and height properly.")
    quit()
b = "{:.1f}".format(a)                  #it shows only one decimal places in BMI.
BMI = float(b)

if BMI==0:
    print("Please enter the weight and height properly.")

elif BMI<18.5:
    print("Your Body Mass Index is", BMI, "which means you are underweight.")

elif BMI>=18.5 and BMI<=24.9:
    print("Your Body Mass Index is", BMI, "which means you are healthy.")

elif BMI>=25 and BMI<=29.9:
    print("Your Body Mass Index is", BMI, "which means you are overweight.")

elif BMI>=30:
    print("Your Body Mass Index is", BMI, "which means you are obese.")

