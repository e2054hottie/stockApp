import json

class Config:
    with open('./databaseMappingFlamework/config.json', 'r') as file:
        data = json.load(file)
    
    def getConfig():
        return Config.data