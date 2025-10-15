from tools.list_files_tool import ListFilesTool
from tools.read_file_tool import ReadFileTool
from tools.find_in_file_tool import FindInFileTool
from tools.search_web_tool import SearchWebTool
from tools.read_html_tool import ReadHtmlTool
from tools.find_in_html_tool import FindInHtmlTool
from tools.download_file_tool import DownloadFileTool
from tools.calculate_tool import CalculateTool
from tools.execute_code_tool import ExecuteCodeTool

class ToolRouter(object):
    def route(self, action_name, action_args, workspace):

        if action_name == "list_files":
            tool = ListFilesTool(workspace.folder_path)
            return tool.execute()

        elif action_name == "read_file":
            tool = ReadFileTool(workspace.folder_path)
            file_name = action_args.get("file_name")
            chunk_index = int(action_args.get("chunk_index", 1))
            return tool.execute(file_name, chunk_index)

        elif action_name == "find_in_file":
            tool = FindInFileTool(workspace.folder_path)
            file_name = action_args.get("file_name")
            text = action_args.get("text")
            match_index = int(action_args.get("match_index", 1))
            return tool.execute(file_name, text, match_index)

        elif action_name == "search_web":
            tool = SearchWebTool()
            query = action_args.get("query")
            return tool.execute(query)

        elif action_name == "read_html":
            tool = ReadHtmlTool()
            url = action_args.get("url")
            chunk_index = int(action_args.get("chunk_index", 1))
            return tool.execute(url, chunk_index)

        elif action_name == "find_in_html":
            tool = FindInHtmlTool()
            url = action_args.get("url")
            text = action_args.get("text")
            match_index = int(action_args.get("match_index", 1))
            return tool.execute(url, text, match_index)

        elif action_name == "download_file":
            tool = DownloadFileTool(workspace.folder_path)
            url = action_args.get("url")
            return tool.execute(url)

        elif action_name == "calculate":
            tool = CalculateTool()
            expression = action_args.get("expression")
            return tool.execute(expression)

        elif action_name == "execute_code":
            tool = ExecuteCodeTool(workspace.folder_path)
            code = action_args.get("code")
            return tool.execute(code)

        else:
            return f"Unknown action: {action_name}."