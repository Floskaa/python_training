# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.create(Group(name="qwertrvf", header="cfserfersc", footer="wefawerfaee"))


def test_add_empty_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.create(Group(name="", header="", footer=""))
