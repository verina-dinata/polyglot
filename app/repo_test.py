# Create approach without repository
# from database_manager import DatabaseManager
# from models import Word, Language

# dbm = DatabaseManager()

# session = dbm.get_session()

# new_word = Word(word='叫', language=Language.CN.value, pronounciation='jiào', type='Verb', english_definition='to be called')

# session.add(new_word)

# session.commit()

# Create with repository
from word_repository import WordRepository
from database_manager import DatabaseManager
from models import Word, Language

dbm = DatabaseManager()
session = dbm.get_session()

word_repo = WordRepository(session)
new_word = word_repo.create({"language": "chinese", "word": "hello", "pronounciation": "hello", "type": "noun", "english_definition": "hello"})

# Get all data from repository
word_repo.get_all(Word)

# Homework -> Refactor this into
word_repo.get_all()