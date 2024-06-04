"""

"""


class InterviewerRepository:

    def __init__(self, data_storage):
        self.__data_storage = data_storage

    def get_interviewer(self, _id):
        return self.__data_storage.get_interviewer(_id)

    def get_interviewers_for_round(self, round_id):
        return self.__data_storage.get_interviewers_for_round(round_id)

    def get_all_interviewers(self):
        return self.__data_storage.get_all_interviewers()

    def add_interviewer(self, interviewer):
        self.__data_storage.add_interviewer(interviewer)

    def remove_interviewer(self, _id):
        self.__data_storage.remove(_id)

    def update_interviewer(self, interviewer):
        self.__data_storage.update(interviewer)
