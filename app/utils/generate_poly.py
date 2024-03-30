"""Getting Started Example for Python 2.7+/3.3+"""
import sys
sys.path.append('../app')

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
from tempfile import gettempdir
from repositories.word_repository import WordRepository
from repositories.sentence_repository import SentenceRepository
from database.database_manager import DatabaseManager

# Create a client using the credentials and region
def create_polly_session():
  session = Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='ap-southeast-1',
  )
  return session.client("polly")

def generate_sound(text, language, path):
  voiceId = "Zhiyu" if language == "chinese" else "Joanna"
  try:
    # Request speech synthesis
    response = polly.synthesize_speech(
      Text=text,
      OutputFormat="mp3",
      VoiceId=voiceId,
      SampleRate="24000",
    )

  except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

  if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
      output = path + ".mp3"
      try:
      # Open a file for writing the output as a binary stream
        with open(output, "wb") as file:
          file.write(stream.read())
      except IOError as error:
        # Could not write to file, exit gracefully
        print(error)
        sys.exit(-1)

  else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)

def generate_sound_for_words():
  dbm = DatabaseManager()
  session = dbm.get_session()
  word_repo = WordRepository(session)
  sentence_repo = SentenceRepository(session)

  words = word_repo.get_all()
  for word in words:
    print('Generating sound for: ', word.word_string)
    # generate chinese sound
    word_cn = word.word_string
    path = "assets/sound/words/" + str(word.id) + "_word_string_cn"
    generate_sound(word_cn, word.language, path)

    # generate english definition
    word_en = word.english_definition
    path = "assets/sound/words/" + str(word.id) + "_definition_en"
    generate_sound(word_en, "english", path)

    # generate sounds for sentence
    sentences = word.sentences
    for sentence in sentences:
       # generate chinese sound
      sentence_cn = sentence.sentence_string
      path = "assets/sound/sentences/" + str(sentence.id) + "_sentence_string_cn"
      generate_sound(sentence_cn, word.language, path)

      # generate english definition
      sentence_en = sentence.english_translation
      path = "assets/sound/sentences/" + str(sentence.id) + "_translation_en"
      generate_sound(sentence_en, "english", path)


polly = create_polly_session()

generate_sound_for_words()
