''' def find_no2(nos):
    if len(nos) < 2:
        return None
    largest = nos[0]
    no2 = None
    for num in nos[1:]:
        if num > largest:
            no2 = largest
            largest = num
        elif num != largest and (no2 is None or num > no2):
            no2 = num
    return no2


num_str = input("Enter 5 nos separated by spaces: ")
num_list = num_str.split()

if len(num_list) != 5:
    print("Error! Enter 5 nos")
elif len(num_list)<5:
    print("Error: nos < 5")
else:
    nos = [int(num) for num in num_list]

no2 = find_no2(nos)

print("\nThe second largest no is: ")
print(no2)
'''
def find_second_largest_number():
    numbers = input("Enter a list of nos separated by spaces: ").split()

    try:
        numbers = [int(num) for num in numbers]
        if len(numbers) < 2:
            print("Please enter at least two numbers.")
            return

        largest_number = float('-inf')
        second_largest_number = float('-inf')

        for num in numbers:
            if num > largest_number:
                second_largest_number = largest_number
                largest_number = num
            elif num > second_largest_number and num != largest_number:
                second_largest_number = num

        if second_largest_number == float('-inf'):
            print("There is no second largest number.")
        else:
            print(f"The second largest no is: {second_largest_number}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

find_second_largest_number()
