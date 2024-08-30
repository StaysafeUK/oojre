class JobListing():
    """
    Creates an instance of JobListing
    """
    def __init__(self, job_title, department):
        self.job_title = job_title
        self.department = department
    
    def description(self):
        return f"Job opening for {self.job_title} in {self.department} department"

# write your code here
class SalesManager(JobListing):
    """
    Subclass Joblisting
    """
    def __init__(self, salary):
        JobListing.__init__(self, "Sales Manager", "Sales")
        self.salary = salary
        

sales_manager = SalesManager(45000)
print(sales_manager.description())
print(sales_manager.salary)
            

    
# e_nd do not remove