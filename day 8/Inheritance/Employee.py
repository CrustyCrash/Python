class Employee:
    organisation_name = None
    emp_id = None
    name = None
    base_location = None
    deployed_location = None
    designation = None
    salary = None

    def get_employee_details(self):
        print("Employee ID is: ", self.emp_id)
        print("Employee name is: ", self.name)
        print("Employee base location is: ", self.base_location)
        print("Employee deployed location is: ", self.deployed_location)
        print("Employee designation is: ", self.designation)
        print("Employee salary is: ", self.salary)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    @classmethod
    def set_name(cls, organisation_name):
        cls.organisation_name = organisation_name

    def get_name(self):
        return self.organisation_name
