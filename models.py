from mongoengine import Document, StringField, SequenceField, ListField, IntField, DictField

class User(Document):
    userID = SequenceField(primary_key=True)
    email = StringField(required=True)
    password = StringField(required=True)
    role = StringField(required=True)
    
    meta = {'collection': 'prof_mvc_users'} 


class Question(Document):
    questionId = IntField(primary_key=True)
    questionBody = StringField(required=True)
    options = ListField(StringField(), required=True)
    correctAnswer = StringField(required=True)
    
    meta = {'collection': 'Questions'} 


class Submission(Document):
    userID = StringField(required=True)
    responses = ListField(DictField(), required=True)
    sectionScores = DictField()
    totalScore = IntField()
    
    meta = {'collection': 'TestSubmissions'}

