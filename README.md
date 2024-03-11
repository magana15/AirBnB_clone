# AirBnB Clone Project

## Description
This project is an AirBnB clone, a simplified version of the popular accommodation platform, designed to understand and implement the basic concepts of a command-line interpreter, serialization/deserialization, and basic storage of Python objects.

## Command Interpreter
The command interpreter is a tool that allows users to interact with the AirBnB clone. It supports various commands to manipulate and manage instances of different classes, such as creating, updating, deleting, and retrieving objects.

### How to Start
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/AirBnB_clone.git
    ```

2. Change into the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:

    ```bash
    python3 console.py
    ```

### How to Use
The command interpreter provides a prompt `(hbnb)` where you can enter various commands to interact with the AirBnB clone. Here are some basic commands:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Display the details of an instance.
- `destroy <class_name> <id>`: Delete an instance.
- `all <class_name>`: Display all instances of a class.
- `update <class_name> <id> <attribute> "<value>"`: Update the attribute of an instance.

### Examples
```bash
(hbnb) create BaseModel
New instance created with ID: 5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4

(hbnb) show BaseModel 5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4
[BaseModel] (5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4) {'id': '5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4', 'created_at': datetime.datetime(2022, 1, 1, 12, 0), 'updated_at': datetime.datetime(2022, 1, 1, 12, 0)}

(hbnb) all BaseModel
[BaseModel] (5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4) {'id': '5ee2d8f5-1ce1-45f0-9bfc-7bde5b739fd4', 'created_at': datetime.datetime(2022, 1, 1, 12, 0), 'updated_at': datetime.datetime(2022, 1, 1, 12, 0)}

