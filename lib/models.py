from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base 
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Integer(), default=False)
    role_id = Column(Integer(), ForeignKey('roles.id'))
    
    # Audition.role returns an instance of role associated with this audition.
    role = relationship('Role', back_populates='auditions')

    # Audition.call_back() will change the the hired attribute to True.
    def call_back(self):
        self.hired = True
    
class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    # Role.auditions returns all of the auditions associated with this role.
    auditions = relationship('Audition', back_populates='role')
    
    # Role.actors returns a list of names from the actors associated with this role.
    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    # Role.locations returns a list of locations from the auditions associated with this role.
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    # Role.lead() returns the first instance of the audition that was hired for this role or returns
    # a string 'no actor has been hired for this role'.
    def lead(self):
        got_hired = [audition for audition in self.auditions if audition.hired]
        return got_hired[1] if got_hired>1 else 'no actor has been hired for this role'
    
    # Role.understudy() returns the second instance of the audition that was hired for this role 
    # or returns a string 'no actor has been hired for understudy for this role'.
    def understudy(self):
        pass

engine = create_engine('sqlite:///moringa_theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
    