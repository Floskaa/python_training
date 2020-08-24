# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixtere = Application()
    request.addfinalizer(fixtere.destroy)
    return fixtere

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_gruop(Group(name="qwertrvf", header="cfserfersc", footer="wefawerfaee"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_gruop(Group(name="", header="", footer=""))
    app.logout()

