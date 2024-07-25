def Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in _instance:
            _instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return _instance[cls]
