# AirBnB_clone

Holberton School has assigned a group project to create a clone of AirBnB.

The AirBnB Clone project will consist of multiple sub_projects.
This project is the fist of the series where we create the console using python.

# Console

Here we create the command line interpreter that will be used to manage our AirBnB objects.
This is our first step to creating our first full web application.

The commands used are:
+ create - creates a new instance(User or a Place).
+ show - retrieves a class with a specific ID from storage, and displays information related to it.
+ all - will work similar to show only it will display all the contents of storage.
+ destroy - Will remove a named object from the storage.
+ update - will update an element in storage.

## Where to start

Our shell should work like this in interactive mode:

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

This code should also work in non-interactive mode:

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
* [create]() - is used to make a new element to be stored in the local memory
```
  (hbnb) create BaseModel
  49faff9a-6318-451f-87b6-910505c55907
```

* [show]() - will print a string representation of an instance based on the class name
```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

* [update]() - Updates an instance based on the class name and id by adding or updating attribute
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

* [all]() - Prints all string representation of all instances based or not on the class name.
```
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```

* [destroy]() - Deletes an instance based on their class name and id
```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```


## Storage contents

The console is used to store everything that relates to our clone in models storage.
The attributes that will be stored are:
  - User
  - State
  - Amenity
  - Place
  - Review

## Collaborators

#### [Derek Clemens TUL-Cohort14- Github](https://github.com/urwithinrange)
#### [Christopher Caswell TUL-Cohort14- Github](https://github.com/Christopher-Caswell)