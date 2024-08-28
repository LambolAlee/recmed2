class DescriptiveAttr:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{owner.__name__}_{name}'

    def __get__(self, obj, cls):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)
