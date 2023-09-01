from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if isinstance(phone, Phone):
            self.phones.append(phone)
        else:
            raise ValueError("Invalid phone format")

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone not found in record")

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        else:
            raise ValueError("Phone not found in record")

    def __str__(self):
        phone_str = ", ".join([str(phone.value) for phone in self.phones])
        return f"Name: {self.name.value}, Phones: {phone_str}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        if isinstance(record, Record):
            self.data[record.name.value] = record
        else:
            raise ValueError("Invalid record format")

    def find_records(self, criteria):
        found_records = []
        for record in self.data.values():
            if criteria in record.name.value:
                found_records.append(record)
        return found_records

# Приклад використання:

# Створення адресної книги
address_book = AddressBook()

# Створення записів
record1 = Record("John")
phone1 = Phone("123-456-7890")
record1.add_phone(phone1)

record2 = Record("Alice")
phone2 = Phone("987-654-3210")
record2.add_phone(phone2)

# Додавання записів до адресної книги
address_book.add_record(record1)
address_book.add_record(record2)

# Пошук записів за іменем
found_records = address_book.find_records("John")
for record in found_records:
    print(record)
