egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

'''
Our favourite modules
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters with are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
We hope you find these useful!
'''

'''
Useful Third-Party Packages
Being able to install and import third party libraries is useful, but to be an effective programmer you also need to know what libraries are available for you to use. People typically learn about useful new libraries by word of mouth; from an online recommendation or from a colleague. If you're a new Python programmer you may not have many colleagues, so to get you started here's a list of packages that are popular with engineers at Udacity.

IPython - A better interactive Python interpreter
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask - a lightweight framework for making web applications and APIs.
Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest - extends Python's builtin assertions and unittest module.
PyYAML - For reading and writing YAML files.
NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
ggplot - Another 2D plotting library, based on R's ggplot2 library.
Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet - A cross-platform application framework intended for game development.
Pygame - A set of Python modules designed for writing games.
pytz - World Timezone Definitions for Python
'''
'''
requirements.txt
Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs programmers often list a project's dependencies in a file called requirements.txt. This is an example requirements.txt file:

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
Each line of the file includes the name of a package and its version number. The version number is technically optional, but it usually should be included. Libraries can change subtly (or dramatically!) between versions, so it's important to use the same library versions that the program's author had when they wrote the program.

You can use pip to install all of a project's dependencies at once with this command:

$ pip3 install -r requirements.txt
'''
