## Write unit tests before implementation!

- Unit tests cannot be deprioritized.

- Time for writing unit tests factored in implementation time.

- Requirements are clearer and implementation easier.

Note: normal arguments, special arguments, bad arguments, return values, exceptions.

## Develop a complete unit test suite

```
data/ 
src/ 
|-- data/ 
|-- features/ 
|-- models/ 
|-- visualization/ 
tests/                     # Test suite 
|-- data/ 
|-- features/ 
|-- models/ 
|-- visualization/
```

Write unit tests for your own projects.

Issues related to deploying the code are listed as follows:

- Exactly the same transformations need to happen in `DEV`, `TEST`, and `PROD`
environments.
- As the code keeps getting updated in the `DEV` environment, how will the changes be
synced to the `PROD` environment?

- What type of testing do you plan to do in the `DEV` and `PROD` environments?

Let's look into two main strategies for deploying the code.

Batch development

This is the traditional development process. We develop the code, compile it, and then
test it. This process is repeated iteratively until all the requirements are met. Then, the
developed code is deployed.


Employing continuous integration and continuous delivery

Continuous integration/continuous delivery (CI/CD) in the context of Python refers
to continuous integration and deployment instead of conducting it as a batch process.
It helps to create a development-operations (DevOps) environment by bridging the gap
between development and operations.


CI refers to continuously integrating, building, and testing various modules of the code
as they are being updated. For a team, this means that the code developed individually by
each team member is integrated, built, and tested, typically many times a day. Once they
are tested, the repository in the source control is updated.

As Python code is dependent on external packages, keeping track of their names and
versions is part of automating the build process. A good practice is to list all these
packages in a file named requirements.txt. The name can be anything, but the
Python community typically tends to call it requirements.txt.

To install the packages, we will execute the following command:

```
$pip install -r requirements.txt
```

To create a requirements file that represents the packages used in our code, we can use
the following command:

```
$pip freeze > requirements.txt
```

Once the code is built and tested, we can choose to update the deployed code as well. That
will implement the CD part. If we choose to have a complete CI/CD process, it means
that each time a change is made, it is built and tested and the changes are reflected in the
deployed code. If managed properly, the end user will benefit from having a constantly
evolving solution.

### Life cycle of a function esting
```
Start test
test fail?
  true: Bugfix
  Start test again
else
  false: accepted implementation
  Bug found?
    true: Bugfix
  else
    Feature request or refactoring
	Start test again
```
### Python unit testing libraries

pytest, unittest, nosetests, doctest

**procedure for pytest**

_Step 1: Create a file_

Create `test_row_to_list.py` .
  
`test_` indicate unit tests inside (naming convention).
  
Also called test modules

_Step 2: Imports_

Test module: `test_row_to_list.py`

```
import pytest
import row_to_list
```

_Step 3: Unit tests are Python functions_

Test module:  test_row_to_list.py 

```
import pytest
import row_to_list

def test_for_clean_row ():
```

_Step 4: Assertion_

Test module: `test_row_to_list.py`

```
import pytest
import row_to_list

def test_for_clean_row():
  assert
```

Theoretical structure of an assertion

```
assert boolean_expression
assert True
assert False
```

Test module: test_row_to_list.py

```
import pytest
import row_to_list

def test_for_clean_row():
  assert row_to_list("2,081\t314,942\n") == \
    ["2,081", "314,942"]

def test_for_missing_area():
  assert row_to_list("\t293,410\n") is None

def test_for_missing_tab():
  assert row_to_list("1,463238,765\n") is None
```

_Checking for None values_

Do this for checking if var is None .

```
assert var is None
```

Do not do this.

```
assert var == None
```

_Step 5: Running unit tests_

Do this in the command line.

```
pytest test_row_to_list.py
```

### In the coding exercises...

_Step 1: Write unit tests and fix requirements_

Test module: `test_convert_to_int.py`

```
import pytest

def test_with_no_comma():
  ...

def test_with_one_comma():
  ...

def test_with_two_commas():
  ...
```

_Step 2: Run tests and watch it fail_

```
$ pytest test_convert_to_int.py
```

```
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-4.0.1, py-1.8.0, pluggy-0.11.0
rootdir: /tmp/tmpbhadho_b, inifile:
plugins: mock-1.10.0
collecting ...
collected 6 items
test_convert_to_int.py FFFFFF [100%]
=========================== 6 failed in 0.06 seconds ===========================
```

_Step 3: Implement function and run tests again_

```
def convert_to_int():
  ...


$ pytest test_convert_to_int.py

============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-4.0.1, py-1.8.0, pluggy-0.11.0
rootdir: /tmp/tmp793ds6mt, inifile:
plugins: mock-1.10.0
collecting ...
collected 6 items
test_convert_to_int.py ...... [100%]
=========================== 6 passed in 0.03 seconds ===========================
```
