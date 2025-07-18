from graders.grader import Grader

class PostfixStopGrader(Grader):
    def grade(self, answer: str) -> bool:
        return answer.strip().endswith("[Stop]")