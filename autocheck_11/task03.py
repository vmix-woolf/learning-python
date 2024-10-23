import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as fh:
        columns = ['name', 'email', 'phone', 'favorite']    
        writer = csv.DictWriter(fh, delimiter=',', fieldnames=columns)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)
        

def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        with open(filename, 'r') as fh:
            reader = csv.DictReader(fh)
            lst = []
            for row in reader:
                row['favorite'] = True if row['favorite'] == 'True' else False
                lst.append(row)
            return lst
    

filename = './students.csv'
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    },
    {
        "name": "Chaim Lewis",
        "email": "ui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris",
        "phone": "(542) 451-7038",
        "favorite": True
    },
    {
        "name": "Wylie Pope",
        "email": "est@utquamvel.net",
        "phone": "(692) 802-2949",
        "favorite": False
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat",
        "phone": "(501) 472-5218",
        "favorite": True
    }
]


write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))
