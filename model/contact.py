from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, id=None,
                 email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, address2=None, phone2=None, note=None,  all_phones=None,
                 all_emails=None, all_address=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.note = note
        self.id = id
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.all_address = all_address

    # representation - стандартная функция - определяет как будет выглядеть объект при выводе на консоль
    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.lastname, self.firstname)

    # equels - функция принимающая в качестве второго параметра обьект с которым мы должны сравнить текущий обьект self
    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and
                (self.lastname == other.lastname or self.lastname == None or other.lastname == None) and
                self.firstname == None or other.firstname == None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
