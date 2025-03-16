"""a program that prints the fibonacci sequence"""
# Ask user how many fibonacci numbers they want
# generate sequence:
# F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2


def fibonacci(max_number):
    """function generates fibonacci numbers up to given max"""
    # max: the user defined endpoint

    fibonacci_list = [0, 1]

    for num in range(2, max_number):
        fibonacci_list.append(
            fibonacci_list[num - 1] + fibonacci_list[num - 2])

    for item in fibonacci_list:
        print(item)


def main():
    """the main function"""
    while True:
        try:
            max_number = int(input(
                "How many fibonacci numbers do you want to generate?\n-: "))
            break
        except ValueError:
            print("Invalid input! Please pick a number.")
    fibonacci(max_number)


if __name__ == "__main__":
    main()
