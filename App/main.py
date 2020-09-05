import random
import pickle


class Person:
    id = 0

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.id = Person.id
        Person.id += 1

    def change_name(self, name):
        self.name = name

    def change_phone_number(self, phone_number):
        self.phone_number = phone_number


class PhoneBook:
    book_arr = {}
    save_file = 'save_file.data'

    def __init__(self):
        """ Create list for phone book """

    @staticmethod
    def add_person(person: Person):
        """ Add person to book """
        PhoneBook.book_arr[person.id] = person

    @staticmethod
    def del_person(person: Person):
        """ Delete person from book """
        del PhoneBook.book_arr[person.name]

    @staticmethod
    def show_list():
        for id, person in PhoneBook.book_arr.items():
            print("id is {0}, name is {1}, phone number is {2}".format(id, person.name, person.phone_number))

    @staticmethod
    def save_book():
        f = open(PhoneBook.save_file, 'wb')
        pickle.dump(PhoneBook.book_arr)
        f.close()

    @staticmethod
    def load_book():
        f = open(PhoneBook.save_file, 'rb')
        PhoneBook.book_arr = pickle.load(f)


class PhoneBookUI:
    book: PhoneBook = None

    def __init__(self):
        """ Create list for phone book """
        PhoneBookUI.book = PhoneBook()
        PhoneBookUI.menu_UI()

    @staticmethod
    def menu_UI():
        while True:
            menu_list = '1. Add to book\n2. Dell from book\n3. Show book\n0. Exit\n\n'
            number = int(input(menu_list + 'Input number ---> '))

            if number == 1:
                PhoneBookUI.add_person_UI()
            elif number == 2:
                print('del el')
            elif number == 3:
                PhoneBookUI.show_list_UI()

            cont = input('Would you like to continue(y/n) ---> ')

            if cont == 'y':
                break

    @staticmethod
    def add_person_UI():
        name = input('Input name ---> ')
        phone_number = input('Input phone number ---> ')
        PhoneBookUI.book.add_person(Person(name, phone_number))

    @staticmethod
    def show_list_UI():
        for id, person in PhoneBook.book_arr.items():
            print("id is {0}, name is {1}, phone number is {2}".format(id, person.name, person.phone_number))


def main():
    PhoneBookUI()


if __name__ == '__main__':
    main()
