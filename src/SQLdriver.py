from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DIALCT = "mysql"
DRIVER = "mysqlconnector"
USERNAME = "root"
PASSWORD = ""
HOST = "120.24.56.100"
PORT = "3306"
DATABASE = "lianjia"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Arctire(Base):
    __tablename__ = "arctire"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", backref="arctires")


class Proxy(Base):
    __tablename__ = "proxy"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20))
    port = Column(Integer)
    service = Column(String(50))
    verify = Column

