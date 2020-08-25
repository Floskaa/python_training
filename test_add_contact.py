# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Sofia", middlename="Ivanovna", lastname="Petrova", nickname="Sofi",
                                    title="prosto test", company="Romashka", address="Kirova str 5",
                                    home="1333434343",
                                    mobile="8923445445", work="2343434444", fax="8923232323",
                                    email="sofi@gmail.com",
                                    email2="sofi2@gmail.ru", email3="sofi3@mail.ru", homepage="sofi.net",
                                    address2="Pervaya str 4",
                                    phone2="1243", note="test contact"))
    app.logout()

