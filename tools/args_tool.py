import sys
from os import path
import texts.error_texts  as err_txt

def get_args(argv):
   """ get arguments on command line
   :param argv: arguments list
   :return: file path and database path
   """
   
   if len(argv) == 4 and argv[0] == "--file" and argv[2] == "--db":
         if path.exists(argv[1]) and path.exists(argv[3]):
               return argv[1],argv[3]
         else:
               print(err_txt.ERR_CMD)
               sys.exit(2)
   else:
        print(err_txt.ERR_CMD)
        sys.exit(2)
