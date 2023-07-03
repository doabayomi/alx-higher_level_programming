## Description
This is the More classes and objects section for the ALX SE program

## Notes
### Importance of Using Setter Methods in Rectangle Class Initialization

In the `Rectangle` class, using setter methods (`self.width = width` and `self.height = height`) instead of directly assigning values to `self.__width` and `self.__height` in the `__init__` function is crucial. Here's why:

1. **Validation:** The setter methods perform validation checks on the input values (`width` and `height`) using `isinstance()` and conditional statements. This ensures that only valid values (integers and non-negative) are assigned to the attributes. If the input values are invalid, appropriate exceptions (`TypeError` and `ValueError`) are raised, providing meaningful error messages.

2. **Data Integrity:** By going through the setter methods, the attributes (`self.width` and `self.height`) maintain their data integrity according to the defined validation rules. This prevents inconsistent or unexpected attribute values and helps maintain the expected behavior of the `Rectangle` class.

3. **Code Consistency:** Using the setter methods consistently throughout the class promotes code consistency. It ensures that any assignments to the attributes follow the same validation rules, regardless of where they occur in the code. This simplifies the maintenance and understanding of the class in the long run.

**Note**: This should be used in other functions too apart from `__init__`
