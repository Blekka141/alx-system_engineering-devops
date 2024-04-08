# 0x04. Loops, conditions and parsing

## Overview

This project is designed to deepen understanding of shell scripting with a focus on loops, conditions, and data parsing using Bash. Participants will explore various control structures that facilitate complex decision-making and repetitive actions within scripts.

## Background Context

As scripts become more complex, efficiently managing and automating tasks requires a solid understanding of conditional statements and looping constructs. This project covers these fundamental concepts, ensuring participants are well-prepared for advanced scripting challenges.

## Learning Objectives

By the end of this project, participants should be able to:

- Create and use SSH keys.
- Explain the benefits of using `#!/usr/bin/env bash` over `#!/bin/bash`.
- Utilize `while`, `until`, and `for` loops to automate repetitive tasks.
- Implement conditional statements like `if`, `else`, `elif`, and `case` to make logical decisions in scripts.
- Use the `cut` command for basic text processing.
- Understand and apply file and other comparison operators.

## Resources

- **Reading:**
  - [Loops sample](#)
  - [Variable assignment and arithmetic](#)
  - [Comparison operators](#)
  - [File test operators](#)
  - [Make your scripts portable](#)

- **Man or Help:**
  - `env`
  - `cut`
  - `for`
  - `while`
  - `until`
  - `if`

## Requirements

### General

- **Environment:** All files will be interpreted on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must start with `#!/usr/bin/env bash` to ensure portability.
  - The second line in each script should be a comment explaining the script's purpose.
  - Scripts must be executable (`chmod +x file`).
  - End all files with a new line.
  - Scripts must pass Shellcheck without any errors to ensure quality and best practices are met.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining the purpose and functionality of each script.

## More Info

### Shellcheck

Shellcheck is a tool for linting and static analysis of shell scripts. It helps identify syntax errors, poor practices, and other issues that could lead to bugs:

- **Installation:** Shellcheck can be installed on Linux via package managers or compiled from source. For detailed installation instructions, refer to the [Shellcheck GitHub page](https://github.com/koalaman/shellcheck).

### Example Usage

```bash
# Check a script with Shellcheck
shellcheck my_script

# Example of output
[SC2034]: my_script:3: warning: my_variable appears unused. Verify use (or export if used externally).
