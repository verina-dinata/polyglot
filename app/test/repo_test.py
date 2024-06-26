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
from repositories.sentence_repository import SentenceRepository
from database.database_manager import DatabaseManager
from models.word import Word, Language

dbm = DatabaseManager()
session = dbm.get_session()

word_repo = WordRepository(session)
sentence_repo = SentenceRepository(session)
# new_word = word_repo.create({"language": "chinese", "word": "hello", "pronounciation": "hello", "type": "noun", "english_definition": "hello"})

# Get all data from repository
# print(word_repo.get_all())
# print(word_repo.get_by_id(1))
print(word_repo.get_with_pagination(1, 40))

# word_to_be_changed = word_repo.get_by_id(1)
# print(word_to_be_changed)
# updated_values = {'word': 'abc', 'pronounciation': 'abc'}
# print(word_repo.update(word_to_be_changed, updated_values))

# Homework 3 -> Create sample code for reading CSV files
