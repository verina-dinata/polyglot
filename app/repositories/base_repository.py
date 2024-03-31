from sqlalchemy.exc import IntegrityError

class BaseRepository:
  """
  A base repository class for performing CRUD operations on SQLAlchemy models.

  This class serves as a template for creating model-specific repositories
  that inherit from it.

  Args:
      session: A SQLAlchemy session object.
  """

  def __init__(self, session, model_class):
    self.session = session
    self.model_class = model_class

  def get_by_id(self, id: int) -> object:
    """
    Retrieves a record by its primary key.

    Args:
        model_class: The SQLAlchemy model class representing the data.
        id: The primary key value of the record to retrieve.

    Returns:
        The model instance or None if not found.
    """

    return self.session.query(self.model_class).get(id)

  def get_all(self) -> list:
    """
    Retrieves all records from the database for a specific model.

    Args:
        model_class: The SQLAlchemy model class representing the data.

    Returns:
        A list of model instances.
    """
    return self.session.query(self.model_class).all()

  def get_with_pagination(self, page, items_per_page) -> list:
    """
    Retrieves records for page, with items per page

    Args:
        page: page number
        items_per_page: number of items returned per page

    Returns:
        A list of model instances.
    """
    offset = (page - 1) * items_per_page

    return self.session.query(self.model_class).offset(offset).limit(items_per_page).all()

  def update(self, obj, data: dict) -> object:
    """
    Updates an existing record based on its data.

    Args:
        obj: The model instance to be updated.
        data: A dictionary containing the updated data for the object.

    Returns:
        The updated model instance.

    Raises:
        IntegrityError: If there's a database constraint violation during update.
    """

    try:
      # Update attributes using dictionary unpacking
      for field, value in data.items():
        setattr(obj, field, value)

      self._save(obj)
      return obj
    except IntegrityError as e:
      # Handle potential database constraint violations
      self.session.rollback()
      raise e


  def _save(self, obj):
    """
    Internal method to perform session add and commit for an object.

    Args:
        obj: The model instance to be saved.
    """

    self.session.add(obj)
    self.session.commit()
    self.session.refresh(obj)  # Optional: Refresh to get latest data
