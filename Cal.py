def calculate_percentage(number, percent):
    return (number * percent) / 100

number = float(input("Enter a number: "))
percent = float(input("Enter the percentage: "))

result = calculate_percentage(number, percent)
print("{} is {}% of {}".format(result, percent, number))
