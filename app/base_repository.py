class BaseRepository:
    """
    A base repository class for performing CRUD operations on SQLAlchemy models.

    This class serves as a template for creating model-specific repositories
    that inherit from it.

    Args:
        session: A SQLAlchemy session object.
    """

    def __init__(self, session):
        self.session = session

    def get_by_id(self, model_class, id: int) -> object:
        """
        Retrieves a record by its primary key.

        Args:
            model_class: The SQLAlchemy model class representing the data.
            id: The primary key value of the record to retrieve.

        Returns:
            The model instance or None if not found.
        """

        return self.session.query(model_class).get(id)

    def get_all(self, model_class) -> list:
        """
        Retrieves all records from the database for a specific model.

        Args:
            model_class: The SQLAlchemy model class representing the data.

        Returns:
            A list of model instances.
        """

        return self.session.query(model_class).all()

    def _save(self, obj):
        """
        Internal method to perform session add and commit for an object.

        Args:
            obj: The model instance to be saved.
        """

        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)  # Optional: Refresh to get latest data
