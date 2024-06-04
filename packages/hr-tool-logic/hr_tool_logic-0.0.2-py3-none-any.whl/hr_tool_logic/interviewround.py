"""
This module defines a class for an interview round.
"""
import datetime as dt

from bson import ObjectId


class InterviewRound:

    def __init__(self, interview_id: ObjectId, datetime: dt.datetime = dt.datetime.now(), round_type: str = "",
                 round_format: str = "", status="Upcoming", mark: int = -1):

        self.__interviewer_ids = []

        self.___id = ObjectId()

        self.__interview_id = interview_id

        self.__datetime = datetime

        self.__round_type = round_type

        self.__round_format = round_format

        if status.strip().lower() == 'upcoming' or status.strip().lower() == 'ended':
            self.__status = status

        self.__mark = mark

    def add_interviewer(self, interviewer_id):
        self.__interviewer_ids.append(interviewer_id)

    def remove_interviewer(self, interviewer_id):
        self.__interviewer_ids.remove(interviewer_id)

    @property
    def _id(self):
        return self.___id

    @property
    def interview_id(self):
        return self.__interview_id

    @interview_id.setter
    def interview_id(self, interview_id):
        self.__interview_id = interview_id

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, datetime):
        self.__datetime = datetime

    @property
    def round_type(self):
        return self.__round_type

    @round_type.setter
    def round_type(self, round_type):
        self.__round_type = round_type

    @property
    def round_format(self):
        return self.__round_format

    @round_format.setter
    def round_format(self, round_format):
        self.__round_format = round_format

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status.strip().lower() == 'upcoming' or status.strip().lower() == 'ended':
            self.__status = status

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def interview_ids(self):
        return self.__interviewer_ids
