# 0x13. Firewall

## Overview

This DevOps, SysAdmin, and Security project focuses on implementing and configuring firewall settings to secure web servers. The project period is from May 13, 2024, 6:00 AM to May 14, 2024, 6:00 AM.

## Concepts

The primary concept for this project is **Web stack debugging**. It's essential to ensure your servers are protected behind a firewall to prevent unauthorized access.

## Resources

**Read or watch:**
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))

## More Info

Utilize tools like `telnet` to check if specific ports are open (e.g., `telnet IP PORT`). It's a practical approach for debugging socket communications between software components.

**Warning:** Do not use containers on demand for this project due to Docker container limitations. Also, be cautious with firewall rules, especially with SSH (port 22), to avoid locking yourself out of your server.

## Tasks

### 0. Block all incoming traffic but

**Requirements:**
- Install and configure UFW on web-01 to block all incoming traffic except on ports 22 (SSH), 443 (HTTPS), and 80 (HTTP).
- Share the UFW commands used in your answer file.

**File:** `0-block_all_incoming_traffic_but`

### 1. Port forwarding

**Requirements:**
- Configure the firewall on web-01 to redirect traffic from port 8080/TCP to port 80/TCP.
- Your answer file should include the modified UFW configuration file.

**File:** `100-port_forwarding`

**Repository:**
- **GitHub repository:** alx-system_engineering-devops
- **Directory:** 0x13-firewall
