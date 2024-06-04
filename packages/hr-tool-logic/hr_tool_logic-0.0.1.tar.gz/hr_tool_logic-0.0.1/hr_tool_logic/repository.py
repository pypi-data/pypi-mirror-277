"""
This module defines a class for a repository
"""
from candidate_repository import CandidateRepository
from interview_repository import InterviewRepository
from interviewround_repository import InterviewRoundRepository
from interviewer_repository import InterviewerRepository


class Repository:

    def __init__(self, data_storage):
        self.__data_storage = data_storage

        self.candidate_rep = CandidateRepository(self.__data_storage)

        self.interview_repository = InterviewRepository(self.__data_storage)

        self.interviewround_repository = InterviewRoundRepository(self.__data_storage)

        self.interviewer_repository = InterviewerRepository(self.__data_storage)
