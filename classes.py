from pydantic import BaseModel

class PersonFromUser(BaseModel):
    person: str
    role: str
    queryType: str

class KeyWordsFromUser(BaseModel):
    keywords: list

class NameFromUser(BaseModel):
    name: str
    queryType: str

class FlagFromUser(BaseModel):
    flag: bool

class IdFromUser(BaseModel):
    movieId: str