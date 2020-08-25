from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self):
        wd = self.wd
        self.return_to_home_page()
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
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

        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("qwertrvf")

        wd.find_element_by_name("address2").send_keys(contact.address2)

        wd.find_element_by_name("phone2").send_keys(contact.phone2)

        wd.find_element_by_name("notes").send_keys(contact.note)
        # submit add new
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_addnew_page(self):
        wd = self.wd
        self.open_addnew_page()
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
