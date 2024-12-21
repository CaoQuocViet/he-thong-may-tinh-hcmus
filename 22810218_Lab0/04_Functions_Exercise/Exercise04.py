# Need to create a function called show_employee() that:

# Accepts two arguments: the employee’s name and salary.
# Displays both the name and salary.
# Assigns a default value of 9000 to the salary if it is not provided.

def show_employee(name, salary=9000):
    print("Name: ", name)
    print("Salary: ", salary)

show_employee("John", 10000)
show_employee("Jane")