from asyncore import read
import email
import json
import pathlib
import re
from DatabaseTool import DatabaseTool
from datetime import datetime

class JsonTool():
    

    def read_json(self,file_path,db_path):
        """
        """
         
        # check extension
        extension =  pathlib.Path(file_path).suffix 
        if extension == ".json" or extension == ".JSON":

            with open(file_path,"r") as file:
                data = json.load(file)
            
                # create connection
                db_conn = DatabaseTool.create_connection(db_path)
                
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
                                
                                emailuserlk = 1 if re.search(username[0:3]+'\w+',email) != None else 0
                                usernamelk =  1 if re.search(isimsoyisim[0:3].lower()+'\w+',username) != None else 0
                                # to get full birth date (1993-03-19)
                                doğumtarihi = re.search("(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[01])",i["profile"]["dob"])
                                dogumyil, dogumay, dogumgun = doğumtarihi.groups()
                                ulke =  i["profile"]["address"].split(", ")[-1]
                                ap = 1
                                # insert data to table
                                DatabaseTool.insert_data(db_conn,table_name,email,username,isimsoyisim,emailuserlk,usernamelk,dogumyil,dogumay,dogumgun,ulke,ap)
                            else:
                                continue
                
                    else:
                        pass
                except:
                    db_conn.close()
                    raise Exception("Error! cannot create the database connection.")

                finally:
                    db_conn.close()

        else:
            raise Exception("This file is not a json file.")
   
 
        
    