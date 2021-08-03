class Contact:
    def __init__(self, name, surname, number, email):
        self.name=name
        self.surname=surname
        self.number=number
        self.email=email
    def edit_name(self, name):
        self.name=name
        return self.name
    def edit_surname(self, surname):
        self.surname=surname
        return self.surname
    def edit_number(self, number):
        self.number=number
        return self.number
    def edit_email(self, email):
        self.email=email
        return self.email

    @classmethod
    def add(cls, name, surname, number, email):
        cls(name, surname, number, email)

        print('CONTACTS SAVED: ', end='')
        for i, contact in enumerate(address_books):
            print(i, contact.name, end=' || ')

        if not address_books:
            print('NO CONTACT SAVED\n')
address_books =[]
msg_error = '{}Invalid option{}'.format('\033[31m', '\033[m')
access = input('Press any key to access')

while True:
        print('=-=-===-=-=-=-=-  CONTACTS MENU -=-=-=-=-=-==-==')
        print("""[ 1 ] ADD    [ 3 ] DELETE     [ 5 ] VIEW ALL
        [ 2 ] MODIFY    [ 4 ] VIEW   [ 0 ] FINISH """)
        option = input('>>> ')
        entry_index=[]

        #input from user
        if not option.isnumeric():
            print(msg_error)
            continue
        elif option not in '12345':
            print(msg_error)
            continue
        else:
            option=int(option)
        if option == 0:
            print("program end/n")
            break

        elif option==1:
            name =input('First_Name').capitalize().strip()
            surname=input('Last_Name').capitalize().strip()
            number=input('Phone_number').strip()
            email=input('Email').lower().strip()

            address_books.append(Contact.add(name, surname, number, email))
            print("Contact saved\n")

        elif option ==2:
            if Contact(address_books):
                continue
                contact_saved()
                name_index=int(input("modify which name"))
                print("modify which entry")
                entry_index = int(input('[1]first_name, [2]last_name, [3]phone_number, [4]address, [5]email'))
            if entry_index == 1:
                modification = input('New name: ').capitalize().strip()
                address_books[name_index].edit_name(modification)

                # User wants to modify surname
            elif entry_index == 2:
                modification = input('New surname: ').capitalize().strip()
                address_books[name_index].edit_surname(modification)

                # User wants to modify number
            elif entry_index == 3:
                modification = input('New number: ').strip()
                address_books[name_index].edit_number(modification)

                # User wants to modify email

            elif entry_index == 4:
                modification = input('New email: ').lower().strip()
                address_books[name_index].edit_email(modification)
            print('Modification saved\n')

            # Delete a contact

        elif option == 3:
            if Contact(address_books):
                continue

            Contact.saved()
            name_index = int(input('\nWhich contact delete? '))
            del address_books[name_index]
            print('Contact deleted')

            # View specific contact details

        elif option == 4:
            if Contact(address_books):
                continue

            Contact.saved()
            index = int(input('\nContact position: '))
            Contact.summary(index)

            # View details of all contacts
        elif option == 5:
            if Contact(address_books):
                continue
            Contact.summary()


