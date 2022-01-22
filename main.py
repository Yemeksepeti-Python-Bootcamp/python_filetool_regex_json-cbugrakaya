from jsontool import JsonTool
import sys
from os import path

def get_args(argv):
   
   try:
      if len(argv) == 4:
         if argv[0] == "--file" and argv[2] == "--db":
               if path.exists(argv[1]) and path.exists(argv[3]):
                    return argv[1],argv[3]
               else:
                    print("Path files is not exists.")
         else:
            print('Usage: test.py --file <filepath> --db <dbpath>')
            sys.exit(2)
      else:
         print('Usage: test.py --file <filepath> --db <dbpath>')
         sys.exit(3)
   except:
      sys.exit(5)


if __name__ == "__main__":
    file_path,db_path = get_args(sys.argv[1:])

    deneme = JsonTool()
    deneme.read_json(file_path,db_path)
