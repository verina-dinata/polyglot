from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum
from database.database_manager import Base


class Language(Enum):
  EN = 'english',
  CN = 'chinese'

class Word(Base):
  __tablename__ = 'words'

  id = Column(Integer, primary_key=True)
  language = Column(String, nullable=False)
  word_string = Column(String, unique=False, nullable=False)
  pronounciation = Column(String, nullable=False)
  type = Column(String, nullable=False)
  english_definition = Column(String, nullable=False)

  sentences = relationship("Sentence", back_populates="word")

  def __repr__(self):
    """
    Returns a string representation of the Word model instance.
    """
    return f"Word(id={self.id}, language='{self.language}', word_string='{self.word_string}', pronounciation='{self.pronounciation}', type='{self.type}', english_definition='{self.english_definition}')"
