from graders.grader import Grader

class AllLowerCaseGrader(Grader):

    def grade(self, answer: str) -> bool:
        return answer.islower()