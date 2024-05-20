# 0x15. API - Python Scripting Back-end API

## Background Context

Old-school system administrators often rely solely on Bash for scripting. While Bash is suitable for many tasks, it can become messy and inefficient compared to other programming languages. The new generation of system administrators, typically referred to as Site Reliability Engineers (SREs), are essentially software engineers who manage systems instead of building products. One key difference between them and their predecessors is their knowledge of more than just Bash scripting.

A popular way to expose an application and its data is through an API. APIs are often the public-facing parts of websites and microservices, allowing external interaction with data. In this project, you will access employee data via an API, organize it, and export it to different data structures.

This task is an excellent example of something not well-suited for Bash scripting, so we will build Python scripts instead.

## Resources

- [Friends don’t let friends program in shell script](https://example.com)
- [What is an API](https://example.com)
- [What is an API? In English, please](https://example.com)
- [What is a REST API](https://example.com)
- [What are microservices](https://example.com)
- [PEP8 Python style guide](https://example.com)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

### General

- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic package and module name style
- Pythonic class name style
- Pythonic variable name style
- Pythonic function name style
- Pythonic constant name style
- Significance of CapWords or CamelCase in Python

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A `README.md` file at the root of the project folder is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key to avoid exceptions if the key doesn't exist
- Code should not be executed when imported (use `if __name__ == "__main__":`)

#### Requirements:

- Use the `urllib` or `requests` module
- The script must accept an integer as a parameter, which is the employee ID
- Display on the standard output the employee's TODO list progress in the exact format:
  - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  - Second and subsequent lines: display the title of completed tasks with one tabulation and one space before each `TASK_TITLE`

## Tasks 📃

### 0. Gather data from an API
**Script:** `0-gather_data_from_an_API.py`  
**Description:** Python script that returns information on the to-do list progress of a given employee ID.  
**Usage:** `python3 0-gather_data_from_an_API.py <employee ID>`  
**Output:** `Employee <employee name> is done with tasks(<# completed tasks>/<total # tasks>):`

### 1. Export to CSV
**Script:** `1-export_to_CSV.py`  
**Description:** Python script exports to-do list information of a given employee ID to CSV format.  
**Usage:** `python3 1-export_to_CSV.py <employee ID>`  
**File name:** `<user id>.csv`  
**Format:** `"<user id>","<username>","<task completed status>","<task title>"`

### 2. Export to JSON
**Script:** `2-export_to_JSON.py`  
**Description:** Python script that exports to-do list information of a given employee ID to JSON format.  
**Usage:** `python3 2-export_to_JSON.py <employee ID>`  
**File name:** `<user id>.json`  
**Format:** `{ "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"} }, ... ]}`

### 3. Dictionary of list of dictionaries
**Script:** `3-dictionary_of_list_of_dictionaries.py`  
**Description:** Python script that exports to-do list information for all employees to JSON format.  
**Usage:** `python3 3-dictionary_of_list_of_dictionaries.py`  
**File name:** `todo_all_employees.json`  
**Format:** `{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}`
