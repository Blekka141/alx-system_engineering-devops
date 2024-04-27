# 0x00. Shell, basics

## Overview

This project introduces the basics of the Unix shell, focusing on navigating the file system, managing files, and using essential shell commands. Participants will gain foundational skills necessary for working proficiently in a Unix-like environment.

## Learning Objectives

By the end of this project, participants should be able to:

- Define what the shell is and differentiate between a terminal and a shell.
- Navigate the filesystem using commands like `cd`, `pwd`, and `ls`.
- Manage files using commands such as `cp`, `mv`, `rm`, and `mkdir`.
- Utilize links, including symbolic links and hard links, and understand their differences.
- Employ commands and utilities such as `type`, `which`, `man`, and `help`.
- Read and understand man pages effectively.
- Understand and use shell scripts, including setting the correct permissions.
- Explain the use and importance of the shebang (`#!/bin/bash`).
- Discuss the purpose of command aliases and how to define them.
- Use wildcards for matching file patterns in the shell.
- Understand what LTS (Long Term Support) means in the context of software versions.

## Resources

- **Reading:**
  - [What Is "The Shell"?](#)
  - [Navigation](#)
  - [Looking Around](#)
  - [A Guided Tour](#)
  - [Manipulating Files](#)
  - [Working With Commands](#)
  - [Reading Man pages](#)
  - [Keyboard shortcuts for Bash](#)
  - [Shebang](#)

- **Man or Help:**
  - `cd`, `ls`, `pwd`, `less`, `file`, `ln`, `cp`, `mv`, `rm`, `mkdir`, `type`, `which`, `help`, `man`

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

- **Repository Description:** A README.md file at the root of the repository describing the repository.
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

###Question #0: How do you change directory on Linux?
- cd

### Question #1: What command would you use to list files on Linux?
- ls

### Question #2: What does LTS stand for?
- Long Term Support

### Question #3: What does RTFM stand for?
- Read The F** Manual

