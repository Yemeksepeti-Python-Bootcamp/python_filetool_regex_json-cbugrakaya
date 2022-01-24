import json
from msilib.schema import Error
import pathlib
import re
from sqlite3 import DatabaseError
from tools.database_tool import DatabaseTool
from datetime import datetime
import texts.error_texts  as err_txt

class JsonTool():
    
    def __init__(self,file_path,db_path):
        self.file_path = file_path
        self.db_path = db_path

    
    def open_json(self,file_path):
        """ read json file 
        :param file_path: path of json file
        :return data: json's file content as a list
        """
        extension =  pathlib.Path(file_path).suffix 
        if extension == ".json" or extension == ".JSON":
            try:
                with open(file_path,"r") as file:
                    data = json.load(file)
                return data
            except Error as e:
                print(e)
        else:
            raise Exception(err_txt.ERR_FILE_TYPE)

    
    def append_json(self):
        """
        insert json data to database
        """
        # create database connection
        db_conn = DatabaseTool.create_connection(self.db_path)
        
        # open json file and read file
        data = self.open_json(self.file_path)

        try:
            # table name
            table_name = "data_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))

            if db_conn is not None:
                # create table
                DatabaseTool.create_table(db_conn,table_name)
            
                for i in data:
                    # email, username, isimsoyisim, doğumtarihi, address
                    values = [i["email"],i["username"],i["profile"]["name"],i["profile"]["dob"],i["profile"]["address"]]
                    
                    if all(v is not None for v in values):
                        email, username, isimsoyisim = i["email"], i["username"], i["profile"]["name"]
                        emailuserlk = 1 if re.search(username[0:3]+'\w+',email)  else 0
                        usernamelk =  1 if re.search(isimsoyisim[0:3].lower()+'\w+',username) else 0
                        dogumyil, dogumay, dogumgun = re.search("(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[01])",i["profile"]["dob"]).groups() 
                        ulke = list(map(str.strip, i["profile"]["address"].split(",")))[-1]
                        ap = 1 if i["apiKey"] else 0

                        # insert data to table
                        DatabaseTool.insert_data(db_conn,table_name,email,username,isimsoyisim,emailuserlk,usernamelk,dogumyil,dogumay,dogumgun,ulke,ap)
                    else:
                        continue
        
            else:
                raise DatabaseError
        except:
            db_conn.rollback()
            print(err_txt.ERR_DB_CONN)

        finally:
            db_conn.close()


