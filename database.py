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
    # items = [
    #     { 
    #         "id" : item.id,
    #         "description" : item.description
    #     }
    #     for item in items
    # ]
    return accounts


def add_account(name, description):
    account = Account(name=name, description=description)
    account.save()

def delete_account(id):
    account = Account.select().where(Account.id == id).get()
    account.delete_instance()

def update_account(id, name, description):
    # item = Item.select().where(Item.id == id).get()
    # item.description = description
    # item.save()
    Account.update({Account.name: name, Account.description: description}).where(Account.id == id).execute()

def get_contacts(id=None):
    if id == None:
        contacts = Contact.select()
    else:
        contacts = Contact.select().where(Contact.id == id)
    # items = [
    #     { 
    #         "id" : item.id,
    #         "description" : item.description
    #     }
    #     for item in items
    # ]
    return contacts

def add_contact(name, description):
    contact = Contact(name=name, description=description)
    contact.save()

def delete_contact(id):
    contact = Contact.select().where(Contact.id == id).get()
    contact.delete_instance()

def update_contact(id, name, description):
    # item = Item.select().where(Item.id == id).get()
    # item.description = description
    # item.save()
    Contact.update({Contact.name: name, Contact.description: description}).where(Contact.id == id).execute()

def add_contact_to_account(account_id, contact_id):
    account = Account.select().where(Account.id == account_id)
    contact = Contact.select().where(Contact.id == contact_id)
    account.contacts.add(contact)

# def test_setup_database():
#     print("testing setup_database()")
#     setup_database()
#     items = get_items()
#     assert len(items) == 5
#     descriptions = [item['description'] for item in items]
#     for description in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
#         assert description in descriptions

# def test_get_items():
#     print("testing get_items()")
#     setup_database()
#     items = get_items()
#     assert type(items) is list
#     assert len(items) > 0
#     for item in items:
#         assert 'id' in item
#         assert type(item['id']) is int
#         assert 'description' in item
#         assert type(item['description']) is str
#     example_id = items[0]['id']
#     example_description = items[0]['description']
#     items = get_items(example_id)
#     assert len(items) == 1
#     assert example_id == items[0]['id']
#     assert example_description == items[0]['description']

# def test_add_item():
#     print("testing add_item()")
#     setup_database()
#     items = get_items()
#     original_length = len(items)
#     add_item("licorice")
#     items = get_items()
#     assert len(items) == original_length + 1
#     descriptions = [item['description'] for item in items]
#     assert "licorice" in descriptions

# def test_delete_item():
#     print("testing delete_item()")
#     setup_database()
#     items = get_items()
#     original_length = len(items)
#     deleted_description = items[1]['description']
#     deleted_id = items[1]['id']
#     delete_item(deleted_id)
#     items = get_items()
#     assert len(items) == original_length - 1
#     for item in items:
#         assert item['id'] != deleted_id
#         assert item['description'] != deleted_description

# def test_update_item():
#     print("testing update_item()")
#     setup_database()
#     items = get_items()
#     original_description = items[1]['description']
#     original_id = items[1]['id']
#     update_item(original_id,"new-description")
#     items = get_items()
#     found = False
#     for item in items:
#         if item['id'] == original_id:
#             assert item['description'] == "new-description"
#             found = True
#     assert found

