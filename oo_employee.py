class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, name, no_of_years):
        # instance attribute
        self.name = name
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"Name: {self.name}\nYears Worked: {self.no_of_years}\nEmployee Number: {self.employee_no}\n"


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    Note that a mixin has no __init__ as you cannot create an instance of a mixin
    """
    def calculate_holidays(self, no_of_years):
        """
        Method that returns holidays as an integer if given no of years of service
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if no_of_years < 3:
            bonus = holidays + 1
        elif no_of_years <= 5:
            bonus = holidays + 2
        elif no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class but also inheriting from HolidayMixin
    """
    def __init__(self, name, no_of_years, skills, cloud_experience):
        self.skills = skills
        self.cloud_experience = cloud_experience
        Employee.__init__(self, name, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 40000
        cloud_bonus = 0

        if self.cloud_experience:  # Check if cloud_experience is True
            cloud_bonus = 3500

        prog_lang_bonuses = {  
            'java': 0.1,
            'python': 0.20,
            'ruby': 0.00,
            'go': 0.05,
            'excel': 0.015,
            'bash': 0.20,
            'c++': 0.001,
            'c': 0.005,
            'googlecli': 0.25,
            'javascript': 0.20,
            'html': 0.15,
            'css':0.15,
            'php': 0.009,
            'laravel': 0.01,
            'django': 0.05,
            'react': 0.0,
            'nodejs': 0.01,
            'flask': 0.0,
            'powershell': 0.10,
            'terraform': 0.25,
            'ansible': 0.10, 
        }

        bonus = sum(base * prog_lang_bonuses.get(skill.lower(), 0) for skill in self.skills)

        return base + bonus + cloud_bonus

    def get_details(self):
        """
        Method to return direct developer details as a string
        Uses details() method inherited from Employee super class
        """
        return Employee.details(self) + f'Skills: {", ".join(self.skills)}\nCloud Experience: {self.cloud_experience}\n'


# Create an instance of DirectDeveloper
eric = DirectDeveloper("Eric Praline", 2, ["python", "javascript", "html", "django"], False)

# Prints out all the attributes of your eric instance using get_details method from DirectDeveloper
# If you use the details method from Employee then the Skills and Cloud Experience will not print
print(eric.get_details())

# The mixin method is usable for instance eric
print(eric.calculate_holidays(eric.no_of_years))

# Uses the calculate_salary method from DirectDeveloper
print(f'£{eric.calculate_salary()}')

# Create an instance of DirectDeveloper
justin = DirectDeveloper("JRE", 4, ["java", "python", "go", "bash", "googlecli", "javascript", "html", "css", "php", "laravel", "django", "nodejs", "powershell", "terraform", "ansible"], True)
print(justin.get_details())
print(justin.calculate_holidays(justin.no_of_years))
print(f'£{justin.calculate_salary()}')

"""
Calculate yours!
"""

