"""
# Exercise 2.1 : Create a dictionary like this by taking values from the user:
here the idea is to support a generic dictionary where the values could be of any datatype
and the keys are strings

{
'employee_id' : 1,
'employee_name' : 'Sarwesh'
'account_number' : 829389283982839,
'salary' : 1000.99999,
'address' : {'home_address' : 'Pune' , 'work_address' : 'mumbai'} ,
'awards': ['employeeOfTheYear','StarOfTheMonth']
'subjects_enrolled' : ('Physics','Chemistry')
}
"""

employee = {
    'employee_id': None,
    'employee_name': None,
    'account_number': None,
    'salary': None,
    'address': {},
    'awards': [],
    'subjects_enrolled': ()
}


def name():
    employee.update({'employee_name': input("Enter Name: ")})


def identity():
    employee.update({'employee_id': int(input("Enter ID: "))})


def acc_num():
    employee.update({'account_number': int(input("Enter account number: "))})


def salary():
    employee.update({'salary': float(input("Enter salary: "))})


def address():
    work_address = input("Enter work address: ")
    home_address = input("Enter home address: ")
    employee.update({'address': {'work_address': work_address, 'home_address': home_address}})


def awards():
    award = input("Enter awards (separated by comma): ").split(",")
    employee.update({'awards': award})


def subjects():
    subs = input("Enter the subjects enrolled in (separated by comma): ").split(",")
    employee.update({'subjects_enrolled': tuple(subs)})


name()
identity()
acc_num()
salary()
address()
awards()
subjects()
print(employee)
