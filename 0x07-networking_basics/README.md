# 0x07. Networking Basics #0

## Overview

This project is an introduction to fundamental networking concepts, including the OSI model, different types of networks (LAN and WAN), the internet, IP addressing, and key TCP/UDP protocols. Participants will gain a foundational understanding of how networks operate and are structured.

## Learning Objectives

By the end of this project, participants should be able to:

- Explain the OSI model, its layers, and its purpose.
- Differentiate between LAN and WAN, including their typical usages and geographical sizes.
- Define what the Internet is and describe the role of IP addresses.
- Distinguish between IPv4 and IPv6, and explain the necessity of IPv6.
- Identify the differences between TCP and UDP, and understand the concept of ports.
- Recognize common ports such as those for SSH (22), HTTP (80), and HTTPS (443).
- Use networking tools like `ping` to verify connectivity.

## Resources

- **Reading:**
  - [OSI model](#)
  - [Different types of network](#)
  - [LAN network](#)
  - [WAN network](#)
  - [Internet](#)
  - [MAC address](#)
  - [IP address](#)
  - [Private and public address](#)
  - [IPv4 and IPv6](#)
  - [Localhost](#)
  - [TCP and UDP](#)
  - [TCP/UDP ports List](#)
  - [What is ping /ICMP](#)
  - [Positional parameters](#)

- **Man or Help:**
  - `netstat`
  - `ping`

## Requirements

### General

- **Environment:** All scripts will be interpreted on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - Each script must start with `#!/usr/bin/env bash` for universal environment compatibility.
  - The second line of every script must be a comment explaining the script's purpose.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod +x file`).
  - Ensure scripts pass Shellcheck without errors to ensure best practices in scripting.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining the function and purpose of each script.

## More Info

### Script Examples

```bash
# Example of how to check network connectivity with ping
#!/usr/bin/env bash
# This script checks network connectivity using ping
ping -c 4 google.com
