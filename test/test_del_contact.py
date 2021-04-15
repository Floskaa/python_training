# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random
import allure


def test_delete_some_contact_db(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given random contact from the list"):
        contact = random.choice(old_contacts)
    with allure.step("When I delete the contact from the list"):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then new contact list is equal to the old list without the contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_some_contact(app):
    with allure.step("Given a non-empty contact list"):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="test"))
        old_contacts = app.contact.get_contact_list()
    with allure.step("Given random contact from the list"):
        # функция randrange генерит случайное число от 0 до указанного
        index = randrange(len(old_contacts))
    with allure.step("When I delete a contact from the list"):
        app.contact.delete_contact_by_index(index)
    with allure.step("Then new contact list is equal to the old list without the contact"):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index:index+1] = []
        assert old_contacts == new_contacts
