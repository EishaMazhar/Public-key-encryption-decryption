from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["USERINFO"] = {
    "id": "k173730",
    "password": "slate1234",
    "login_submit_message": "Log In"
}

config_object["SERVERCONFIG"] = {
    "host": "http://203.124.42.218",
    "port": "8080"
}

service_config = config_object["SERVERCONFIG"]
filename = 'ISS_message.txt'

config_object["URLS"] = {
    "login": f'{service_config["host"]}:{service_config["port"]}/portal/xlogin',
    "file_access": f'{service_config["host"]}:{service_config["port"]}/access/content/user/{config_object["USERINFO"]["id"]}/{filename}'
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)


#Reference
#https://tutswiki.com/read-write-config-files-in-python/