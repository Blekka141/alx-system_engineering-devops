# 0x01. Shell, permissions

## Overview

This project delves into Unix permissions, covering the manipulation and understanding of file and directory permissions in a Linux environment. Participants will learn about the different types of permissions, how to modify them, and the use of various commands to manage user and group ownerships.

## Learning Objectives

By the end of this project, participants should be able to:

- Explain the functionality of commands like `chmod`, `sudo`, `su`, `chown`, `chgrp`, `id`, and more.
- Understand Linux file permissions and how they affect user interactions with the filesystem.
- Represent the permissions for owner, group, and others using octal and symbolic methods.
- Change file permissions, ownership, and group association using command-line tools.
- Discuss why only superusers can change the owner of a file and how to execute commands with superuser privileges.
- Create users and groups in Linux and manage their associations.
- Display user and group IDs, including real and effective IDs, and understand their implications in permissions management.

## Resources

- **Reading:**
  - [Permissions](#)

- **Man Pages:**
  - `chmod`
  - `sudo`
  - `su`
  - `chown`
  - `chgrp`
  - `id`
  - `groups`
  - `whoami`
  - `adduser`
  - `useradd`
  - `addgroup`

## Requirements

### General

- **Environment:** All scripts will be tested on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must be exactly two lines long (`$ wc -l file` should print 2).
  - The first line of all scripts must be `#!/bin/bash`.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod u+x file`).
  - No use of backticks, `&&`, `||`, or `;`.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining what each script is doing.

## More Info

- **File Permissions:**
  To test your scripts, use the `chmod u+x file` command to make them executable. This command changes the file's mode, allowing the user to execute it as a program.

### Example Usage

```bash
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$ chmod u+x 12-file_type
julien@ubuntu:/tmp$ ./12-file_type

## Quiz Answers

### Question #0: What is the numerical value for the ----w---x permission?
- 021

### Question #1: What is the permission value for a file without any restriction?
- 777

### Question #2: Which command should I use for changing a file permission?
- chmod

### Question #3: What is the numerical value for the r-xr--r-- permission?
- 544

### Question #4: What is the numerical value for the rwx------ permission?
- 700

### Question #5: Which command should I use for changing a file owner?
- chown

### Question #6: What is the permission value for a file read only for the group owner?
- 040
