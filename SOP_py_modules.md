


## Docstring

A powerful use of a docstring is for functional or class-level documentation. If we place the docstring just after the definition of a function or a class, Python associates the docstring with the function or a class. This is placed in the `__doc__` attribute of that particular function or class. 

In all cases, the docstrings should use the triple-double quote (""") string format. This should be done whether the docstring is multi-lined or not. At a bare minimum, a docstring should be a quick summary of whatever is it you’re describing and should be contained within a single line:


While developing the code, various types of documentation need to be produced, including the following: Line-by-line commentary; Functional or class-level documentation; Algorithmic details


### Creating a docstring

```
"""This is a quick summary line used as a description of the object."""
```

Multi-lined docstrings are used to further elaborate on the object beyond the summary. All multi-lined docstrings have the following parts:

- A docstring should be placed right after the function or the class definition.

- A one-line summary line. A docstring should be given a one-line summary followed by a more detailed description.

- A blank line proceeding the summary

- Any further elaboration for the docstring

- Another blank line. Blank spaces should be strategically used to organize the comments but they should not be overused.

```
"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

# Notice the blank line above. Code should continue on this line.
```

## Class Docstrings

Class Docstrings are created for the class itself, as well as any class methods. The docstrings are placed immediately following the class or class method indented by one level:

```
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')
```

Class docstrings should contain the following information:

- A brief summary of its purpose and behavior

- Any public methods, along with a brief description

- Any class properties (attributes)

- Anything related to the interface for subclassers, if the class is intended to be subclassed


The class constructor parameters should be documented within the `__init__` class method docstring. Individual methods should be documented using their individual docstrings. Class method docstrings should contain the following:

- A brief description of what the method is and what it’s used for

- Any arguments (both required and optional) that are passed including keyword arguments

- Label any arguments that are considered optional or have a default value

- Any side effects that occur when executing the method

- Any exceptions that are raised

- Any restrictions on when the method can be called


Let’s take a simple example of a data class that represents an Animal. This class will contain a few class properties, instance properties, a `__init__`, and a single instance method:


```
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))

```

## Package and Module Docstrings

Package docstrings should be placed at the top of the package’s `__init__.py` file. This docstring should list the modules and sub-packages that are exported by the package.

Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. Module docstrings are placed at the top of the file even before any imports. Module docstrings should include the following:

- A brief description of the module and its purpose

- A list of any classes, exception, functions, and any other objects exported by the module


The docstring for a module function should include the same items as a class method:

- A brief description of what the function is and what it’s used for

- Any arguments (both required and optional) that are passed including keyword arguments

- Label any arguments that are considered optional

- Any side effects that occur when executing the function

- Any exceptions that are raised

- Any restrictions on when the function can be called


## Script Docstrings

Scripts are considered to be single file executables run from the console. Docstrings for scripts are placed at the top of the file and should be documented well enough for users to be able to have a sufficient understanding of how to use the script. It should be usable for its “usage” message, when the user incorrectly passes in a parameter or uses the -h option.

Finally, any custom or third-party imports should be listed within the docstrings to allow users to know which packages may be required for running the script. Here’s an example of a script that is used to simply print out the column headers of a spreadsheet:


```
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()

```

## Documenting Your Python Projects

Python projects come in all sorts of shapes, sizes, and purposes. The way you document your project should suit your specific situation. Keep in mind who the users of your project are going to be and adapt to their needs. Depending on the project type, certain aspects of documentation are recommended. The general layout of the project and its documentation should be as follows:

```
project_root/
│
├── project/  # Project source code
├── docs/
├── README
├── HOW_TO_CONTRIBUTE
├── CODE_OF_CONDUCT
├── examples.py
```

Projects can be generally subdivided into three major types: Private, Shared, and Public/Open Source.


### Private Projects

Private projects are projects intended for personal use only and generally aren’t shared with other users or developers. Documentation can be pretty light on these types of projects. There are some recommended parts to add as needed:

- Readme: A brief summary of the project and its purpose. Include any special requirements for installation or operating the project.

- examples.py: A Python script file that gives simple examples of how to use the project.

Remember, even though private projects are intended for you personally, you are also considered a user. Think about anything that may be confusing to you down the road and make sure to capture those in either comments, docstrings, or the readme.

- docs: A folder that contains further documentation. The next section describes more fully what should be included and how to organize the contents of this folder.


### The Four Main Sections of the docs Folder

All projects should have the following four major sections to help you focus your work:

- Tutorials: Lessons that take the reader by the hand through a series of steps to complete a project (or meaningful exercise). Geared towards the user’s learning.

- How-To Guides: Guides that take the reader through the steps required to solve a common problem (problem-oriented recipes).

- References: Explanations that clarify and illuminate a particular topic. Geared towards understanding.

- Explanations: Technical descriptions of the machinery and how to operate it (key classes, functions, APIs, and so forth). Think Encyclopedia article.



## References


https://peps.python.org/pep-0257/

https://realpython.com/documenting-python-code/

