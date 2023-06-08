## Description
This is the import and modules section of the ALX SE program.

## Notes
* To handle the hidden\_4, I installed Python 3.8 as a zip file and run this script on the terminal:
```python
import sys
import os
file_directory = os.path.abspath('C:/Users/LENOVO/Downloads')
sys.path.append(file_directory)
import hidden_4
names = dir(hidden_4)
filtered_names = sorted(name for name in names if not name.startswith('__'))
for name in filtered_names:
    print(name)
```
* To make the code non-importable we use
```python
if __name__ == "__main__":
```
