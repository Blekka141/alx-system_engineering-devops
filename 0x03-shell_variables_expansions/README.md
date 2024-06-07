# 0x03. Shell, init files, variables and expansions

## Overview

This project explores the initialization processes of the shell, the use and scope of variables, and the utility of expansions and expressions within Bash. Participants will delve into the mechanics of shell environment configuration, command aliases, and arithmetic operations directly from the command line.

## Learning Objectives

By the end of this project, participants should be able to:

- Describe what happens when you type `$ ls -l *.txt` and how shell expansions affect this command.
- Explain the purpose and content of shell initialization files like `/etc/profile`, `/etc/profile.d` directory, and the `~/.bashrc` file.
- Distinguish between local and global variables, and understand how to manipulate them.
- Recognize the roles of reserved variables such as `HOME`, `PATH`, and `PS1`.
- Define what special parameters are, including the significance of the `$?` parameter.
- Utilize expansions for renaming, length, and command substitution.
- Understand the use and syntax differences between single and double quotes.
- Perform basic arithmetic operations within the shell without using external programs like `bc`.
- Create, use, and manage aliases, including disabling them temporarily.
- Execute commands from a file in the current shell using the `source` or `.` command.

## Resources

- **Reading:**
  - [Expansions](#)
  - [Shell Arithmetic](#)
  - [Variables](#)
  - [Shell initialization files](#)
  - [The alias Command](#)
  - [Technical Writing](#)

- **Man or Help:**
  - `printenv`
  - `set`
  - `unset`
  - `export`
  - `alias`
  - `unalias`
  - `.`
  - `source`
  - `printf`

## Requirements

### General

- **Environment:** All scripts will be tested on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must be exactly two lines long (`$ wc -l file` should print 2).
  - The first line of all scripts must be `#!/bin/bash`.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod u+x file`).
  - No use of backticks, `&&`, `||`, or `;`.
  - Do not use `bc`, `sed`, or `awk`.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining what each script is doing.

## More Info

- **File Inspection:** Participants are encouraged to read and understand the configuration and functionalities defined in `/etc/profile`, `/etc/inputrc`, and `~/.bashrc`.
- **Directory Inspection:** Review the scripts and settings in the `/etc/profile.d` directory to gain a better understanding of environment setup.

### Example Usage

```bash
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$ chmod u+x 12-file_type
julien@ubuntu:/tmp$ ./12-file_type

## Quiz Answers

### Question #0: Which command should I use to display the exit code of the previous command?
- echo $?

### Question #1: Which command should I use to display a variable?
- echo $MYVAR

### Question #2: What is the variable name who contains the previous working directory path?
- OLDPWD

### Question #3: Which command should I use to define a new command push for pushing in Github?
- alias push="git push"
