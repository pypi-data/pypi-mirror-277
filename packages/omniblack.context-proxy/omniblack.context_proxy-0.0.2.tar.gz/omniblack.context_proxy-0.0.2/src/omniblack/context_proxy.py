import math
import operator

from contextvars import ContextVar
from functools import wraps


def urnary_operator(cls, handler):

    @wraps(handler)
    def wrapper(self):
        value = self._ContextProxy__get_current()
        return handler(value)

    name = handler.__name__.removesuffix('_')

    setattr(cls, f'__{name}__', wrapper)


def binary_operator(cls, handler):

    @wraps(handler)
    def wrapper(self, other):
        value = self._ContextProxy__get_current()
        if issubclass(type(other), ContextProxy):
            other = self._ContextProxy__get_current()

        return handler(value, other)

    name = handler.__name__.removesuffix('_')

    setattr(cls, f'__{name}__', wrapper)


def reverse_binary_operator(cls, handler):

    @wraps(handler)
    def wrapper(self, other):
        value = self._ContextProxy__get_current()
        if issubclass(type(other), ContextProxy):
            other = self._ContextProxy__get_current()

        return handler(other, value)

    name = handler.__name__.removesuffix('_')

    setattr(cls, f'__r{name}__', wrapper)


def inplace_binary_operator(cls, handler):

    @wraps(handler)
    def wrapper(self, other):
        value = self._ContextProxy__get_current()
        if issubclass(type(other), ContextProxy):
            other = self._ContextProxy__get_current()

        context_var = self._ContextProxy__context_var
        context_var.set(handler(value, other))

        return self

    name = handler.__name__.removesuffix('_')

    setattr(cls, f'__{name}__', wrapper)


def trinary_operator(cls, handler):

    @wraps(handler)
    def wrapper(self, other, other2):
        value = self._ContextProxy__get_current()

        if issubclass(type(other), ContextProxy):
            other = other._ContextProxy__get_current()

        if issubclass(type(other2), ContextProxy):
            other2 = other2._ContextProxy__get_current()

        return handler(value, other, other2)

    name = handler.__name__.removesuffix('_')

    setattr(cls, f'__{name}__', wrapper)


pickle_methods = {
    '__getnewargs_ex__',
    '__getnewargs__',
    '__getstate__',
    '__setstate__',
    '__reduce__',
    '__reduce_ex__',
}


class ContextProxy:
    def __init__(self, *, init=None, name=None, var=None):
        if init is None and var is None:
            msg = 'ContextProxy must be passed var or init.'
            raise TypeError(msg)

        if name is None:
            name = var.name if var is not None else init.__name__

        object.__setattr__(self, '_ContextProxy__name', name)

        object.__setattr__(self, '_ContextProxy__init', init)

        object.__setattr__(
            self,
            '_ContextProxy__context_var',
            var or ContextVar(name),
        )

    def __get_current(self):
        current = self.__context_var.get(None)

        if current is None:
            current = self.__init()
            self.__context_var.set(current)

        return current

    def __getattr__(self, name):
        value = self.__get_current()

        return getattr(value, name)

    def __getattribute__(self, name):
        if name in pickle_methods:
            raise AttributeError(name)
        else:
            return super().__getattribute__(name)

    @property
    def __class__(self):
        value = self.__get_current()

        return value.__class__

    def __call__(self, *args, **kwargs):
        value = self.__get_current()

        return value(*args, **kwargs)

    @property
    def __doc__(self):
        value = self.__get_current()

        return value.__doc__

    @property
    def __weakref__(self):
        value = self.__get_current()

        return value.__weakref__

    @property
    def __dict__(self):
        value = self.__get_current()

        return value.__dict__

    def __get__(self, instance, owner=None):
        value = self.__get_current()

        if issubclass(type(instance), ContextProxy):
            instance = instance.__get_current()

        if issubclass(type(owner), ContextProxy):
            owner = owner.__get_current()

        return value.__get__(instance, owner)

    def __set__(self, instance, value):
        value = self.__get_current()

        return value.__set__(instance, value)

    def __delete__(self, instance):
        value = self.__get_current()

        return value.__delete__(instance)

    @property
    def __objclass__(self):
        value = self.__get_current()

        return value.__objclass__

    def __del__(self):
        self.__context_var.set(None)
        self.__context_var = None


urnary_ops = (
    abs,
    aiter,
    anext,
    bool,
    bytes,
    complex,
    dir,
    float,
    hash,
    int,
    iter,
    len,
    next,
    repr,
    reversed,
    str,

    math.ceil,
    math.floor,
    math.trunc,

    operator.index,
    operator.invert,
    operator.length_hint,
    operator.neg,
    operator.not_,
    operator.pos,
)

for op in urnary_ops:
    urnary_operator(ContextProxy, op)

reversable_binary_ops = (
    divmod,

    operator.add,
    operator.and_,
    operator.floordiv,
    operator.lshift,
    operator.matmul,
    operator.mod,
    operator.mul,
    operator.or_,
    operator.pow,
    operator.rshift,
    operator.sub,
    operator.truediv,
    operator.xor,
)

binary_ops = (
    delattr,
    format,

    operator.concat,
    operator.contains,
    operator.delitem,
    operator.eq,
    operator.ge,
    operator.getitem,
    operator.gt,
    operator.le,
    operator.lt,
    operator.ne,
    operator.setitem,
    *reversable_binary_ops,
)

for op in binary_ops:
    binary_operator(ContextProxy, op)

for op in reversable_binary_ops:
    reverse_binary_operator(ContextProxy, op)

trinary_ops = (
    operator.setitem,
    setattr,
)

for op in trinary_ops:
    trinary_operator(ContextProxy, op)

inplace_binary_ops = (
    operator.iadd,
    operator.iand,
    operator.iconcat,
    operator.ifloordiv,
    operator.ilshift,
    operator.imod,
    operator.imul,
    operator.imatmul,
    operator.ior,
    operator.ipow,
    operator.irshift,
    operator.isub,
    operator.itruediv,
    operator.ixor,
)

for op in inplace_binary_ops:
    inplace_binary_operator(ContextProxy, op)
