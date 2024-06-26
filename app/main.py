from fastapi import FastAPI, Query, Response
from fastapi.responses import StreamingResponse
from mangum import Mangum
import os

import repositories
import database

app = FastAPI()
session = database.DatabaseManager().get_session()
word_repo = repositories.WordRepository(session)
sentence_repo = repositories.SentenceRepository(session)

@app.get("/")
def read_root():
  return {}

@app.get("/api/v1/words")
def words_index(page: int = Query(default=1, description="Page number for word list (optional)")):
  words = word_repo.get_with_pagination(page, 36)
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

@app.get("/assets/sound/sentences/{filename}")
def get_sentence_mp3(filename: str):
  file_path = os.path.join("./assets/sound/sentences", filename)
  return stream_mp3(file_path)

@app.get("/assets/sound/words/{filename}")
def get_word_mp3(filename: str):
  file_path = os.path.join("./assets/sound/words", filename)
  return stream_mp3(file_path)


def stream_mp3(file_path):
  if not os.path.exists(file_path):
    return Response(status_code=404)

  def readfile():
    with open(file_path, mode="rb") as file:
      yield from file

  return StreamingResponse(readfile(), media_type="audio/mpeg")


handler = None
if __name__ == "__main__":
  uvicorn.run("app")
else:
  handler = Mangum(app, lifespan="off")
