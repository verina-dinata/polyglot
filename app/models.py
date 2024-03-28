from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from database_manager import Base


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
    return f"Word(id={self.id}, language='{self.language}', word string='{self.word_string}', pronounciation='{self.pronounciation}', type='{self.type}', english_definition='{self.english_definition}')"


class Sentence(Base):
  __tablename__ = 'sentences'

  id = Column(Integer, primary_key=True)
  word_id = Column(Integer, ForeignKey('words.id'))
  sentence = Column(String, nullable=False)
  pronounciation = Column(String, nullable=False)
  english_definition = Column(String, nullable=False)

  word = relationship("Word", back_populates="sentences")

  def __repr__(self):
    """
    Returns a string representation of the Sentence model instance.
    """
    return f"Sentence(id={self.id}, word_id={self.word_id}, sentence='{self.sentence}', pronounciation='{self.pronounciation}', english_definition='{self.english_definition}')"
