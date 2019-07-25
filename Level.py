import json

with open('G:\\Git\\Repositories\\Python\\New_snake\\config.json') as config_file:
    data = json.load(config_file)

class level:
    def __init__(self):
        self.x = data['gameX']
        self.y = data['gameY']
        self.FPS = data['FPS']
        self.movetimer = data['movetimer']
        self.startLength = data['startLength']



