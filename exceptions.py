class UniversityError(Exception):
    """Базовое пользовательское исключение."""
    pass

class EntityNotFoundError(UniversityError):
    """Исключение, выбрасываемое при отсутствии запрашиваемой сущности."""
    pass