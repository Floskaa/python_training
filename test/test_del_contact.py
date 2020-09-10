
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_for_edit_contact(Contact(firstname="Test"))
    app.contact.delete_first_contact()
