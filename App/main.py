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
    file = 'save_file.pickle'

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
        with open(PhoneBook.file, 'wb') as file:
            pickle.dump(PhoneBook.book_arr, file)

    @staticmethod
    def load_book():
        with open(PhoneBook.file, 'rb') as file:
            new_book = pickle.load(file)
            print('Save book')

            PhoneBook.book_arr = new_book
            print('Load new book')



class PhoneBookUI:
    book: PhoneBook = None

    def __init__(self):
        """ Create list for phone book """
        PhoneBookUI.book = PhoneBook()
        PhoneBookUI.menu_UI()

    @staticmethod
    def cont():
        cont = input('Would you like to continue(y/n) ---> ')

        if cont == 'n':
            return False

        return True


    @staticmethod
    def menu_UI():
        run = True
        while run:
            menu_list = '1. Add to book\n2. Dell from book\n3. Show book\n4.Save book\n5.Load book\n0. Exit\n\n'
            number = int(input(menu_list + 'Input number ---> '))

            if number == 1:
                PhoneBookUI.add_person_UI()
            elif number == 2:
                print('del el')
            elif number == 3:
                PhoneBookUI.show_list_UI()
            elif number == 4:
                PhoneBookUI.save_book_UI()
            elif number == 5:
                PhoneBookUI.load_book_UI()
            elif number == 0:
                break

            run = PhoneBookUI.cont()

    @staticmethod
    def add_person_UI():
        name = input('Input name ---> ')
        phone_number = input('Input phone number ---> ')
        PhoneBookUI.book.add_person(Person(name, phone_number))

    @staticmethod
    def show_list_UI():
        for id, person in PhoneBook.book_arr.items():
            print("id is {0}, name is {1}, phone number is {2}".format(id, person.name, person.phone_number))

    @staticmethod
    def save_book_UI():
        answer = input(f'Would you like to save book?(y/n) ---> ')
        if answer == 'y':
            PhoneBookUI.book.save_book()
            print('Book was saved')

    @staticmethod
    def load_book_UI():
        answer = input(f'Would you like to load book?(y/n) ---> ')
        if answer == 'y':
            PhoneBookUI.book.load_book()
            print('Book was loaded')


def main():
    PhoneBookUI()


if __name__ == '__main__':
    main()
