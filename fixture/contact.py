from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # click add new
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")
                and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

#     def fill_contact_form(self, contact):
#         wd = self.app.wd
#         wd.find_element_by_name("firstname").click()
#         wd.find_element_by_name("firstname").clear()
#         wd.find_element_by_name("firstname").send_keys(contact.firstname)
#         wd.find_element_by_name("middlename").click()
#         wd.find_element_by_name("middlename").clear()
#         wd.find_element_by_name("middlename").send_keys(contact.middlename)
#         wd.find_element_by_name("lastname").click()
#         wd.find_element_by_name("lastname").clear()
#         wd.find_element_by_name("lastname").send_keys(contact.lastname)
#         wd.find_element_by_name("nickname").click()
#         wd.find_element_by_name("nickname").clear()
#         wd.find_element_by_name("nickname").send_keys(contact.nickname)
# #        wd.find_element_by_name("photo").click()
# #        wd.find_element_by_name("photo").clear()
#         wd.find_element_by_name("photo").send_keys(contact.photo)
#         wd.find_element_by_name("title").click()
#         wd.find_element_by_name("title").clear()
#         wd.find_element_by_name("title").send_keys(contact.title)
#         wd.find_element_by_name("company").click()
#         wd.find_element_by_name("company").clear()
#         wd.find_element_by_name("company").send_keys(contact.company)
#         wd.find_element_by_name("address").click()
#         wd.find_element_by_name("address").clear()
#         wd.find_element_by_name("address").send_keys(contact.address)
#         wd.find_element_by_name("home").click()
#         wd.find_element_by_name("home").clear()
#         wd.find_element_by_name("home").send_keys(contact.home)
#         wd.find_element_by_name("mobile").click()
#         wd.find_element_by_name("mobile").clear()
#         wd.find_element_by_name("mobile").send_keys(contact.mobile)
#         wd.find_element_by_name("work").click()
#         wd.find_element_by_name("work").clear()
#         wd.find_element_by_name("work").send_keys(contact.work)
#         wd.find_element_by_name("fax").click()
#         wd.find_element_by_name("fax").clear()
#         wd.find_element_by_name("fax").send_keys(contact.fax)
#         wd.find_element_by_name("email").click()
#         wd.find_element_by_name("email").clear()
#         wd.find_element_by_name("email").send_keys(contact.email)
#         wd.find_element_by_name("email2").click()
#         wd.find_element_by_name("email2").clear()
#         wd.find_element_by_name("email2").send_keys(contact.email2)
#         wd.find_element_by_name("email3").click()
#         wd.find_element_by_name("email3").clear()
#         wd.find_element_by_name("email3").send_keys(contact.email3)
#         wd.find_element_by_name("homepage").click()
#         wd.find_element_by_name("homepage").clear()
#         wd.find_element_by_name("homepage").send_keys(contact.homepage)
#
#         wd.find_element_by_name("bday").click()
#         Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
#         wd.find_element_by_name("bday").click()
#
#         wd.find_element_by_name("bmonth").click()
#         Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
#         wd.find_element_by_name("bmonth").click()
#
#         wd.find_element_by_name("byear").click()
#         wd.find_element_by_name("byear").clear()
#         wd.find_element_by_name("byear").send_keys(contact.byear)
#
#         wd.find_element_by_name("aday").click()
#         Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
#         wd.find_element_by_name("aday").click()
#
#         wd.find_element_by_name("amonth").click()
#         Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
#         wd.find_element_by_name("amonth").click()
#
#         wd.find_element_by_name("ayear").click()
#         wd.find_element_by_name("ayear").clear()
#         wd.find_element_by_name("ayear").send_keys(contact.ayear)
#
#         wd.find_element_by_name("address2").click()
#         wd.find_element_by_name("address2").clear()
#         wd.find_element_by_name("address2").send_keys(contact.address2)
#
#         wd.find_element_by_name("phone2").click()
#         wd.find_element_by_name("phone2").clear()
#         wd.find_element_by_name("phone2").send_keys(contact.phone2)
#
#         wd.find_element_by_name("notes").click()
#         wd.find_element_by_name("notes").clear()
#         wd.find_element_by_name("notes").send_keys(contact.note)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

        self.change_field_value_date("bday", contact.bday)
        self.change_field_value_date("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

        self.change_field_value_date("aday", contact.aday)
        self.change_field_value_date("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.note)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.select_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_first_contact(self):
        self.select_contact_by_index(0)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_date(self, field_date, text):
        wd = self.app.wd
        if text is not None:
            selector = Select(wd.find_element_by_name(field_date))
            selector.select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                all_address = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones=all_phones, all_emails=all_emails, all_address=all_address))
        return list(self.contact_cache)

    # открывает форму редактирование index контакта
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    # открывает страницу просмотра деталей определенного index контакта
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)

        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")

        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile,
                       work=work, phone2=phone2,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, home=home, mobile=mobile, work=work,  phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)