# 0x02. Shell, I/O Redirections and filters

## Overview

This project dives into the core concepts of I/O redirections and filters in the Unix shell. Participants will learn how to manipulate input and output streams using various commands, allowing for sophisticated data processing and management directly from the command line.

## Learning Objectives

By the end of this project, participants should be able to:

- Describe the functionality of commands such as `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr`, `rev`, and `cut`.
- Redirect standard output to a file and standard input from a file.
- Pipe the output from one program to the input of another.
- Combine multiple commands and filters to process data through redirection.
- Identify and use special characters in the shell including white spaces, quotes, backslashes, pipes, and more.
- Display, concatenate, and reverse text within the command line.
- Remove specific sections from each line of files using command line utilities.
- Understand the format and purpose of system files like `/etc/passwd` and `/etc/shadow`.

## Resources

- **Reading:**
  - [Shell, I/O Redirection](#)
  - [Special Characters](#)

- **Man Pages:**
  - `echo`
  - `cat`
  - `head`
  - `tail`
  - `find`
  - `wc`
  - `sort`
  - `uniq`
  - `grep`
  - `tr`
  - `rev`
  - `cut`
  - `passwd` (5)

## Requirements

### General

- **Environment:** All scripts will be tested on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must be exactly two lines long (`$ wc -l file` should print 2).
  - The first line of all scripts must be `#!/bin/bash`.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod u+x file`).
  - No use of backticks, `&&`, `||`, or `;`.
  - Do not use `sed` or `awk`.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining what each script is doing.

## More Info

- **File Inspection:** Participants are encouraged to explore the `/etc/passwd` and `/etc/shadow` files to understand system configurations related to user and group definitions.
- **Permissions:** Ensure that all your files are executable to facilitate testing and usage.

### Example Usage

```bash
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$ chmod u+x 12-file_type
julien@ubuntu:/tmp$ ./12-file_type
