## Description
This is the More classes and objects section for the ALX SE program

# Notes
## Importance of Using Setter Methods in Rectangle Class Initialization

In the `Rectangle` class, using setter methods (`self.width = width` and `self.height = height`) instead of directly assigning values to `self.__width` and `self.__height` in the `__init__` function is crucial. Here's why:

1. **Validation:** The setter methods perform validation checks on the input values (`width` and `height`) using `isinstance()` and conditional statements. This ensures that only valid values (integers and non-negative) are assigned to the attributes. If the input values are invalid, appropriate exceptions (`TypeError` and `ValueError`) are raised, providing meaningful error messages.

2. **Data Integrity:** By going through the setter methods, the attributes (`self.width` and `self.height`) maintain their data integrity according to the defined validation rules. This prevents inconsistent or unexpected attribute values and helps maintain the expected behavior of the `Rectangle` class.

3. **Code Consistency:** Using the setter methods consistently throughout the class promotes code consistency. It ensures that any assignments to the attributes follow the same validation rules, regardless of where they occur in the code. This simplifies the maintenance and understanding of the class in the long run.

**Note**: This should be used in other functions too apart from `__init__`


## Instance Methods vs Static Methods vs Class Methods

In Python, there are three types of methods commonly used in classes: instance methods, static methods, and class methods.

### Instance Methods

- Instance methods are defined within a class and are intended to operate on instance-specific data.
- They receive the instance (`self`) as the first parameter, allowing them to access and modify instance attributes.
- Instance methods can be called on an instance of the class.

Example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
area = circle.calculate_area()
print(area)  # Output: 78.5
```

### Static Methods
- Static methods are defined within a class, but they do not have access to instance-specific data.
- They are not bound to the instance or the class itself, and they do not receive the instance or class as the first parameter.
- Static methods are used when the method does not depend on instance or class state and does not modify them.
- They can be called directly on the class without creating an instance.
e.g.
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(3, 4)
print(result)  # Output: 7
```

### Class Methods
- Class methods are defined within a class and operate on the class itself rather than instances.
- They receive the class as the first parameter (cls) instead of the instance.
- Class methods can access class-level attributes and modify them.
- They are typically used for operations that involve the class as a whole.
e.g.

```python
class Car:
    num_wheels = 4

    @classmethod
    def get_num_wheels(cls):
        return cls.num_wheels

wheels = Car.get_num_wheels()
print(wheels)  # Output: 4
```
