#!/usr/bin/python3

class MyList(list):
    """A modified list object
    """
    def print_sorted(self):
        """Prints the list with its members sorted
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
