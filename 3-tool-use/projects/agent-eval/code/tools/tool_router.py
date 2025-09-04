from tools.calculator_tool import CalculatorTool
from tools.list_files_tool import ListFilesTool
from tools.read_file_tool import ReadFileTool
from tools.search_web_tool import SearchWebTool


class ToolRouter(object):
    def route(self, action_name, action_args, workspace):

        if action_name == "calculate":
            tool = CalculatorTool()
            return tool.execute(action_args)

        elif action_name == "list_files":
            tool = ListFilesTool(workspace.folder_path)
            return tool.execute()

        elif action_name == "read_file":
            tool = ReadFileTool(workspace.folder_path)
            return tool.execute(action_args)

        elif action_name == "search_web":
            tool = SearchWebTool()
            return tool.execute(action_args)

        # elif action_name == "read_file_as_image":
        #     tool = ReadFileAsImageTool(workspace.folder_path)
        #     return tool.execute(action_args)

        else:
            return f"Unknown action: {action_name}."