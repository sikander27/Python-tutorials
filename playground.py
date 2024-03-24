import functools
import sys


class AnnouncerMeta(type):
    """
    Print method name when called.

    FIXME Something is wrong here, please fix it.
    """

    def __new__(cls, class_name, bases, namespace):
        for name, func in list(namespace.items()):
            if callable(func):
                def create_call_wrapper(inner_name):
                    @functools.wraps(func)
                    def call_wrapper(*args, **kwargs):
                        try:
                            print(f"Calling {inner_name}")
                            return func(*args, **kwargs)
                        finally:
                            print(f"Called {inner_name}")
                    return call_wrapper

                namespace[name] = create_call_wrapper(name)

        return type.__new__(cls, class_name, bases, namespace)


# Leave code below as is; focus on fixing the metaclass

class ExampleClass(metaclass=AnnouncerMeta):
    """
    Just an example of a class using AnnouncerMeta class.
    """

    def foo(self, n):
        return f"foo{n}"

    def bar(self, n):
        return f"bar{n}"


# test_name = sys.stdin.readline().strip()
# if test_name == "sample_test":
instance = ExampleClass()
print(instance.foo(1) + instance.bar(2))
