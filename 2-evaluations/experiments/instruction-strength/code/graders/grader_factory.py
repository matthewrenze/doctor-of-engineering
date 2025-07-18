from graders.case.all_upper_case_grader import AllUpperCaseGrader
from graders.case.all_lower_case_grader import AllLowerCaseGrader
from graders.exclude.exclude_commas_grader import ExcludeCommasGrader
from graders.exclude.exclude_periods_grader import ExcludePeriodsGrader
from graders.exclude.exclude_spaces_grader import ExcludeSpacesGrader
from graders.exclude.exclude_word_and_grader import ExcludeWordAndGrader
from graders.exclude.exclude_word_the_grader import ExcludeWordTheGrader
from graders.exclude.exclude_letter_e_grader import ExcludeLetterEGrader
from graders.include.include_word_platypus import IncludeWordPlatypusGrader
from graders.include.include_word_bamboozle import IncludeWordBamboozleGrader
from graders.include.include_word_effervescent import IncludeWordEffervescentGrader
from graders.length.less_than_100_words_grader import LessThan100WordsGrader
from graders.length.more_than_100_words import MoreThan100Words
from graders.length.exactly_100_words import Exactly100WordsGrader
from graders.length.exactly_3_paragraphs import Exactly3ParagraphsGrader
from graders.position.prefix_start_grader import PrefixStartGrader
from graders.position.postfix_stop_grader import PostfixStopGrader
from graders.format.format_is_json_grader import FormatIsJsonGrader
from graders.format.format_is_html import FormatIsHtmlGrader

class GraderFactory:
    def __init__(self):
        self.grader_map = {
            "all-upper-case": AllUpperCaseGrader(),
            "all-lower-case": AllLowerCaseGrader(),
            "exclude-commas": ExcludeCommasGrader(),
            "exclude-periods": ExcludePeriodsGrader(),
            "exclude-spaces": ExcludeSpacesGrader(),
            "exclude-letter-e": ExcludeLetterEGrader(),
            "exclude-word-the": ExcludeWordTheGrader(),
            "exclude-word-and": ExcludeWordAndGrader(),
            "include-word-platypus": IncludeWordPlatypusGrader(),
            "include-word-bamboozle": IncludeWordBamboozleGrader(),
            "include-word-effervescent": IncludeWordEffervescentGrader(),
            "less-than-100-words": LessThan100WordsGrader(),
            "more-than-100-words": MoreThan100Words(),
            "exactly-100-words": Exactly100WordsGrader(),
            "exactly-3-paragraphs": Exactly3ParagraphsGrader(),
            "prefix-answer": PrefixStartGrader(),
            "postfix-stop": PostfixStopGrader(),
            "format-is-json": FormatIsJsonGrader(),
            "format-is-html": FormatIsHtmlGrader(),
        }

    def create(self, instruction_id: str):
        if instruction_id not in self.grader_map:
            raise ValueError(f"Unknown instruction_id: {instruction_id}")

        return self.grader_map[instruction_id]