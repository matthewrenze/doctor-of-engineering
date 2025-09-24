from tools.calculate_tool import CalculateTool
from tools.list_files_tool import ListFilesTool
from tools.read_file_tool import ReadFileTool
from tools.read_html_tool import ReadHtmlTool
from tools.search_web_tool import SearchWebTool
from tools.execute_code_tool import ExecuteCodeTool

class ToolRouter(object):
    def route(self, action_name, action_args, workspace):

        # Pad args so we always have at least 3
        while len(action_args) < 3:
            action_args.append(None)

        if action_name == "calculate":
            tool = CalculateTool()
            expression = action_args[0]
            return tool.execute(expression)

        elif action_name == "list_files":
            tool = ListFilesTool(workspace.folder_path)
            return tool.execute()

        elif action_name == "read_file":
            tool = ReadFileTool(workspace.folder_path)
            file_name = action_args[0]
            return tool.execute(file_name)

        elif action_name == "search_web":
            tool = SearchWebTool()
            query = action_args[0]
            return tool.execute(query)

        elif action_name == "read_html":
            tool = ReadHtmlTool()
            url = action_args[0]
            chunk = int(action_args[1]) if action_args[1] is not None else 1
            return tool.execute(url, chunk)

        elif action_name == "execute_code":
            tool = ExecuteCodeTool()
            code = action_args[0]
            return tool.execute(code)

        else:
            return f"Unknown action: {action_name}."