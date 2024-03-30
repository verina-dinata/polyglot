from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseManager:

  def __init__(self) -> None:
    self.engine = create_engine('sqlite:///database/sqlite.db')
    self.session_maker = sessionmaker(bind=self.engine)
    Base.metadata.create_all(self.engine)


  def get_session(self) -> object:
    """
    Returns a new SQLAlchemy session object.

    Returns:
      A new SQLAlchemy session object.
    """
    return self.session_maker()
