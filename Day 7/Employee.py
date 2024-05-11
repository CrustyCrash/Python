class Employee:
    department_name = "Cloud"
    __emp_id = None
    __emp_salary = None
    __mgr_id = None
    __emp_expertise = None

    @classmethod
    def get_department_name(cls):
        return cls.department_name

    def __init__(self, emp_id, emp_salary, mgr_id):
        self.__emp_id = emp_id
        self.__emp_salary = emp_salary
        self.__mgr_id = mgr_id

    def get_emp_id(self):
        return self.__emp_id

    def get_emp_salary(self):
        return self.__emp_salary

    def get_mgr_id(self):
        return self.__mgr_id

    def del_expertise(self):
        del self.__mgr_id

    @staticmethod
    def field_expertise():
        return "HPC Engineer"

    def __del__(self):
        print("Deleting object.")


def main():
    employees = Employee(100, 1000, 1)

    print("Department name is: ", Employee.get_department_name())
    print("Employee ID is: ", employees.get_emp_id())
    print("Employee salary is: ", employees.get_emp_salary())
    print("Employee mgr_id is: ", employees.get_mgr_id())
    print("Expertise is: ", employees.field_expertise())

    print("Deleting mgr_id attribute ", employees.del_expertise())
    del employees


main()
