from Employee import Employee


class Manager(Employee):
    managed_employee = []
    Employee.set_name("HelloWorld")

    print("Organisation Name is :", Employee.organisation_name)

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary, managed_list):
        super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
        self.managed_list = managed_list

    def detail(self):
        super().get_employee_details()
        for obj in self.managed_list:
            obj.get_employee_details()

    # def salary_appraisal(self, reference, percent):


def main():
    obj1 = Employee(1, "John", "Pune", "Delhi", "Manager", 120000)
    obj2 = Employee(2, "Mark", "Mumbai", "Bangalore", "Engineer", 100000)
    obj3 = Employee(3, "Victor", "Delhi", "Delhi", "HR", 100000)

    managerObj = Manager(4, "Man", "Chandigarh", "Delhi", "HPC", 150000, [obj1, obj2, obj3])

    managerObj.detail()
    # managerObj.salary_appraisal(obj1, 15)
    # managerObj.detail()


main()
