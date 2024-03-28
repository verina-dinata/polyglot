import csv
from word_repository import WordRepository
from sentence_repository import SentenceRepository
from database_manager import DatabaseManager
from models import Language

dbm = DatabaseManager()
session = dbm.get_session()
word_repo = WordRepository(session)
sentence_repo = SentenceRepository(session)

with open('../data/words.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
    # Access data in each row using indexing
        word_string = row[0]
        pronounciation = row[1]
        type = row[2]
        english_definition = row[3]
        sentence1 = row[4]
        sentence1_pro = row[5]
        sentence1_eng_def = row[6]
        sentence2 = row[7]
        sentence2_pro = row[8]
        sentence2_eng_def = row[9]

        new_word = word_repo.create({"language": Language.CN.value, "word_string": word_string, "pronounciation": pronounciation, "type": type, "english_definition": english_definition})

        new_sentence1 = sentence_repo.create({"sentence": sentence1, "pronounciation": sentence1_pro, "english_definition": sentence1_eng_def})
        new_sentence2 = sentence_repo.create({"sentence": sentence2, "pronounciation": sentence2_pro, "english_definition": sentence2_eng_def})

        new_word.sentences.append(new_sentence1)
        new_word.sentences.append(new_sentence2)
