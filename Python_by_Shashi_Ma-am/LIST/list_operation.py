'''Performing some basic operation on list
    1. List Concatenation
    2. Repeatation
    3. Membership
    4. Alliasing
    5. Closing list     '''

# List Concatenation
My_List = list(map(int,input("Enter the Value of First List: ").split()))
My_New_List = list(map(int,input("Enter the value of Second List: ").split()))
print(f"My List : {My_List}")
print(f"My New List : {My_New_List}")

Final_List = My_List + My_New_List
print(f"Final List: {Final_List}")
