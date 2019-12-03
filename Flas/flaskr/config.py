import os

class Config:
	SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/jpk'
#	engine = create_engine("mysql://prokash:q1234q123@localhost/myapp")

	SECRET_KEY = 'any secret string'
