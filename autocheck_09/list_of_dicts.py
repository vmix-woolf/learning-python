class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact['id'] == id:
                return contact
            else:
                return None
                
contacts = Contacts()
contacts.add_contacts('Gerda', '050-4445566', 'email@example.com', True)
print(contacts.get_contact_by_id(1))
print(contacts.get_contact_by_id(2))
