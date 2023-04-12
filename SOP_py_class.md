

## Introduction

lass constructors are a fundamental part of object-oriented programming in Python. They allow you to create and properly initialize objects of a given class, making those objects ready to use. Class constructors internally trigger Python’s instantiation process, which runs through two main steps: instance creation and instance initialization.

If you want to dive deeper into how Python internally constructs objects and learn how to customize the process, then this tutorial is for you.

In this SOP, you’ll:

- Understand Python’s internal instantiation process X

- Customize object initialization using `.__init__()`

- Fine-tune object creation by overriding `.__new__()`


Once you have a class to work with, then you can start creating new instances or objects of that class, which is an efficient way to reuse functionality in your code.

Creating and initializing objects of a given class is a fundamental step in object-oriented programming. This step is often referred to as object construction or instantiation. The tool responsible for running this instantiation process is commonly known as a class constructor.

In short, Python’s instantiation process starts with a call to the class constructor, which triggers the instance creator, `.__new__()`, to create a new empty object. The process continues with the instance initializer, `.__init__()`, which takes the constructor’s arguments to initialize the newly created object.

To explore how Python’s instantiation process works internally, consider the following example of a Point class that implements a custom version of both methods, `.__new__()` and `.__init__()`, for demonstration purposes:

```
# point.py

class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
```


The `.__new__()` method also takes `*args` and `**kwargs`, which allow for passing an undefined number of initialization arguments to the underlying instance.



Here’s a breakdown of what this code does:

- Line 3 defines the Point class using the class keyword followed by the class name.

- Line 4 defines the `.__new__()` method, which takes the class as its first argument. Note that using cls as the name of this argument is a strong convention in Python, just like using self to name the current instance is. The method also takes *args and **kwargs, which allow for passing an undefined number of initialization arguments to the underlying instance.

- Line 5 prints a message when `.__new__()` runs the object creation step.

- Line 6 creates a new Point instance by calling the parent class’s `.__new__()` method with cls as an argument. In this example, object is the parent class, and the call to super() gives you access to it. Then the instance is returned. This instance will be the first argument to `.__init__()`.

- Line 8 defines `.__init__()`, which is responsible for the initialization step. This method takes a first argument called self, which holds a reference to the current instance. The method also takes two additional arguments, x and y. These arguments hold initial values for the instance attributes .x and .y. You need to pass suitable values for these arguments in the call to Point(), as you’ll learn in a moment.

- Line 9 prints a message when `.__init__()` runs the object initialization step.

- Lines 10 and 11 initialize .x and .y, respectively. To do this, they use the provided input arguments x and y.

- Lines 13 and 14 implement the `.__repr__()` special method, which provides a proper string representation for your Point class.


dditionally, keep in mind that `.__init__()` must not explicitly return anything different from None, or you’ll get a TypeError exception:




In `.__init__()`, you can also run any transformation over the input arguments to properly initialize the instance attributes. For example, if your users will use Rectangle directly, then you might want to validate the supplied width and height and make sure that they’re correct before initializing the corresponding attributes:

```
>>> class Rectangle:
...     def __init__(self, width, height):
...         if not (isinstance(width, (int, float)) and width > 0):
...             raise ValueError(f"positive width expected, got {width}")
...         self.width = width
...         if not (isinstance(height, (int, float)) and height > 0):
...             raise ValueError(f"positive height expected, got {height}")
...         self.height = height
...

>>> rectangle = Rectangle(-21, 42)
Traceback (most recent call last):
    ...
ValueError: positive width expected, got -21
```

In this updated implementation of `.__init__()`, you make sure that the input width and height arguments are positive numbers before initializing the corresponding .width and .height attributes. If either validation fails, then you get a ValueError.



Now say that you’re using inheritance to create a custom class hierarchy and reuse some functionality in your code. If your subclasses provide a `.__init__()` method, then this method must explicitly call the base class’s `.__init__()` method with appropriate arguments to ensure the correct initialization of instances. To do this, you should use the built-in super() function like in the following example:

```
>>> class Person:
...     def __init__(self, name, birth_date):
...         self.name = name
...         self.birth_date = birth_date
...

>>> class Employee(Person):
...     def __init__(self, name, birth_date, position):
...         super().__init__(name, birth_date)
...         self.position = position
...

>>> john = Employee("John Doe", "2001-02-07", "Python Developer")

>>> john.name
'John Doe'
>>> john.birth_date
'2001-02-07'
>>> john.position
'Python Developer'
```


