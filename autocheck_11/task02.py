import json


def write_contacts_to_file(filename, contacts):
    json_structure = {}
    json_structure["contacts"] = contacts
    
    with open(filename, 'w') as fh:
        json.dump(json_structure, fh, indent=4)


def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        res = json.load(fh)
        return res['contacts']
    

filename = './contacts.json'
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Post Man API",
        "email": "nulla.post@vestibul.co.uk",
        "phone": "(999) 000-1122",
        "favorite": True,
    }

]
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))

