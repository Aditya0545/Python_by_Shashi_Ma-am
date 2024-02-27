# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_elements():
    l = list(map(int,input("Enter the elements of list: ").split()))
    unique_list = []
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    print(f"unique elemwnts of list is : {unique_list}")
    
unique_elements()