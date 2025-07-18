class StrengthFactory:
    def create(self, instruction, strength_id):
        if strength_id == "baseline":
            return instruction

        elif strength_id == "markdown-bold":
            return f"**{instruction}**"

        else:
            raise ValueError(f"Unknown strength_id: {strength_id}")