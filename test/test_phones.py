import re
from model.contact import Contact
# from random import randrange
import allure


def test_info_on_home_page_db(app, db):
    with allure.step("Given contact list from DB and UI"):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        contact_from_db_page = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step("Then contact info from UI equals contact info from DB"):
        for number in range(len(db.get_contact_list())):
            assert contact_from_home_page[number].firstname == contact_from_db_page[number].firstname
            assert contact_from_home_page[number].lastname == contact_from_db_page[number].lastname
            assert contact_from_home_page[number].all_phones == merge_phones_like_on_home_page(contact_from_db_page[number])
            assert contact_from_home_page[number].all_emails == merge_emails_like_on_home_page(contact_from_db_page[number])


def test_phones_on_home_page(app):
    with allure.step("Given phones list from home page"):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with allure.step("Given phones list from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with allure.step("Then phones list from home page equals phones list from edit page"):
        assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)


# def test_phones_on_contact_view_page(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                 [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))
