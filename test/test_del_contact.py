from model.contact import Contact
from random import randrange


# def test_delete_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create_for_edit_contact(Contact(firstname="Test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0:1] = []
#     assert old_contacts == new_contacts


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_for_edit_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    # функция randrange генерит случайное число от 0 до указанного
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
