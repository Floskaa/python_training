# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random
import allure


def test_modify_some_contact_db(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given random contact from the list"):
        contact = random.choice(old_contacts)
        new_data = Contact(firstname="New contact db")
        index = old_contacts.index(contact)
    with allure.step("When I modify the contact from the list"):
        app.contact.modify_contact_by_index(index, new_data)
    with allure.step("Then new contact list is equal to the old list"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_some_contact(app):
    with allure.step("Given a non-empty contact list"):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="test"))
        old_contacts = app.contact.get_contact_list()
    with allure.step("Given random contact from the list"):
        index = randrange(len(old_contacts))
        contact = Contact(firstname="New modify contact")
        contact.id = old_contacts[index].id
    with allure.step("When I modify the contact from the list"):
        app.contact.modify_contact_by_index(index, contact)
    with allure.step("Then new contact list is equal to the old list"):
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

