## Description
This is the import and modules section of the ALX SE program.

## Notes
* To handle the hidden\_4, I installed Python 3.8 as a zip file and run this script on the terminal:
```python
import hidden_4
names = dir(hidden_4)
filtered_names = sorted(name for name in names if not name.startswith('__'))
for name in filtered_names:
    print(name)
```
The `dir` function names all the classes, names and functions in the code.
* To make the code non-importable we use
```python
if __name__ == "__main__":
```
* Another thing to consider is that the "\*" symbol is a wildcard, so when multiplying you use `'*'` instead
* You can print using `os.write()`. Its implementation is of the form `os.write(fd, line)`. For the line variable you input the number of bytes/binary representation using the `str.encode()` function
