class assignment():
    def subfields():
        print("Sub-fields in AI are:")
        s = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for a in s:
            print(a)
    
    def OddEven():
            a = int(input("Enter a number:"))
            if (a=="odd"):
                print("Odd number")
            else:
                print(a,"is Even number")

    def Eligible():
        k = input("Your Gender:")
        l = int(input("Your Age:"))
        if (k == "Male"):
            if (l>=21):
                print("Eligible")
        elif (k == "female"):
            if (l>=18):
                print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        a = int(input("Subject1="))
        b = int(input("Subject2="))
        c = int(input("Subject3="))
        d = int(input("Subject4="))
        e = int(input("Subject5="))
        Total = a+b+c+d+e
        print("Total :",Total)
        Percentage = (Total/500)*100
        print("Percentage :",Percentage)

    def triangle():
        a = int(input("Height:"))
        b = int(input("Breadth:"))
        Areaformula = (a*b)/2
        print ("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", Areaformula)
        c = int(input("Height1:"))
        d = int(input("Height2:"))
        e = int(input("Breadth:"))
        Perimeterformula = c+d+e
        print("Perimeter formula: Height1+Height+Breadth")
        print("Perimeter of Triangle:",Perimeterformula)