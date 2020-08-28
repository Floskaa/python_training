# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Andrey", middlename="Sergeevich", lastname="Smirnov", nickname="Andru",
                               title="test edit", company="Cheburek", address="Nikolskaya str., 1",
                               home="+7(987)654321",
                               mobile="7(923)445445", work="7(234)3434444", fax="7(923)2323234",
                               email="andru@gmail.com",
                               email2="andru2@gmail.ru", email3="andru3@mail.ru", homepage="andru.net",
                               address2="Vtoraya str 34",
                               phone2="7(904)8888888", note="test edit contact"))
    app.session.logout()