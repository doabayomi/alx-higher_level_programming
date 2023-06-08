#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    # listing names in the file
    valid_names = []
    for name in names:
        if name.startswith("__"):
            continue
        valid_names.append(name)
    valid_names = sorted(valid_names)

    # print the valid names
    for name in valid_names:
        print(name)
