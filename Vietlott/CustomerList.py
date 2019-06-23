# Info of a customer includes name, birthdate, address, phone, email
import datetime


class Customer:
    def __init__(self, name: str, birthdate: datetime.date, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthdate = birthdate

    def __str__(self):
        return "Name: {}, Birthdate: {}, Address: {}, Phone: {}, Email: {}\n"\
            .format(self.name, self.birthdate, self.address, self.phone, self.email)

    def __repr__(self):
        return "Customer({}, {}, {}, {}, {})\n"\
            .format(self.name, self.birthdate, self.address, self.phone, self.email)

    # ----------------------------------------------------------------------------------------------------------
    @staticmethod
    def input_customer_details():
        name = input("Customer name: ")
        address = input("Customer address: ")
        phone = input("Customer phone: ")
        email = input("Customer email: ")
        try:
            year_of_birth = int(input("Customer year of birth: "))
            month_of_birth = int(input("Customer month of birth: "))
            day_of_birth = int(input("Customer day of birth: "))
            birthdate = datetime.date(year_of_birth, month_of_birth, day_of_birth)
            return Customer(name, birthdate, address, phone, email)
        except ValueError:
            print("\nInvalid birthdate! Please check!")
            return None
# ----------------------------------------------------------------------------------------------------------


class CustomerList:
    def __init__(self):
        self.customer_list = []

    def __str__(self):
        if not self.customer_list:
            return "Haven't seen any customer yet :)"
        else:
            string = "\nCustomer List:\n"
            for i in range(0, len(self.customer_list)):
                string += "Customer {} -> {}".format(i, self.customer_list[i])
            return string

    def __len__(self):
        return len(self.customer_list)

    # CustomerList CRUD
    def add_customer(self, customer: Customer):
        if customer is None:
            print("Can't add an invalid customer!")
            return
        else:
            self.customer_list.append(customer)

    def delete_customer(self, index: int):
        if not self.customer_list:
            print("There's nothing to delete :)")
            return
        else:
            try:
                del self.customer_list[index]
            except IndexError:
                print("\nInvalid index! Please check!\nData: unchanged")
                return

    def update_customer(self, customer: Customer, index: int):
        if customer is None:
            print("Cannot update a customer with invalid details.\nData: unchanged")
            return
        else:
            try:
                self.customer_list[index] = customer
            except IndexError:
                print("Invalid index! Please check!\nData: unchanged")
                return
