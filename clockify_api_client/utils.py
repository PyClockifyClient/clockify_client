from typing_extensions import Self


class Singleton(type):
    """Singleton metaclass. Creates **singleton** instead of normal class when used as metaclass of class

    """
    _instances = {}

    def __call__(cls, *args, **kwargs) -> Self:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
