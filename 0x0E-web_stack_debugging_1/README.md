# 0x0E. Web Stack Debugging #1

## Concepts

For this project, we are focusing on the following key concepts:
- **Network Basics**: Understanding the fundamental aspects of networking that affect web servers.
- **Web Stack Debugging**: The process of identifying and correcting issues that affect the operation and performance of web stack components.

## Requirements

### General

- **Editors**: vi, vim, emacs
- **Environment**: All scripts will be tested on Ubuntu 20.04 LTS.
- **Documentation**: A README.md file at the root of the folder of the project is mandatory.
- **Scripting**:
  - All Bash script files must be executable.
  - Scripts must pass [Shellcheck](https://www.shellcheck.net/) (version 0.3.7) without any error.
  - Bash scripts must run without error.
  - The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
  - The second line of all your Bash scripts should contain a comment explaining the script's purpose.
- **Restrictions**:
  - You are not allowed to use `wget`.

## Tasks

### Task 0: Nginx likes port 80

#### Objective
Diagnose and resolve why an Ubuntu container's Nginx installation is not listening on port 80. This involves using debugging tools and methods to correct the configuration to ensure Nginx listens on the desired port across all active IPv4 addresses.

#### Expected Outcome
- Nginx running and properly configured to listen on port 80.
- A minimal Bash script that automates this configuration.

### Task 1: Make it sweet and short

#### Objective
Refine the solution from Task #0 to make the Bash script shorter and more efficient while adhering to strict syntax rules.

#### Requirements
- Script is no longer than 5 lines.
- Proper Bash script formatting without using semicolons, logical operators, or external scripts.
- Validates that the service initialization reports Nginx as not running, then restarts and configures it correctly.

#### Expected Outcome
A succinct and efficient script that ensures Nginx is properly installed and configured, as verified through service status checks and web page responses.

## Additional Resources

- [Network Basics Tutorial](https://example.com/network-basics)
- [Introduction to Web Stack Debugging](https://example.com/web-stack-debugging)

