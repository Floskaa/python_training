from model.group import Group
# from timeit import timeit
import allure


def test_group_list(app, db):
    with allure.step('Given a group list from UI'):
        ui_list = app.group.get_group_list()
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
    with allure.step('Given a group list from DB'):
        db_list = map(clean, db.get_group_list())
    with allure.step('Then group list from UI equals to group list from DB'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


# def test_time_group_list(app, db):
#     print(timeit(lambda: app.group.get_group_list(), number=1))
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#     print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
#     assert False
