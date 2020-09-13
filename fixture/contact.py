from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # click add new
        wd.find_element_by_link_text("add new").click()
        # fill form
        wd.find_element_by_name("firstname").send_keys(contact.firstname)

        wd.find_element_by_name("middlename").send_keys(contact.middlename)

        wd.find_element_by_name("lastname").send_keys(contact.lastname)

        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("photo").send_keys("C:\\Devel\\ca6a3d3645.jpg")

        wd.find_element_by_name("title").send_keys(contact.title)

        wd.find_element_by_name("company").send_keys(contact.company)

        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").send_keys(contact.home)

        wd.find_element_by_name("mobile").send_keys(contact.mobile)

        wd.find_element_by_name("work").send_keys(contact.work)

        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").send_keys(contact.email)

        wd.find_element_by_name("email2").send_keys(contact.email2)

        wd.find_element_by_name("email3").send_keys(contact.email3)

        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()

        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()

        wd.find_element_by_name("byear").send_keys("1999")

        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("15")
        wd.find_element_by_xpath("(//option[@value='15'])[2]").click()

        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("(//option[@value='August'])[2]").click()

        wd.find_element_by_name("ayear").send_keys("2020")

#        wd.find_element_by_name("new_group").click()
#        Select(wd.find_element_by_name("new_group")).select_by_visible_text("qwertrvf")

        wd.find_element_by_name("address2").send_keys(contact.address2)

        wd.find_element_by_name("phone2").send_keys(contact.phone2)

        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit add new
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")
                and len(wd.find_element_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home page").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\Devel\\Andru.jpg")
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
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text("5")
        # wd.find_element_by_xpath("//option[@value='5']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text("May")
        # wd.find_element_by_xpath("//option[@value='May']").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys("1989")
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text("30")
        # wd.find_element_by_xpath("(//option[@value='30'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text("September")
        # wd.find_element_by_xpath("(//option[@value='september'])").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys("2010")
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill form
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()

    def create_for_edit_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.fill_contact_form(new_contact_data)
        # submit add new
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
