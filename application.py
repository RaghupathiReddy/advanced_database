from bottle import route, post, run, template, redirect, request

import database

database.setup_database()

# Account routes
@route("/")
def index():
    query = request.query.get("q")
    if(query):
        rows = database.get_filtered_accounts(query)
    else:
        rows = database.get_accounts()
        query = ''
    return template("accounts/index.tpl", accounts=rows, query=query)

@route("/show/<id>")
def show(id):
    account = database.get_accounts(id)
    contacts = database.get_contacts()
    return template("accounts/show.tpl", account=account[0], contacts = contacts)

@route("/add")
def get_add():
    return template("accounts/create.tpl")

@post("/add")
def post_add():
    name = request.forms.get("name")
    description = request.forms.get("description")
    database.add_account(name, description)
    redirect("/")

@route("/delete/<id>")
def get_delete(id):
    database.delete_account(id)
    redirect("/")

@route("/update/<id>")
def get_update(id):
    rows = database.get_accounts(id)
    if len(rows) != 1:
        redirect("/")
    name = rows[0].name
    description = rows[0].description
    return template("accounts/update.tpl", id=id, name=name, description=description)

@post("/update")
def post_update():
    name = request.forms.get("name")
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_account(id, name, description)
    redirect("/")

# Contact routes
@route("/contacts")
def contacts_index():
    query = request.query.get("q")
    if(query):
        rows = database.get_filtered_contacts(query)
    else:
        rows = database.get_contacts()
        query = ''
    return template("contacts/index.tpl", contacts=rows, query=query)

@route("/contacts/show/<id>")
def show(id):
    contact = database.get_contacts(id)
    accounts = database.get_accounts()
    return template("contacts/show.tpl", contact=contact[0], accounts=accounts)

@route("/contacts/new")
def new_contact():
    return template("contacts/create.tpl")

@post("/contacts/add")
def create_contact():
    name = request.forms.get("name")
    description = request.forms.get("description")
    database.add_contact(name, description)
    redirect("/contacts")

@route("/contacts/delete/<id>")
def delete_contact(id):
    database.delete_contact(id)
    redirect("/contacts")

@route("/contacts/update/<id>")
def get_contact_update(id):
    rows = database.get_contacts(id)
    if len(rows) != 1:
        redirect("/contacts")
    name = rows[0].name
    description = rows[0].description
    return template("contacts/update.tpl", id=id, name=name, description=description)

@post("/contacts/update")
def post_contact_update():
    name = request.forms.get("name")
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_contact(id, name, description)
    redirect("/contacts")

# Association routes
@post("/add_account_contacts")
def add_contact_accounts():
    account_id = request.forms.get("account_id")
    contact_id = request.forms.get("contact_id")
    account = database.get_accounts(account_id)
    contact = database.get_contacts(contact_id)
    account[0].contacts.add(contact[0])
    previous_page = request.get_header('Referer') or '/'
    redirect(previous_page)

@route("/delete_contact_accounts/<account_id>/<contact_id>")
def remove_contact_accounts(account_id, contact_id):
    account = database.get_accounts(account_id)
    contact = database.get_contacts(contact_id)
    account[0].contacts.remove(contact[0])
    previous_page = request.get_header('Referer') or '/'
    redirect(previous_page)

run(host='localhost', port=8080)