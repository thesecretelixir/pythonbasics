
S1 = float(input()) 
S2 = float(input()) 
S3 = float(input()) 
S4 = float(input()) 
S5 = float(input()) 
S6 = float(input()) 

Sum = S1 + S2 + S3 + S4 + S5+ S6
CGPA = Sum / 6
Percentage= (Sum/600)*100
print(f"Your percentage is {Percentage}"+ " And  "+ f"Your CGPA is {CGPA}")
if Percentage > 90:
    print ("You have A grade")
elif Percentage > 70:
    print("You have B grade")
elif Percentage > 45:
    print("You have C grade")
elif Percentage > 35:
    print("You have D grade")
elif Percentage < 35:
    print ("You have E grade" )
   
       
