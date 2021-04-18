import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Define association tables to create a many to many for the favorites
favorites_people = Table('user_people', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('person_id', Integer, ForeignKey('people.id'))
)
favorites_planets = Table('user_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planets_id', Integer, ForeignKey('planets.id'))
)
favorites_starships = Table('user_starships', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('starships_id', Integer, ForeignKey('starships.id'))
)

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    # Relationship is made for each type of favorite separately
    people = relationship("Person", secondary=favorites_people)
    planets = relationship("Planets", secondary=favorites_planets)
    starships = relationship("Starships", secondary=favorites_starships)
                               

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the People   
    id = Column(Integer, primary_key=True)
    # one to one with planet for homeworld
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship("Planets", back_populates="people")
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    name = Column(String(50), nullable=False)
    photo_url: Column(String)      

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the Planets   
    id = Column(Integer, primary_key=True)
    # relationship for the homeworld for people
    people = relationship("Person", uselist=False)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name = Column(String(50), nullable=False)
    photo_url: Column(String)
 
class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the Starships   
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    name = Column(String(50), nullable=False)
    photo_url: Column(String)  

    def to_dict(self):
        return {}

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')