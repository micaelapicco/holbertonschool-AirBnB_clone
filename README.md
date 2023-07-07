<div align="center">

<img src="https://github.com/vandriodd/holbertonschool-AirBnB_clone/assets/110431271/16e8dbdd-c2b9-46a8-ad80-2d0b8729618a" alt="AirBnB" width=300 />
<h1> AirBnB clone: The console </h1>

<div align="left">

- This is the first step towards building our first full web application: the [AirBnB](https://es.airbnb.com/) clone.

## What’s a Command Interpreter?
- The user can interact with the operating system through a special process, in our case, we want to be able to manage the objects of our project and test them;
  * Create new object (ex: a new User or a new Place)
  * Retrieve an object from a file...
  * Update attributes of an object
  * Destroy an object

### Executing the Console:
After cloning the repository, the file *console.py* have to have execution permission;
```
your_terminal@~$ ./console.py
(hbnb) _
```

#### Supported Types of Object:
- `BaseModel`:
It is the base of all subclases, contains atributtes and methods that will be used by them;
`State`, `City`, `Amenity`, `Place`, `Review"`

#### Supported Commands:
* --> `create`:
Creates a new object of the allowed types (its type must be specified).
**Example:**
```
(hbnb) create User
c82182df-6f57-4c7f-a5fb-6625337cefd7
```

* --> `show`: 
Shows the selected object (type and id of it must be given).
**Example**
```
(hbnb) show User c82182df-6f57-4c7f-a5fb-6625337cefd7
[User] (c82182df-6f57-4c7f-a5fb-6625337cefd7) {'id': 'c82182df-6f57-4c7f-a5fb-6625337cefd7', 'created_at': datetime.datetime(2023, 7, 7, 11, 24, 6, 730425), 'updated_at': datetime.datetime(2023, 7, 7, 11, 24, 6, 730463)}
```
 
# Authors
-  [Emanel Trias](https://github.com/KrasniKot)
-  [Micaela Picco](https://github.com/micaelapicco)