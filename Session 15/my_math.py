def square(x):
    return x * x


def main():
    n = int(input())
    print("In my_math: square of {} is {}.".format(n, square(n)))

if __name__ == '__main__':
    main()
