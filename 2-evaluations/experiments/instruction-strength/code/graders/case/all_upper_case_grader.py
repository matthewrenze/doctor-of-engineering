from graders.grader import Grader

class AllUpperCaseGrader(Grader):

    def grade(self, answer: str) -> bool:
        return answer.isupper()