'''Two lists num1 and num2 are given. Now form a new list which contain elements of num1 but not num2.
The element of num1 may be present in num2 so you have to exclude that elements. Use list comprehension
to solve this case study. '''

def exclude_elements(num1, num2):
    return [num for num in num1 if num not in num2]
# Example usage:
num1 = [1, 2, 3, 4, 5]
num2 = [4, 5, 6, 7, 8]
new_list = exclude_elements(num1, num2)
print("New list with elements of num1 but not num2:", new_list)