import json
from graders.grader import Grader

class FormatIsJsonGrader(Grader):
    def grade(self, response: str) -> bool:
        try:
            json.loads(response)
            return True
        except json.JSONDecodeError:
            return False

# DEBUG
grader = FormatIsJsonGrader()
assert grader.grade('{"key": "value"}')
assert not grader.grade('"key": "value"')