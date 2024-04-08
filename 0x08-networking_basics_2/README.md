# 0x08. Networking Basics #1

## Overview

This project builds upon foundational networking concepts, focusing on addressing schemes like localhost and 0.0.0.0, the significance of the hosts file, and network interface management. Participants will enhance their understanding of network configurations and the utilities used to manage and troubleshoot network interfaces.

## Learning Objectives

By the end of this project, participants should be able to:

- Define `localhost` and the IP address `127.0.0.1`, and explain their purpose.
- Describe the use of the IP address `0.0.0.0` and how it differs from `localhost`.
- Understand the function and structure of the `/etc/hosts` file.
- Display the active network interfaces on a machine using command-line tools.

## Resources

- **Reading:**
  - [What is localhost](#)
  - [What is 0.0.0.0](#)
  - [What is the hosts file](#)
  - [Netcat examples](#)

- **Man or Help:**
  - `ifconfig`
  - `telnet`
  - `nc` (Netcat)
  - `cut`

## Requirements

### General

- **Environment:** All files will be interpreted on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - The first line of all Bash scripts must be `#!/usr/bin/env bash` to ensure compatibility across environments.
  - The second line of each script must be a comment that clearly explains the script's functionality.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod +x file`).
  - Ensure all scripts pass Shellcheck without any errors to maintain best practices in scripting.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, providing detailed descriptions of each script and their purpose in the context of networking basics.

## More Info

### Shellcheck

Shellcheck is a static analysis tool for shell scripts that helps to identify syntax errors and poor practices:

- **Installation:**
  ```bash
  sudo apt-get install shellcheck

