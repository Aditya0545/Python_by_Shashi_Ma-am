'''There is a scholarship for which a group of students enrolled in college. There is another scholarship for
which another group of students got enrolled. So, now we want to know the name of the students who
enrolled for both the scholarships so that we can restrict them to take only one scholarship.'''

def common_students(scholorship1,scholorship2):
    return set(scholorship1) & set(scholorship2)

scholorship1 = ['Aditya', 'Rohit', 'Komal', 'Pratik', 'John', 'Cassey']
scholorship2 = ['Rohit', 'Malti', 'John', 'Siber', 'Cassey']

common_students_list = common_students(scholorship1,scholorship2)
print(f"Students whon are in both Scholorship list is: {common_students_list}")