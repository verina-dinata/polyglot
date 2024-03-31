from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database_manager import Base

class Sentence(Base):
  __tablename__ = 'sentences'

  id = Column(Integer, primary_key=True)
  word_id = Column(Integer, ForeignKey('words.id'))
  sentence_string = Column(String, nullable=False)
  pronounciation = Column(String, nullable=False)
  english_translation = Column(String, nullable=False)

  word = relationship("Word", back_populates="sentences")

  def __repr__(self):
    """
    Returns a string representation of the Sentence model instance.
    """
    return f"Sentence(id={self.id}, word_id={self.word_id}, sentence_string='{self.sentence_string}', pronounciation='{self.pronounciation}', english_translation='{self.english_translation}')"

  def json(self):
    return {
      "id": self.id,
      "sentence_string": self.sentence_string,
      "pronounciation": self.pronounciation,
      "english_translation": self.english_translation
    }
