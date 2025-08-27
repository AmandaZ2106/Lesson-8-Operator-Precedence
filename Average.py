a=int(input("Please enter a number:"))
b=int(input("Please enter another value"))
c=int(input("Please enter another value"))
avg=(a+b+c)/3
print("\nThe average of the entered numbers are",avg)
if avg>a and avg>b and avg>c:
    print("The average is greater than",a,b"and",c)
elif avg>a and avg>b:
    print("The average is greater than",a,"and",b,"only")    
elif avg>a and avg>c:
    print("The average is greater than",a,"and",c)   
elif avg>b and avg>c:
    print("The average is greater than",b,"and",c)
elif avg>a:
    print("The average is greater than only",a)
elif avg>b:
    print("The average is greater than only",b)
else:
    print("The average is greater than only",c)
         

