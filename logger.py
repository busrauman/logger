import sys
import os
import json
import time
import datetime
from os.path import abspath, dirname, join

cur_path =os.path.dirname(str(sys.argv[0]))
log_file =cur_path + 'happyLogger.json'
#print log_file
log_json=dict()
log_json["Data"]={}

i=0
while True:
        i +=1
        print(i)
        log_json["Data"]["Count"]=i
        log_json['Created']=datetime.datetime.utcnow().isoformat()

        with open(log_file, "a") as f:
                json.dump(log_json,f)#, ensure_ascii=False)
                f.write("\n")
        time.sleep(3)

