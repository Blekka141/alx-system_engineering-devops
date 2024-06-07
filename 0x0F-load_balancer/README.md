# 0x0F. Load Balancer

## Background Context

In this project, we aim to enhance our web infrastructure by adding redundancy to our web servers. This approach not only allows handling increased traffic by doubling the number of web servers but also enhances the reliability of the infrastructure. With two web servers, if one fails, the other can still manage the requests. This setup involves the use of load balancers to distribute incoming traffic evenly across the servers.

You have been provided with two additional servers:
- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

## Project Objectives

- Configure a load balancer using HAProxy.
- Automate configuration and deployment using Bash scripts.
- Ensure high availability and load balancing of web traffic across multiple servers.

## Resources

- [Introduction to Load Balancing and HAProxy](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Requirements

### General

- **Allowed editors:** vi, vim, emacs
- **Environment:** All scripts will be tested on Ubuntu 16.04 LTS
- **Documentation:** A README.md file at the root of the project folder is mandatory
- **Scripting files:** Must be executable Bash scripts
- **Code style:** All Bash scripts must pass Shellcheck (version 0.3.7) without any errors
- **Script headers:** 
  - The first line must be `#!/usr/bin/env bash`
  - The second line must contain a comment describing the script's functionality

## Setup and Configuration

Each script in the repository is tailored to automate specific tasks in the setup and maintenance of the load balancer and web servers. Detailed instructions for each script are provided within the script files themselves.

## Usage

Scripts should be run on the servers where they are intended to execute. For example, configuration scripts for the load balancer should run on `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
