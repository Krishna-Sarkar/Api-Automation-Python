import configparser
import os
import json



def read_config():
    config = configparser.ConfigParser()
    config.read(os.getcwd()+'/'+'config.ini')
    return config

def read_json(file_name:str):
    with open(os.getcwd()+'/testdata/'+file_name, 'r') as json_file:
        data = json.load(json_file)
        return data