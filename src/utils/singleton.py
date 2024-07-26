def Singleton(cls):
    """Singleton class decorator."""
    instances = {}

    def instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    cls.instance = instance

    return cls
