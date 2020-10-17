
import re
from random import randrange

def clear(s):
    return re.sub("[() -]", "", s)

def test_all_info_on_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
    # join - склеивается то что осталось при помощи перевода строки. filter - отфильтровываются все пустые строки
                            map(lambda x: clear(x),
                            # К оставшимся применяется clear, которая удаляет все лишние символы
                                filter(lambda x: x is not None,
                                # список фильтруется и выкидываются все пустые значения
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))
                                        #исходный список

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
