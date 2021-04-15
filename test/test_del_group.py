# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random
import allure


def test_delete_some_group_db(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given random group from the list"):
        group = random.choice(old_groups)
    with allure.step("When I delete the group from the list"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then new group list is equal to the old list without the group"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_some_group(app):
    with allure.step("Given a non-empty group list"):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
    with allure.step("Given random group from the list"):
        index = randrange(len(old_groups))
    with allure.step("When I delete the group from the list"):
        app.group.delete_group_by_index(index)
    with allure.step("Then new group list is equal to the old list without the group"):
        new_groups = app.group.get_group_list()
        assert len(old_groups) - 1 == app.group.count()
        old_groups[index:index+1] = []
        assert old_groups == new_groups


def test_delete_first_group(app):
    with allure.step("Given a non-empty group list"):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
    with allure.step("When I delete the group from the list"):
        app.group.delete_first_group()
    with allure.step("Then new group list is equal to the old list without the group"):
        new_groups = app.group.get_group_list()
        assert len(old_groups) - 1 == app.group.count()
        old_groups[0:1] = []
        assert old_groups == new_groups
