class InstructionFactory:
    def create(self, instruction_id: str) -> str:
        if instruction_id == "all-upper-case":
            return "Respond in all capital letters."
        elif instruction_id == "all-lower-case":
            return "Respond in all lowercase letters."

        elif instruction_id == "exclude-commas":
            return "Respond without using any commas."
        elif instruction_id == "exclude-periods":
            return "Respond without using any periods."
        elif instruction_id == "exclude-spaces":
            return "Respond without using any spaces."
        elif instruction_id == "exclude-letter-e":
            return "Respond without using the letter 'e'."
        elif instruction_id == "exclude-word-the":
            return "Respond without using the word 'the'."
        elif instruction_id == "exclude-word-and":
            return "Respond without using the word 'and'."

        elif instruction_id == "include-word-platypus":
            return "Include the word 'platypus' in your response."
        elif instruction_id == "include-word-bamboozle":
            return "Include the word 'bamboozle' in your response."
        elif instruction_id == "include-word-effervescent":
            return "Include the word 'effervescent' in your response."

        elif instruction_id == "less-than-100-words":
            return "Respond in less than 100 words."
        elif instruction_id == "more-than-100-words":
            return "Respond in more than 100 words."
        elif instruction_id == "exactly-100-words":
            return "Respond in exactly 100 words."
        elif instruction_id == "exactly-3-paragraphs":
            return "Respond in exactly 3 paragraphs."

        elif instruction_id == "prefix-start":
            return "Start your response with [Start]."
        elif instruction_id == "postfix-stop":
            return "End your response with [Stop]."

        elif instruction_id == "format-is-json":
            return "Respond in valid JSON format."
        elif instruction_id == "format-is-html":
            return "Respond in valid HTML format."

        else:
            raise ValueError(f"Unknown instruction_id: {instruction_id}")