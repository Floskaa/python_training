# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Sofia", middlename="Ivanovna", lastname="Petrova", nickname="Sofi",
                               photo="C:\\Devel\\Andru.jpg", title="prosto test", company="Romashka",
                               address="Kirova str 5", home="1333434343",
                               mobile="8923445445", work="2343434444", fax="8923232323", email="sofi@gmail.com",
                               email2="sofi2@gmail.ru", email3="sofi3@mail.ru", homepage="sofi.net",
                               bday="19", bmonth="April", byear="1989", aday="6", amonth="May", ayear="1999",
                               address2="Pervaya str 4",
                               phone2="1243", note="test contact"))
    app.session.logout()

