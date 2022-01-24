from tools.json_tool import JsonTool
import sys
from os import path
from tools.args_tool import get_args



if __name__ == "__main__":
    file_path,db_path = get_args(sys.argv[1:])

    object1 = JsonTool(file_path,db_path)
    object1.append_json()
