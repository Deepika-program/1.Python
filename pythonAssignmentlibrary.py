class AssignmentFinalFunc():
    def Subfields():
        list1 = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for i in list1:
            print (i)
        return i
    def OddEven():
        num=int(input("Enter the number"))
        if((num%2)==1):
            print(num, "is Odd Number")
            message="Odd Number"
        else:
            print(num,"is Even Number")
            message="Even Number"
        return message
    def CheckEligibility():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))   
        if(gender=="Male"):
            if(age>21):
                print("ELIGIBLE")
                message = "ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                message ="NOT ELIGIBLE"
        elif(gender=="Female"):
            if(age>18):
                print("ELIGIBLE")
                message = "ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
        else:
            message = "Invalid gender input. Please enter 'Male' or 'Female'."
    
        return message
    def Area_triangle():
        height=float(input("Height : "))
        breadth=float(input("Breadth : "))
        Area_formula = (height*breadth)/2
        print("Area of Triangle: ",Area_formula)
    def Perimeter_triangle(h1,h2,b):
        print("Height1:",h1)
        print("Height2:",h2)
        print("Breadth:",b)
        Perimeter_formula=h1+h2+b
        print("Perimeter of Triangle : ",Perimeter_formula)
    def FindResult():
        sub1=int(input("Subject1 : "))
        sub2=int(input("Subject2 : "))
        sub3=int(input("Subject3 : "))
        sub4=int(input("Subject4 : "))
        sub5=int(input("Subject5 : "))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total :",total)
        percentage=(sub1+sub2+sub3+sub4+sub5)/5
        print("percentage :",percentage)