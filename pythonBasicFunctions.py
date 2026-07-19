class multiplefunctions():
    def OddEven():
        num=int(input("Enter the number"))
        if((num%2)==1):
            print("Odd Number")
            message="Odd Number"
        else:
            print("Even Number")
            message="Even Number"
        return message
    
    def AgeCategory():
          age=int(input("Enter the age :"))
          if(age<18):
            print("children")
            cate="children"
          elif(age<35):
            print("Adult")
            cate="Adult"
          elif(age<59):
            print("Citizen")
            cate="Citizen"
          else:
            print("Senior Citizen")
            cate="Senior Citizen"
            return cate
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