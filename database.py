from peewee import *

db = SqliteDatabase('crm.db')
db.connect()

class Contact(Model):
    name = CharField()
    description = CharField()
    class Meta:
        database = db

class Account(Model):
    name = CharField()
    description = CharField()
    contacts = ManyToManyField(Contact, backref='accounts')
    class Meta:
        database = db 

AccountContactRelation = Account.contacts.get_through_model()

def setup_database():
    Account.drop_table(safe=True)
    Contact.drop_table(safe=True)
    AccountContactRelation.drop_table(safe=True)
    Account.create_table()
    Contact.create_table()
    AccountContactRelation.create_table()

def get_accounts(id=None):
    if id == None:
        accounts = Account.select()
    else:
        accounts = Account.select().where(Account.id == id)
    return accounts


def add_account(name, description):
    account = Account(name=name, description=description)
    account.save()

def delete_account(id):
    account = Account.select().where(Account.id == id).get()
    account.delete_instance()

def update_account(id, name, description):
    Account.update({Account.name: name, Account.description: description}).where(Account.id == id).execute()

def get_contacts(id=None):
    if id == None:
        contacts = Contact.select()
    else:
        print('test')
        contacts = Contact.select().where(Contact.id == id)
    return contacts

def add_contact(name, description):
    contact = Contact(name=name, description=description)
    contact.save()

def delete_contact(id):
    contact = Contact.select().where(Contact.id == id).get()
    contact.delete_instance()

def update_contact(id, name, description):
    Contact.update({Contact.name: name, Contact.description: description}).where(Contact.id == id).execute()

