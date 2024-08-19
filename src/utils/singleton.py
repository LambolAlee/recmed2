def Singleton(cls):
    """Singleton class decorator."""
    if not hasattr(cls, "__singleton__"):
        cls.__singleton__ = None

    def instance(*args, **kwargs):
        if cls.__singleton__ is None:
            print(f"create instance of {cls.__name__}")     # TODO：add logs here
            setattr(cls, "__singleton__", cls(*args, **kwargs))
        return cls.__singleton__

    return instance
