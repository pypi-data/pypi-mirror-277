"""

"""


class InterviewRoundRepository:

    def __init__(self, data_storage):

        self.__data_storage = data_storage

    def get_rounds_for_interview(self, _id):

        return self.__data_storage.get_rounds_for_interview(_id)

    def get_round_by_id(self, _id):

        return self.__data_storage.get_round_by_id(_id)

    def add_round(self, interview_round):

        self.__data_storage.add_round(interview_round)

    def remove_round(self, _id):

        self.__data_storage.remove(_id)

    def update_round(self, interviewround):

        self.__data_storage.update_round(interviewround)
