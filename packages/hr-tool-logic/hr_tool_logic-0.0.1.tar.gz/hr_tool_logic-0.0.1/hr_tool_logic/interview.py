"""
This module defines a class for interview
"""
import datetime as dt

from bson import ObjectId


class Interview:

    def __init__(self, candidate_id: ObjectId, start_time: dt.date = dt.date.today(), decision: str = "In progress",
                 status: str = "Active"):

        self.___id = ObjectId()

        self.__candidate_id = candidate_id

        self.__start_time = start_time

        if (decision.lower().strip() == "in progress" or decision.lower().strip() == "hire"
                or decision.lower().strip() == "reject"):
            self.__decision = decision

        if status.lower().strip() == "active" or status.lower().strip() == "archived":
            self.__status = status

        self.__mark: int = -1

        self.__end_time: dt.date = dt.date.today() + dt.timedelta(days=14)

    @property
    def _id(self):
        return self.___id

    @property
    def candidate_id(self):
        return self.__candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        self.__candidate_id = candidate_id

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def decision(self):
        return self.__decision

    @decision.setter
    def decision(self, decision):
        if (decision.lower().strip() == "in progress" or decision.lower().strip() == "reject"
                or decision.lower().strip() == "hire"):
            self.__decision = decision

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status.lower().strip() == "active" or status.lower().strip() == "archived":
            self.__status = status

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time
