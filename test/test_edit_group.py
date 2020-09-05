# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="New group", header="12345", footer="testtesttest"))
