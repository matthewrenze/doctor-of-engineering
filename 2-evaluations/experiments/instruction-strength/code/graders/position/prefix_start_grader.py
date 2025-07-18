from graders.grader import Grader

class PrefixStartGrader(Grader):
    def grade(self, answer: str) -> bool:
        return answer.startswith("[Start]")