import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="the fibonacci number you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output result to a file", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()

    result = fib(args.num)
    if (args.verbose):
        print("The " + str(args.num) + " the fib number is " + str(result))
    elif (args.quiet):
        print(result)
    else:
        print(f"fib({args.num}) = {str(result)}")


    if (args.output):
        file = open("fibonacci.txt", "a")
        file.write(str(result)+"\n")


if __name__ == "__main__":
    Main()
