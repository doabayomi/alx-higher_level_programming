#!/usr/bin/python3
"""A modified list implementation with method to print
members of the list in sorted order
"""


class MyList(list):
    """A modified list object
    """
    def print_sorted(self):
        """Prints the list with its members sorted
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
