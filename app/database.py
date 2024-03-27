from sqlalchemy import create_engine

def create_sqlite_engine():
  """
  Creates a connection engine to the SQLite database.

  Returns:
      sqlalchemy.engine.Engine: The engine object for interacting with the database.
  """
  # No arguments passed to create_engine
  engine = create_engine('sqlite:///sqlite.db')
  return engine
