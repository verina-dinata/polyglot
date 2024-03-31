# enable import from parent directory
import sys
sys.path.append('../app')

# Create approach without repository
# from database_manager import DatabaseManager
# from models import Word, Language

# dbm = DatabaseManager()

# session = dbm.get_session()

# new_word = Word(word='叫', language=Language.CN.value, pronounciation='jiào', type='Verb', english_definition='to be called')

# session.add(new_word)

# session.commit()

# Create with repository
from repositories.word_repository import WordRepository
from database.database_manager import DatabaseManager
from models.word import Word, Language

dbm = DatabaseManager()
session = dbm.get_session()

word_repo = WordRepository(session)
new_word = word_repo.create(
  {
    "language": "chinese",
    "word": "hello",
    "pronounciation": "hello",
    "type": "noun",
    "english_definition": "hello",
  }
)

# Get all data from repository
word_repo.get_all()
# word_repo.get_all()

# Homework 1 -> Refactor this into
word_repo.get_all()

# Homework 1 -> Give me example find by id
