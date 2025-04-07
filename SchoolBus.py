class Vehicle:
    def __init__(self, brand, model):
        # Private attributes
        self.__brand = brand
        self.__model = model

    # Getter and Setter for maker
    def get_make(self):
        return self.__brand

    def set_make(self, make):
        self.__brand = make

    # Getter and Setter for model
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    # Method to display vehicle details
    def display_details(self):
        print(f"Vehicle Maker: {self.__brand}, Model: {self.__model}")




class SchoolBus(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    # Overriding display_details method to show school bus details
    def display_details(self):
        super().display_details()  # Call the parent class method



# Create an instance of SchoolBus
schoolBus = SchoolBus("Ford", "Transit")

# Check if schoolBus is an instance of Vehicle
if isinstance(schoolBus, Vehicle):
    print("SchoolBus is an instance of Vehicle")

# Display the details of the school bus
schoolBus.display_details()
