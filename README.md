# AirBnB_clone

This AirBnB clone is the first in a myriad of projects that will eventually lead to a working website production of the AirBnB model. This first project is strictly the Python and JSON script and an initial implemetation of structure. This repository contains the classes, attributes, and base methods utilized to create and store base models.
The goal of this project is first and foremost: learning.

As we continue to develop in this project, any bugs that arise will be addressed. Please see the collaborators section for contact information if you find a bug and want to help or if you are interested in revising the code.

# Console

Here we create the command line interpreter that will be used to manage the AirBnB objects.
This is our first step in creating our first full web application.

The commands used are:
+ All - similar to show, plus displays all instances of that class in storage.
+ Create - creates a new instance (i.e. User or Place).
+ Destroy - removes an object from storage.
+ Show - retrieves a class with a specific ID from storage and displays dictionary information related to it.
+ Update - updates an element of an object in storage.

## Where to start

The console behavior in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The console behavior in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Commands
* [create]() - is used to store a new element in local memory
```
  (hbnb) create BaseModel
  49faff9a-6318-451f-87b6-910505c55907
```

* [show]() - prints a string representation of an instance based on a class name
```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

* [update]() - updates an instance based on a class name and id by adding or updating attribute
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

* [all]() - prints all string representation of all instances based on a class name
```
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```

* [destroy]() - deletes an instance based on a class name and id
```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```


## Storage contents

The console stores attributes and classes using json.
The attributes stored are:
  - Amenity
  - Place
  - Review
  - State
  - User

## Collaborators

#### [Derek Clemens TUL-Cohort14- Github](https://github.com/urwithinrange)
#### [Christopher Caswell TUL-Cohort14- Github](https://github.com/Christopher-Caswell)