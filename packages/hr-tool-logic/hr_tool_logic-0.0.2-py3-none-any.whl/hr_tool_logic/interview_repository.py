"""

"""


class InterviewRepository:

    def __init__(self, data_storage):
        self.__data_storage = data_storage

    def get_interviews_for_candidate(self, cand_id):
        return self.__data_storage.get_interviews_for_candidate(cand_id)

    def get_interview_by_id(self, _id):
        return self.__data_storage.get_interview_by_id(_id)

    def add_interview(self, interview):
        self.__data_storage.add_interview(interview)

    def remove_interview(self, _id):
        self.__data_storage.remove_interview(_id)

    def update_interview(self, _id, **fields):
        self.__data_storage.update_interview(_id, fields)

    def get_mark(self, _id):
        self.__data_storage.get_mark(_id)
