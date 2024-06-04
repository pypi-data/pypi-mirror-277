"""
This module defines an interviewer class
"""
from re import match

from bson import ObjectId


class Interviewer:

    def __init__(self, name, title="", email=""):

        self.__interviewround_ids = []

        self.___id = ObjectId()

        self.__name = name

        self.__title = title

        if match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip(), 0):
            self.__email = email

    def add_round(self, round_id):
        self.__interviewround_ids.append(round_id)

    def remove_round(self, round_id):
        self.__interviewround_ids.remove(round_id)

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
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip(), 0):
            self.__email = email

    @property
    def interviewround_ids(self):
        return self.__interviewround_ids
