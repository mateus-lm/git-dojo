from division import division
from multiplication import product
from sum import soma
from subtraction import subtraction

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print("The sum of", a, "and", b, "is", soma(a, b))
    print("The difference between", a, "and", b, "is", subtraction(a, b))
    print("The product of", a, "and", b, "is", product(a, b))
    print("The division of", a, "and", b, "is", division(a, b))

if __name__ == "__main__":
    main()