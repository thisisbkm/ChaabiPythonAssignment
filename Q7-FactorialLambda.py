factorial = lambda x: 1 if x==0 else x*factorial(x-1)
if __name__=="__main__":
    number = int(input("Enter the Number : "))
    fact = factorial(number)
    print(f"The factorial of number {number} is {fact}")