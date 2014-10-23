#!/usr/bin/env python

"""
These are some common imports.
"""
import argparse

"""
This scripts is a basic command line tool with some examples of a main
function, as well as an example class and function where you might do some
work.

"""

class WorkingClass(object):
    """
    This class is your top level object. Associate any operations with this,
    and this gives you a class based scripts.
    """

    def __init__(self):

        pass

    def doTheStuff(self):
        """
        Function to do the work in a class based script.
        """
        print("Doing some class-based work.")


def doTheStuff(*args, **kwargs):
    """
    Main function.
    You can also make a top level function, for simpler stuff..
    """

    print("Doing some function-based work.")

def main():
    """
    Main driver for the script.

    I like to put the 'main' code in a def file, just more organized.
    """
    descText= """

    Place anything you want here. This text is displayed by arg parse
    if you do <command> --help.

    """

    parser = argparse.ArgumentParser(description=descText)

    """
    Required parameter usually go first, with no --

    parser.add_argument("param1",
        help="First parameter, required")

    """

    """
    Next, add any optoinal parameters, usually with a double --, a single
    - is also possible, in fact you can have both.

    parser.add_argument("--option","-o",
            action="store_true",
            help="This is a boolean option. It will be false normally, and true if specified.")
    """

    """
    It's even possible to get a 'list' of things.. using the nargs (number of args).
    nargs="*" will get a list, but you can specifiy a number (say 2).

    parser.add_argument("--xl",
        nargs="*",
        help="Excel Input files containing language translations. "
            "Required columns are 'TextKey', and one or more columns "
            "with the title 'Language:XX', where XX is the desired JSON "
            "output language code. "
            "Note: Titles are case sensitive."
    )
    """

    # Get the arguments. The parsed values will be in args.<argname> Easy.
    args = parser.parse_args()

    """
    Now, do what you want. I recommend making a class, possibly at the top of this file, that
    contains the majority of the code. then
    """

    # For class based:
    wc = WorkingClass() # No params..
    wc.doTheStuff() # Again, no params

    # For function based
    doTheStuff()


if __name__ == '__main__':
    main()
