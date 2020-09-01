import random


class Person:
    id = 0

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Person.id += 1

    def change_name(self, name):
        self.name = name

    def change_phone_number(self, phone_number):
        self.phone_number = phone_number


class PhoneBook:
    list = None

    def __init__(self):
        """ Create list for phone book """
        PhoneBook.list = dict

    @staticmethod
    def add_person(person: Person):
        """ Add person to book 
        :type person: Person
        """
        PhoneBook.list.update({person.name : person.phone_number})

    @staticmethod
    def del_person(person: Person):
        """ Delete person from book
        :type person: Person
        """
        del PhoneBook.list[person.name]

    @staticmethod
    def show_list():
        for name, phone in PhoneBook.list.items():
            print("name is {0}, phone number is {1}".format(name, phone))


book = PhoneBook()

tmp_list_name = ("Alex", "Olga", "Danial", "Julia", "Anastasia", "Inna", "Valeria")
tmp_list_phone_number = ("+38099153223", "+380112751923", "+380932876923", "+3809365365323")

for name in range(4):
    person = Person(tmp_list_name[random.randint(0, 6)], tmp_list_phone_number[random.randint(0, 3)])
    book.add_person(person)
    print("name is {0}, phone number is {1}".format(person.name, person.phone_number))

# book.show_list()
