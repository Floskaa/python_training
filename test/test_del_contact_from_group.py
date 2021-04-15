from model.contact import Contact
from model.group import Group
import random
import allure
# from fixture.orm import ORMFixture
#
# orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, orm,  db):
    with allure.step("Given non-empty contact and group list from db"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test"))

        groups = db.get_group_list()
        group_index = random.randrange(len(groups))
        group_id = groups[group_index].id
        contacts = db.get_contact_list()

    with allure.step(f'Given random contact in group'):
        if len(orm.get_contacts_in_group(groups[group_index])) == 0:
            contact_index = random.randrange(len(contacts))
            contact = contacts[contact_index]
            contact_id = contact.id
            app.contact.add_contact_to_group(contact_id, group_id)
        else:
            contact = random.choice(orm.get_contacts_in_group(groups[group_index]))
            contact_id = contact.id
    with allure.step("When I delete contacts from the group"):
        app.contact.del_contact_from_group(contact_id, group_id)
    with allure.step("Then chek that contact not in group list"):
        assert contact not in orm.get_contacts_in_group(groups[group_index])
