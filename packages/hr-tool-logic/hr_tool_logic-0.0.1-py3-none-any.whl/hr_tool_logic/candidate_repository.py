"""

"""


class CandidateRepository:

    def __init__(self, data_storage):
        self.__data_storage = data_storage

    def get_candidate_by_id(self, _id):
        return self.__data_storage.get_candidate_by_id(_id)

    def get_all_candidates(self):
        return self.__data_storage.get_all_candidates()

    def add_candidate(self, candidate):
        self.__data_storage.add_candidate(candidate)

    def update_candidate(self, candidate):
        self.__data_storage.update_candidate(candidate)

    def remove_candidate(self, _id):
        self.__data_storage.remove_candidate(_id)
