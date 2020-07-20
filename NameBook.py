class BaseContact:
    def __init__(self, name, last_name, phone_number, adress, email):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.adress = adress
        self.email = email

        #Variables
        self._label_lenght = 0

    def __str__(self):
        return f'{self.name} {self.last_name}\n{self.adress}\ntel: {self.phone_number}\nemail: {self.email}'

    def contact(self):
        print(f'Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.last_name}')

    #@property
    #def label_lenght(self):
        return self._label_lenght

    #@label_lenght.setter
    def label_lenght(self):
         self._label_lenght = len(self.name) + len(self.last_name) + len(" ")
         print(f'{self._label_lenght}')

class BusinessContact(BaseContact):
   def __init__(self, position, company_name, bussines_phone,company_email, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company_name = company_name
       self.bussines_phone = bussines_phone
       self.company_email = company_email

   def __str__(self):
       return f'{self.company_name}\n{self.name} {self.last_name}\n{self.position}\ntel: {self.bussines_phone}\nemail {self.company_email} '


   def contact(self):
       print(f'Wybieram numer {self.bussines_phone} i dzwonię do {self.name} {self.last_name}')

def create_contacts(contact_type='Base', quantity='1'):
    '''Generetes random cards. Quantity and type of card depends on given arguments
    Base - private card
    Bussines - bussines card'''

    quantity = int(quantity)
    from faker import Faker
    fake = Faker('pl_PL')

    genereted_contacts =[]
    if contact_type == 'Base':
        for item in range(quantity):
            item = fake.last_name()
            item = BaseContact(name = fake.first_name(),  last_name = fake.last_name(),\
                               phone_number = fake.phone_number(), adress = fake.address(),\
                               email = fake.ascii_free_email() )
            genereted_contacts.append(item)
        return genereted_contacts

    elif contact_type == 'Bussines':
        for item in range(quantity):
            item = fake.last_name()
            item = BusinessContact(name=fake.first_name(), last_name=fake.last_name(), \
                                   phone_number = fake.phone_number(),adress=fake.address(), email=fake.ascii_free_email(),\
                                   company_name=fake.company(),bussines_phone= fake.phone_number(),\
                                   company_email=fake.ascii_company_email(),position=fake.job())
            genereted_contacts.append(item)
        return genereted_contacts
    else:
        print('Function accepts only two contact types\nBase and Bussines')
        return None

contacts = create_contacts('Base','5')

print(contacts[1])
BaseContact.contact(contacts[1])
BaseContact.label_lenght(contacts[1])