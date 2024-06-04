"""
This module defines a class for a candidate
"""
from re import match
import datetime as dt

from bson import ObjectId


class Candidate:

    def __init__(self, name: str, role: str = "", yoe: int = 0, email: str = "", phone_number: str = "",
                 linkedin: str = "", birthdate: dt.date = dt.date.today(), is_blacklisted: bool = False,
                 notes: str = ""):

        self.___id = ObjectId()

        self.__name = name

        self.__role = role

        if 0 <= yoe <= 50:
            self.__yoe = yoe

        if match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip(), 0):
            self.__email = email

        if match(r'\+?\d+', phone_number, flags=0):
            self.__phone_number = phone_number

        self.__linkedin = linkedin

        self.__birthdate = birthdate

        self.__is_blacklisted = is_blacklisted

        self.__notes = notes

    @property
    def _id(self):
        return self.___id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def yoe(self):
        return self.__yoe

    @yoe.setter
    def yoe(self, yoe):
        if 0 <= yoe <= 50:
            self.__yoe = yoe

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip(), 0):
            self.__email = email

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if match(r'\+?\d+', phone_number, flags=0):
            self.__phone_number = phone_number

    @property
    def linkedin(self):
        return self.__linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        self.__linkedin = linkedin

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self.__birthdate = birthdate

    @property
    def is_blacklisted(self):
        return self.__is_blacklisted

    @is_blacklisted.setter
    def is_blacklisted(self, is_blacklisted):
        self.__is_blacklisted = is_blacklisted

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes
