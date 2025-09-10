from tools.calculator_tool import CalculatorTool
from tools.list_files_tool import ListFilesTool
from tools.read_file_tool import ReadFileTool
from tools.read_html_tool import ReadHtmlTool
from tools.search_web_tool import SearchWebTool


class ToolRouter(object):
    def route(self, action_name, action_args, workspace):

        # Pad args so we always have at least 3
        while len(action_args) < 3:
            action_args.append(None)

        if action_name == "calculate":
            tool = CalculatorTool()
            return tool.execute(action_args[0])

        elif action_name == "list_files":
            tool = ListFilesTool(workspace.folder_path)
            return tool.execute()

        elif action_name == "read_file":
            tool = ReadFileTool(workspace.folder_path)
            return tool.execute(action_args[0])

        elif action_name == "search_web":
            tool = SearchWebTool()
            return tool.execute(action_args[0])

        elif action_name == "read_html":
            tool = ReadHtmlTool()
            url = action_args[0]
            chunk = int(action_args[1]) if action_args[1] is not None else 1
            return tool.execute(url, chunk)

        else:
            return f"Unknown action: {action_name}."