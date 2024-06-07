# 0x05. Processes and Signals

## Overview

This project focuses on understanding processes and signal handling in Unix-like operating systems, particularly Linux. Participants will learn how to manage processes, handle various signals, and use system calls related to process management.

## Learning Objectives

By the end of this project, participants should be able to:

- Define what a PID (Process ID) is.
- Explain what constitutes a process in Linux.
- Identify methods to find a process's PID and terminate processes.
- Understand what signals are and how they are used in process management.
- Recognize signals that cannot be ignored and explain their significance.
- Use commands like `ps`, `pgrep`, `pkill`, `kill`, `exit`, and `trap` to interact with and manage processes.

## Resources

- **Reading:**
  - [Linux PID](#)
  - [Linux process](#)
  - [Linux signal](#)
  - [Process management in linux](#)

- **Man or Help:**
  - `ps`
  - `pgrep`
  - `pkill`
  - `kill`
  - `exit`
  - `trap`

## Requirements

### General

- **Environment:** All scripts will be tested on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must start with `#!/usr/bin/env bash` to ensure portability.
  - The second line in each script should be a comment explaining the script's purpose.
  - Scripts must be executable (`chmod +x file`).
  - End all files with a new line.
  - Scripts must pass Shellcheck without any errors to ensure quality and adherence to best practices.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining the function and purpose of each script.

## More Info

### Shellcheck

- **Using Shellcheck:** Shellcheck is a static analysis tool for shell scripts. This tool will be used to ensure scripts are free from common errors and follow best practices. It is available via `apt-get` as version 0.7.0:
  ```bash
  sudo apt-get install shellcheck
