import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets
    # Notice that each column is also a normal Python instance attribute.
    id_Planets = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter  = Column(Integer, nullable=False)
    rotation_period   = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id_People = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table starships
    # Notice that each column is also a normal Python instance attribute.
    id_Starships = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table favorite
    # Notice that each column is also a normal Python instance attribute.
    id_Favorite = Column(Integer, primary_key=True)
    id_Starships = Column(Integer, ForeignKey('starships.id_Starships'))
    id_People = Column(Integer, ForeignKey('people.id_People'))
    id_Planets = Column(Integer, ForeignKey('planets.id_Planets'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')