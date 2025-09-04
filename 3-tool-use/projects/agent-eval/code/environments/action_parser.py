class ActionParser:
    def parse(self, action):
        action_parts = action.split('(', 1)
        action_name = action_parts[0].strip()
        action_args = action_parts[1] if len(action_parts) > 1 else ""
        action_args = action_args.rstrip(')')
        action_args = action_args.strip("\"")
        return action_name, action_args