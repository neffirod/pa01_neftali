# bmi.py
# Neftali Rodriguez, 04/19/17



def bmi(inches, pounds):
    kg=pounds/2.20462262
    m=inches/39.3700787
    bmi=kg/m**2
    return(bmi)


def category(bmi):
    if bmi<18.5:
        return('Underweight')
    if bmi>=18.5 and bmi<25:
        return('Normal')
    if bmi>=25 and bmi<30:
        return('Overweight')
    if bmi>=30:
        return('Obese')







# solution must be above this comment

# do not change any part of the code below
def main():
    height = float( input("enter height in inches: ") )
    weight = float( input("enter weight in pounds: ") )
    bodyMassIndex = bmi(height, weight)
    bmiCat = category(bodyMassIndex)
    allCats = ['Underweight','Normal','Overweight','Obese']
    if bmiCat in allCats:
        print("BMI is {0:.1f}: {1}".format(bodyMassIndex, bmiCat))
    else: print ("Category error:",bmiCat,'\n  must be one of ',allCats)

main()
