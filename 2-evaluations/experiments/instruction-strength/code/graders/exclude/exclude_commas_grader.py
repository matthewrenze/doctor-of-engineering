from graders.grader import Grader

class ExcludeCommasGrader(Grader):

    def grade(self, answer: str) -> bool:
        return ',' not in answer