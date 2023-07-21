<div align="center">

<img src="https://github.com/vandriodd/holbertonschool-AirBnB_clone/assets/110431271/16e8dbdd-c2b9-46a8-ad80-2d0b8729618a" alt="AirBnB" width=300 />
<h1> AirBnB clone: The console </h1>

<div align="left">

- This is the first step towards building our first full web application: the [AirBnB](https://es.airbnb.com/) clone.

## What’s a Command Interpreter?
- The user can interact with the operating system through a special process, in our case, we want to be able to manage the objects of our project and test them;
  * Create new object (ex: a new User or a new Place).
  * Retrieve an object from a file...
  * Update attributes of an object.
  * Destroy an object.
 
 ## Requirements
- All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- `README.md` file must exist
- All the files use the `pycodestyle (version 2.7.)` standard guidelines, including class and functions documentation
- All tests are execute using the `unittest` module

## Usage
### Installation
- `git clone https://github.com/micaelapicco/holbertonschool-AirBnB_clone` 

### Executing the Console:
After cloning the repository, the file *console.py* have to have execution permission;
```
your_terminal@~$ ./console.py
(hbnb)
```
It can be used in non-interactive mode though.
```
your_terminal@~$ echo "create City" | ./console.py 
(hbnb) c32ff5fb-858c-457a-9716-7c0d47e4c71b
(hbnb)
your_terminal@~$
```

### Supported Types of Object:
- `BaseModel`:
It is the base of all subclases, contains atributtes and methods that will be used by them; <br />
`State`, `City`, `Amenity`, `Place`, `Review`.

## Supported Commands

| Command  | Description                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------|
| create   | Creates a new object of the allowed types (its type must be specified).                                |
| show     | Shows the selected object, (type and id of it must be given).                                          |
| all      | Shows all the existing objects of a class, (if not argument given will show all the existing objects). |
| update   | Updates an object adding or updating the given attribute. (type, id, attribute, value required).       |
| destroy  | Destroys (removes) an object, (type and id required).                                                  |
| quit/EOF | Exits the program.                                                                                     |

#### Usage Commands:
* --> `create`: <br />
Creates a new object of the allowed types (its type must be specified). <br />
**Example:**
```
(hbnb) create User
59966872-4a99-49ba-92ac-8393538c749a
```

* --> `show`: <br />
Shows the selected object, (type and id of it must be given). <br />
**Example:**
```
(hbnb) show User 59966872-4a99-49ba-92ac-8393538c749a
["[User] (59966872-4a99-49ba-92ac-8393538c749a) {'id': '59966872-4a99-49ba-92ac-8393538c749a', 'created_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444506), 'updated_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444611)}"]
```

* --> `all`: <br />
Shows all the existing objects of a class, (if not argument given will show all the existing objects). <br />
**Example (no arguments):**
```
(hbnb) create City
7653c610-2cc4-4cd2-adf7-92bf04e12b0b
(hbnb) all
["[City] (7653c610-2cc4-4cd2-adf7-92bf04e12b0b) {'id': '7653c610-2cc4-4cd2-adf7-92bf04e12b0b', 'created_at': datetime.datetime(2023, 7, 7, 14, 16, 57, 604763), 'updated_at': datetime.datetime(2023, 7, 7, 14, 16, 57, 604816)}", "[User] (59966872-4a99-49ba-92ac-8393538c749a) {'id': '59966872-4a99-49ba-92ac-8393538c749a', 'created_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444506), 'updated_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444611)}"]
```
**Example:**
```
(hbnb) all User
["[User] (59966872-4a99-49ba-92ac-8393538c749a) {'id': '59966872-4a99-49ba-92ac-8393538c749a', 'created_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444506), 'updated_at': datetime.datetime(2023, 7, 7, 14, 17, 5, 444611)}"]
```

* --> `update`: <br />
Updates an object adding or updating the given attribute. (type, id, attribute, value required). <br />
**Example:**
```
(hbnb) create User
4db9b0b5-9dad-4e1e-a89c-8e752f60e52d
(hbnb) update User 4db9b0b5-9dad-4e1e-a89c-8e752f60e52d gonna "die:)"
(hbnb) show  User 4db9b0b5-9dad-4e1e-a89c-8e752f60e52d
["[User] (4db9b0b5-9dad-4e1e-a89c-8e752f60e52d) {'id': '4db9b0b5-9dad-4e1e-a89c-8e752f60e52d', 'created_at': datetime.datetime(2023, 7, 7, 14, 32, 14, 398566), 'updated_at': datetime.datetime(2023, 7, 7, 14, 32, 14, 399215), 'gonna': 'die:)'}"]
```

* --> `destroy`: <br />
Destroys (removes) an object, (type and id required). <br />
**Example:**
```
(hbnb) destroy User 59966872-4a99-49ba-92ac-8393538c749a
(hbnb destroy User 4db9b0b5-9dad-4e1e-a89c-8e752f60e52d
(hbnb) all
["[City] (7653c610-2cc4-4cd2-adf7-92bf04e12b0b) {'id': '7653c610-2cc4-4cd2-adf7-92bf04e12b0b', 'created_at': datetime.datetime(2023, 7, 7, 14, 16, 57, 604763), 'updated_at': datetime.datetime(2023, 7, 7, 14, 16, 57, 604816)}"]
```

* --> `quit` and `EOF`: <br />
Exits the program. <br />
**Example:**
```
your_terminal@~$ ./console.py
(hbnb) quit
your_terminal@~$ ./console.py
(hbnb) EOF
your_terminal@~$
```
## Testing:
All unittests can be executed with:
```
python3 -m unittest discover tests
```
# Web static
[Click here](https://micaelapicco.github.io/holbertonschool-AirBnB_clone/web_static/)
# Authors
-  [Emanel Trias](https://github.com/KrasniKot)
-  [Micaela Picco](https://github.com/micaelapicco)
