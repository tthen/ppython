

<!-- https://learn.microsoft.com/en-us/training/modules/python-create-manage-projects/ -->

<!-- https://learn.microsoft.com/en-us/training/browse/?terms=python -->


## Installing a virtual environment

A virtual environment is a self-contained copy of everything needed to run your program. This includes the Python interpreter and any libraries your program needs. By using a virtual environment, you can ensure your program will have access to the correct versions and resources to run correctly.


The basic workflow looks like this:

- Create a virtual environment that won't affect the rest of the machine.

- Step into the virtual environment, where you specify the Python version and libraries that you need.

- Develop your program.


### Installing virtualenv


> python3.9 -m pip install virtualenv

 python3.9     explicit version
 -m            run the main entry point
 pip           installer
 install       pip run install
 virtualenv    virtualenv


### Install a virtual environment Python version 3.9 in venv39 directory

 > python3.9 -m virtualenv venv39

From python3.9 and up you should not need to install pip. This now comes pre-installed with python.

$ python3.6 -m pip install virtualenv


### Activate the virtual environment

At this point, you have a virtual environment, but you haven't started using it. To use it, you need to activate it by calling an activate script in your env directory. Here's how the activation can look on Windows, Linux, and macOS:

In Windows

> venv39/Scripts/activate

In Linux, WSL or macOS

$ source venv39/bin/activate

### Installing IPython

(venv39) C:\Users\htorres\Downloads\PYTHON>python -m pip install IPython

(venv39) C:\Users\htorres\Downloads\PYTHON>IPython


### Deactivate a virtual environment

Windows

> deactivate

Linux

$ deactivate

### Create and Run Python Project

 Open a terminal and create a folder with your project name using the command as shown in the example below:


$ mkdir my_first_project
