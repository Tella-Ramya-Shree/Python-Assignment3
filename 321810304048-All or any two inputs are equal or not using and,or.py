#All or any two inputs are equal or not using and,or
first = int(input ("first number"))
second = int(input("second number"))
third=int(input("third number"))
all = (first == second) and (second == third) and (third == first)
print("All are equal:",all)
any = (first == second) or (second == third) or (third == first)
print("Any of two are equal:",any)