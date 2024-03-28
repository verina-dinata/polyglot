from base_repository import BaseRepository
from models import Sentence

class SentenceRepository(BaseRepository):
    """
    A specific repository for managing User model operations.

    This class inherits from BaseRepository and provides additional methods
    specific to User management.
    """

    def __init__(self, session):
        super().__init__(session, Sentence)  # Call parent class constructor

    def create(self, data: dict) -> object:
        """
        Creates a new User record in the database.

        Args:
            data: A dictionary containing the data for the new user.

        Returns:
            The newly created User model instance.
        """

        sentence = Sentence(**data)
        self._save(sentence)
        return sentence
