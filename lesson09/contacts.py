from collections import UserDict

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"
        
    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")
    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")
    for customer in customers:
        print(customer.email_info())

