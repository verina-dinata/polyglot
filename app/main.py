from fastapi import FastAPI, Query, File, Response
from fastapi.responses import StreamingResponse
import os

from  repositories.word_repository import WordRepository
from  repositories.sentence_repository import SentenceRepository
from database.database_manager import DatabaseManager

app = FastAPI()
session = DatabaseManager().get_session()
word_repo = WordRepository(session)
sentence_repo = SentenceRepository(session)

@app.get("/")
def read_root():
  return {}

@app.get("/api/v1/words")
def words_index(page: int = Query(default=1, description="Page number for word list (optional)")):
  words = word_repo.get_with_pagination(page, 40)
  array = []
  for word in words:
    array.append(word.json())
  return array

@app.get("/api/v1/words/{id}/sentences")
def get_sentences_for_word(id: str):
  word = word_repo.get_by_id(id)
  sentences = word.sentences
  array = []
  for sentence in sentences:
    array.append(sentence.json())
  return array


mp3_directory = "./assets/sound/sentences"
@app.get("/assets/sound/sentences/{filename}")
def get_mp3(filename: str):
    # Check if the requested file exists
    file_path = os.path.join(mp3_directory, filename)

    if not os.path.exists(file_path):
        return Response(status_code=404)

    def readfile():
        with open(file_path, mode="rb") as file:
            yield from file

    return StreamingResponse(readfile(), media_type="audio/mpeg")
