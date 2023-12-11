# import sqlite3

# connection = sqlite3.connect("crm.db")

# cursor = connection.cursor()

# try:
#     cursor.execute("drop table accounts")
#     cursor.execute("drop table contacts")
#     cursor.execute("drop table account_contacts")
# except:
#     pass

# cursor.execute("create table accounts(id integer primary key, Name text, Description text)")
# cursor.execute("create table contacts(id integer primary key, Name text, Description text)")
# cursor.execute("create table accounts(id integer primary key, account_id integer, contact_id integer, foreign key (account_id) references accounts (id), foreign key (contact_id) references contacts (id)")

# for account in [
#     {name: 'Kent State University', Description: 'University at Kent'},
#     {name: 'Akron State University', Description: 'University at Akron'},
#     {name: 'Cleveland State University', Description: 'University at Cleveland'},
#     ]:
#     cursor.execute(f"insert into accounts (name, description) values ({account['item']}, {account['description']})")

# for contact in [
#     {name: 'Raghupathi Allapuram', Description: 'Computer Science grad'},
#     {name: 'Daniel Porter', Description: 'Director at Department of Philanthropy'},
#     {name: 'Greg', Description: 'Professor'},
#     ]:
#     cursor.execute(f"insert into contacts (name, description) values ({contact['item']}, {contact['description']})")



connection.commit()
connection.close()
