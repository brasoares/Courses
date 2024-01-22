#Request input data:
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

#Calculate the BMI:
bmi = weight / (pow(height, 2))

#Provide the output that matches:
if bmi < 18.5:
 print(f"Your BMI of {bmi} indicates that you are underweight. Consider consulting with a healthcare professional for personalized advice.")
elif bmi < 25:
 print(f"Your BMI of {bmi} falls within the normal weight range. Keep up with healthy habits!")
elif bmi < 30:
 print(f"Your BMI of {bmi} suggests a slight overweight. Consider focusing on overall health and well-being.")
elif bmi < 35:
 print(f"Your BMI of {bmi} indicates a classification of obesity. It's advisable to consult with a healthcare professional for personalized guidance.")
else:
 print(f"Your BMI of {bmi} classifies as clinically obese. Seeking the advice of a healthcare professional is recommended to address your specific health needs.")
