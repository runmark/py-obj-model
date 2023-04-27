MISSING = object()


class AttrMap:
    def __init__(self, attrs: dict):
        self._attrs = attrs
        self._next = {}

    def index_of(self, name):
        return self._attrs.get(name, -1)

    def next(self, name):
        if name in self._attrs:
            return self
        if name in self._next:
            return self._next[name]
        attrs = self._attrs.copy()
        attrs[name] = len(attrs)
        new_map = AttrMap(attrs)
        self._next[name] = new_map
        return new_map


EMPTY_MAP = AttrMap({})


class _Base:
    def __init__(self, fields: dict = None):
        self._map = EMPTY_MAP
        self._values = []
        if fields:
            for k, v in fields.items():
                self.set_attr(k, v)
        # self._fields = fields or {}

    def get_attr(self, name: str):
        # if name not in self._fields:
        if name not in self._map._attrs:
            raise AttributeError(f"'{self.cls.name}' has no attribute {name}")
        return self.read_attr(name)

    def read_attr(self, name: str):
        index = self._map.index_of(name)
        if index < 0:
            return MISSING
        return self._values[index]
        # return self._fields.get(name, MISSING)

    def set_attr(self, name: str, value):
        # self._fields[name] = value
        index = self._map.index_of(name)
        if index < 0:
            self._map = self._map.next(name)
            self._values.append(value)
        else:
            self._values[index] = value


class _Class(_Base):
    def __init__(
        self, name: str, base: None, fields: dict = None, user_class: bool = True
    ):
        super().__init__(fields)
        if user_class:
            self._base = base or Object
        else:
            self._base = base
        self.name = name

    # def get_attr(self, name: str):
    #     value = self.read_attr(name)
    #     if value is not MISSING:
    #         return value
    #     elif self._base == None:
    #         raise AttributeError(f"'{self.cls.name}' has no attribute {name}")
    #     else:
    #         return self._base.get_attr(name)

    def read_attr(self, name: str):
        value = super().read_attr(name)
        if value is not MISSING:
            return value
        return self._base.read_attr(name) if self._base else MISSING

    def is_instance(self, cls):
        return cls is Type

    def inheritance_hierarchy(self):
        yield self
        # if self._base:
        #     yield self._base.inheritance_hierarchy()
        if self._base:
            for base in self._base.inheritance_hierarchy():
                yield base


class _Instance(_Base):
    def __init__(self, cls: _Class, fields: dict = None):
        super().__init__(fields)
        self.cls = cls

    def get_attr(self, name: str):
        value = self.read_attr(name)
        if value is MISSING:
            value = self.cls.read_attr(name)
        if value is MISSING:
            default_getter = self.cls.read_attr("__getattr__")
            if default_getter is not MISSING:
                return default_getter(self, name)
        if value is MISSING:
            raise AttributeError(f"'{self.cls.name}' has no attribute {name}")
        if callable(value):
            return self.make_bound_method(value)
        else:
            return value

        # raise AttributeError(f"'{self.cls.name}' has no attribute {name}")

    def is_instance(self, cls):
        # print(list(self.cls.inheritance_hierarchy()))
        return cls in self.cls.inheritance_hierarchy()

    def set_attr(self, name: str, value):
        default_setter = self.cls.read_attr("__setter__")
        if default_setter is not MISSING:
            return default_setter(name, value)
        return super().set_attr(name, value)

    def make_bound_method(self, func):
        def method(*args, **kwargs):
            return func(self, *args, **kwargs)

        return method

    def call_method(self, func_name, *args, **kwargs):
        method = self.get_attr(func_name)
        return method(*args, **kwargs)


def define_class(
    name: str, base: _Class = None, fields: dict = None, user_class: bool = True
) -> _Class:
    return _Class(name, base=base, fields=fields, user_class=user_class)


def create_instance(cls: _Class, fields: dict = None) -> _Instance:
    return _Instance(cls, fields=fields)


def is_instance(obj, cls) -> bool:
    return obj.is_instance(cls)


Object = define_class("Object", user_class=False)
Type = define_class("Type", base=Object, user_class=False)
