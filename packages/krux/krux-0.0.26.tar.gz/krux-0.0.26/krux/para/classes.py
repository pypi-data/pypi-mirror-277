# yet another version of Schema
__all__ = ['ParaBase', 'Para', 'ParaItem', 'P']

from collections import OrderedDict
from krux.types.null import Null
from .exceptions import *


class ParaBase(type):
    """Meta class for para"""
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__

        # Ensure initialization is only performed for subclasses of Para
        # (Excluding Para class itself)
        parents = [b for b in bases if isinstance(b, ParaBase)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        _items = OrderedDict()

        # Create the class
        for base in bases:
            if base_items := getattr(base, '_items', None):
                _items.update(base_items)

            for key, value in base.__dict__.items():
                if isinstance(value, ParaItem):
                    _items[key] = value

        to_pop = []
        for key, value in attrs.items():
            if isinstance(value, ParaItem):
                _items[key] = value
                to_pop.append(key)

        for key in to_pop:
            attrs.pop(key)

        module = attrs.pop('__module__')

        new_attrs = {
            '__module__': module,
            '_items': _items,
            **attrs,
        }

        new_class = super_new(cls, name, bases, new_attrs)
        return new_class


class Para(metaclass=ParaBase):
    def __init__(self, **kwargs):
        self._dic = {}

        for field, item in self._items.items():
            if item.default is not Null:
                self._dic[field] = item.default

        for field, value in kwargs.items():
            if field in self._items:
                self._dic[field] = value

        self._validate_values()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return {field: self[field] for field in self._items}

    def copy(self):
        return self.__class__.from_dict(self._dic)

    def vary(self, **kwargs):
        return self.__class__.from_dict({**self._dic, **kwargs})

    def _validate_values(self):
        for field, item in self._items.items():
            if field not in self._dic:
                if item.required:
                    raise MissingRequiredParaItem(field)
            else:
                raw_value = self._dic[field]
                if callable(raw_value):
                    raw_value = raw_value(self)
                item.validate(raw_value)

    def __len__(self):
        return len(self._items)

    # dict compatible methods
    def keys(self):
        return self._items.keys()

    def values(self):
        for field in self.keys():
            yield self[field]

    def items(self):
        for field in self.keys():
            yield field, self[field]

    def __getitem__(self, field):
        if field not in self._items:
            raise InvalidParaField(f'Invalid para field {field} for {self}.')

        if field in self._dic:
            value = self._dic[field]
            if callable(value):
                return value(self)
            else:
                return value
        else:
            return None

    def __getattr__(self, field):
        return self[field]

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def preview(self):
        pass


class ParaItem:
    def __init__(self,
                 name='', desc='',
                 default=Null,
                 required=False,
                 vmin=None, vmax=None,
                 **kwargs):
        self.name = name
        self.default = default
        self.required = required
        self.desc = desc
        self.vmin = vmin
        self.vmax = vmax

    def validate(self, value):
        if self.vmin is not None and value < self.vmin:
            raise ValueOutOfBound(f'{value} is too small for {self}, min value: {self.vmin}.')

        if self.vmax is not None and value > self.vmax:
            raise ValueOutOfBound(f'{value} is too large for {self}, max value: {self.vmax}.')

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'


def P(name='', desc='',
      default=Null, required=False,
      vmin=None, vmax=None,
      **kwargs):
    # This shortcut function will become a factory for creating ParaItem objects.
    # ParaItem may be extended to more subclasses
    return ParaItem(name=name, desc=desc,
                    default=default, required=required,
                    vmin=vmin, vmax=vmax,
                    **kwargs)