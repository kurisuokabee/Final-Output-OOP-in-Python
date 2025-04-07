class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @classmethod
    def from_name(cls, name):
        return cls(name, department = "IT")
    
    @classmethod
    def from_dict(cls, info_dict):
        return cls(
            name=info_dict.get("name", "Unknown"),
            department=info_dict.get("department", "Unknown")
        )
    
    def __str__(self):
        return f"Name: {self.name}, Department: {self.department}"
    
#Main constructor
employee_1 = Employee("Serg", "Finance")

#Using from_name constructor
employee_2 = Employee.from_name("Angelo")

#Using from_dict constructor
employee_3 = Employee.from_dict({"name": "David", "department": "Security"})

#Print the objects
print(employee_1)
print(employee_2)
print(employee_3)