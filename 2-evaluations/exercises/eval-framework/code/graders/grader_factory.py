from graders.grader_agent import GraderAgent

class GraderFactory:
    def create(self):
        return GraderAgent()