#  this calculator will return false answer for specific calculation i.e 2*4 = 15
a = int(input("enter a number:"))
b = int(input("enter the value of b:"))
c = input("choose any operator +, / ,* ,-, %:")
if a == 45 and b == 3 and c == "*":
    print("555")
elif a == 56 and b == 9 and c == "+":
    print("77")
elif a == 56 and b == 6 and c == "/":
    print("4")
elif c == "+":
    print(a+b)
elif c == "*":
    print(a*b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(a/b)
elif c == "%":
    print(a%b)
else:
    print("not available")
