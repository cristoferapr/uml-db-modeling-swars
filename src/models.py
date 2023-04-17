import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(80), unique=False, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(Integer)
    gender = Column(String(16))
    homeworld_planet_id = Column(Integer, ForeignKey('planets.id'))
    homeworld_planet = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    cargo_capacity = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    vehicle_class = Column(String(20))
    manufacturer = Column(String(20))
    max_atmosphering_speed = Column(Integer)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

    def to_dict(self):
        return {}

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram4.png')
