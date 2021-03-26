from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(groups)
#         print(len(groups))
# finally:
#     db.destroy()

# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#         print(len(l))
# finally:
#     pass #db.destroy()

try:
    l = db.get_contacts_not_in_group(Group(id='144'))
    for item in l:
        print(item)
        print(len(l))
finally:
    pass #db.destroy()