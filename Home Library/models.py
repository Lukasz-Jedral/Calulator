import json


class HomeLibrary:
    '''
    Home Library data base
    '''
    def __init__(self):
        try:
            with open("static/homelibrary.json", "r") as f:
                self.homelibrary = json.load(f)
        except FileNotFoundError:
            self.homelibrary = []

    def all(self):
        return self.homelibrary

    def get(self, id):
        return self.homelibrary[id]

    def create(self, data):
        data.pop('csrf_token')
        self.homelibrary.append(data)

    def save_all(self):
        with open("static/homelibrary.json", "w") as f:
            json.dump(self.homelibrary, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.homelibrary[id] = data
        self.save_all()


homelibrary = HomeLibrary()