def threeN(x, y, z):
    if x == y == z:
        print("\nResult is ", int(x) * int(y) * int(z))
    elif x == y:
        print("\nResult is ", int(x) * int(y) + int(z))
    elif x == z:
        print("\nResult is ", int(x) * int(z) + int(y))
    elif z == y:
        print("\nResult is ", int(x) + int(y) * int(z))
    else:
        print("\nResult is ", int(x) + int(y) + int(z))


def main():
    while True:
        try:
            print()
            first = int(input("Enter First Number  : "))
            second = int(input("Enter Second Number : "))
            third = int(input("Enter Third Number  : "))
            threeN(first, second, third)
        except ValueError:
            print("Enter a Valid Integer!\n\n")
            continue


main()
