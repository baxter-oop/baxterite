import os
import sys, datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config

Base = declarative_base()


class Standard(Base):
    __tablename__ = 'Standard'
    standard_id = Column(Integer, primary_key=True)
    standard_name = Column(String(), nullable=False)
    standard_desc = Column(String(), nullable=False)


class Class(Base):
    __tablename__ = 'Class'
    class_id = Column(Integer, primary_key=True)
    current_name = Column(Integer(), nullable=False)
    class_desc = Column(String(), nullable=False)


# We have to have a table to keep track of class names because people can't stop renaming classes.
class ClassName(Base):
    __tablename__ = 'ClassName'
    className_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    name = Column(String(), nullable=False)

# Couldn't come up for a bett
er name for a class session.
class Instance(Base):
    __tablename__ = 'Instance'
    instance_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    className_id = Column(Integer, nullable=False)
    block = Column(String(), nullable=False)
    start_trimester = Column(Integer, nullable=False)  # 1 for first trimester in a school year, 2 for second...
    end_trimester = Column(Integer, nullable=False)  # For most instances this will be the same as the start_trimester
    year = Column(Integer, nullable=False)  # The start of the school year (2015 for 2015-2016 school year


class InstanceMember(Base):
    __tablename__ = 'InstanceMember'
    instance_member_id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, nullable=False)  # The id of the instance
    student_id = Column(Integer, nullable=False)


class Student(Base):
    __tablename__ = 'Student'
    student_id = Column(Integer, primary_key=True)
    email = Column(String(), nullable=False, unique=True)
    name = Column(String(), nullable=True)
    avatar = Column(String())
    active = Column(Boolean, default=False)
    tokens = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())




# Create an engine that stores data in the local directory's
# database.db file.
engine = create_engine(config.path_to_database)  # In memory of Peter B.

Base.metadata.create_all(engine)