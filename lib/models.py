from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, Boolean
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DB setup
engine = create_engine('sqlite:///theater_work.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base
Base = declarative_base()

# Models
class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    auditions = relationship("Audition", back_populates="role")

    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]

    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired = [aud for aud in self.auditions if aud.hired]
        return hired[0] if hired else "no actor has been hired for this role"

    def understudy(self):
        hired = [aud for aud in self.auditions if aud.hired]
        return hired[1] if len(hired) > 1 else "no actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)

    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", back_populates="auditions")

    def call_back(self):
        self.hired = True
        session.add(self)
        session.commit()