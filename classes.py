from pydantic import BaseModel

class PersonFromUser(BaseModel):
    person: str
    role: str
    queryType: str

    def getJson(self):
        return {
            'person': self.person,
            'role': self.role,
            'queryType': self.queryType
        }

class KeyWordsFromUser(BaseModel):
    keywords: list
    def getJson(self):
        return {
            'keywords': self.keywords
        }

class NameFromUser(BaseModel):
    name: str
    queryType: str

    def getJson(self):
        return {
            'name': self.name,
            'queryType': self.queryType
        }

class FlagFromUser(BaseModel):
    flag: bool

    def getJson(self):
        return {
            'flag': self.flag
        }

class IdFromUser(BaseModel):
    movieId: str

    def getJson(self):
        return {
            'movieId': self.movieId
        }