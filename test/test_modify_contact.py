# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New update contact"))
    app.session.logout()

def test_modify_contact_foto(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(photo="C:\\Devel\\petrov4.jpg"))
    app.session.logout()