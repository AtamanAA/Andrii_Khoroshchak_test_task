def fibonacci(n):
    try:
        number = int(n)
    except ValueError:
        return "Incorrect value"
    if number < 0:
        return "Number must be positive"
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    print(fibonacci(10))
