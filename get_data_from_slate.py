import requests as r
from configparser import ConfigParser
from utils import *

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the data from config
userinfo = config_object["USERINFO"]
urls = config_object["URLS"]
ID = userinfo["id"]
PASSWORD = userinfo["password"]
LOGIN_MESSAGE = userinfo["login_submit_message"]
LOGIN_URL = urls["login"]
FILE_ACCESS_URL = urls["file_access"]

def get_file_message():
    s = r.Session()

    payload = {
        'eid': ID,
        'pw' : PASSWORD,
        'submit': LOGIN_MESSAGE
    }
    with r.Session() as s:
        p = s.post(LOGIN_URL, data=payload)
        page = s.get(FILE_ACCESS_URL)

    file_message = page.content

    my_file = open("message.txt","w")
    my_file.write(file_message.decode("utf-8"))
    my_file.close()

    # file_message = page.content.decode("utf-8")
    return file_message

if __name__ == '__main__':
    print("=======================================")
    print(" Fetching Message from Slate")
    print("=======================================")
    start = start_time()
    file_message = get_file_message()
    end = end_time()
    hours,minutes,seconds = format_time(start,end)
    print("=======================================")
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

