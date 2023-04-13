
## Naming scheme

They are written in a PEP 8 document that has a complete section on naming conventions,
which is followed by many code bases. PEP 8 has naming and style guidelines that are
suggested. You can read more about it at https://www.Python.org/dev/peps/pep-0008/.


The naming scheme suggested in PEP 8 can be summarized as follows:

- In general, all module names should be all_lower_case.

- All class names and exception names should be CamelCase.

- All global and local variables should be all_lower_case.

- All functions and method names should be all_lower_case.

- All constants should be ALL_UPPER_CASE


Some guidelines about the structure of the code from PEP 8 are given here:

- Indentation is important in Python. Do not use Tab for indentation. Instead, use four spaces.

- Limit nesting to four levels.

- Remember to limit the number of lines to 79 characters. Use the \ symbol to break long lines.

- To make code readable, insert two blank lines to separate functions.

- Insert a single black line between various logical sections.

Methods

Method names should use lowercase. The name should consist of a single word or more
than one word separated by underscores. You can see an example of this here:

```
calculate_sum
```

To make the code readable, the method should preferably be a verb, related to the
processing that the method is supposed to perform.

If a method is non-public, it should have a leading underscore. Here's an example of this:

```
_my_calculate_sum
```


Boolean variables
Starting a Boolean variable with is or has makes it more readable. You can see a couple
of examples of this here:

class Patient:
    is_admitted = False
    has_heartbeat = False


Collection variables
As collections are buckets of variables, it is a good idea to name them in a plural format, as
illustrated here:

class Patient:
    admitted_patients = ['John','Peter']


Dictionary variables
The name of the dictionary is recommended to be as explicit as possible. For example, if
we have a dictionary of people mapped to the cities they are living in, then a dictionary
can be created as follows:

persons_cities = {'Imran': 'Ottawa', 'Steven': 'Los Angeles'}


Constant
For constants, the recommendation is to use uppercase words or words separated by an
underscore. An example of a constant is given here:

CONVERSION_FACTOR


Classes
Classes should follow the CamelCase style—in other words, they should start with
a capital letter. If we need to use more than one word, the words should not be separated
by an underscore, but each word that is appended should have an initial capital letter.
Classes should use a noun and should be named in a way to best represent the entity the
class corresponds to. One way of making the code readable is to use classes with
suffixes that have something to do with their type or nature, such as the following:

• HadoopEngine
• ParquetType
• TextboxWidget

Here are some points to keep in mind:
• There are exception classes that handle errors. Their names should always have
Error as the trailing word. Here's an example of this:

FileNotFoundError

• Some of Python's built-in classes do not follow this naming guideline.
• To make it more readable, for base or abstract classes, a Base or Abstract prefix
can be used. An example could be this:

AbstractCar
BaseClass


Packages
The use of an underscore is not encouraged while naming a package. The name should be
short and all lowercase. If more than one word needs to be used, the additional word
or words should also be lowercase. Here's an example of this:

mypackage



Modules
When naming a module, short and to-the-point names should be used. They need to be
lowercase, and more than one word will be joined by underscores. Here's an example:

main_module.py


Import conventions
Over the years, the Python community has developed a convention for aliases that are
used for commonly used packages. You can see an example of this here:

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels as sm
import matplotlib.pyplot as plt


Arguments
Arguments are recommended to have a naming convention similar to variables, because
arguments of a function are, in fact, temporary variables.


