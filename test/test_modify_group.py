# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random
import allure


def test_modify_group_name_db(app, db, check_ui):
    with allure.step("Given a non-empty group list from DB"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given random group from the list"):
        group = random.choice(old_groups)
        new_data = Group(name="New update name")
    with allure.step("When I modify the group from the list"):
        app.group.modify_group_by_id(group.id, new_data)
    with allure.step("Then new group list is equal to the old list"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app):
    with allure.step("Given a non-empty group list from UI"):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
    with allure.step("Given random group from the list"):
        index = randrange(len(old_groups))
        group = Group(name="New update")
        group.id = old_groups[index].id
    with allure.step("When I modify the group from the list"):
        app.group.modify_group_by_index(index, group)
    with allure.step("Then new group list is equal to the old list"):
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count()
