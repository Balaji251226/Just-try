num = int(input("Enter Num :"))
if (num % 2 == 0):  #2 vala divide pana vara reminder zero va iruntha even illana odd
    print("Even")  
else:
    print("Odd")

print("Even" if(num % 2 == 0) else "Odd")