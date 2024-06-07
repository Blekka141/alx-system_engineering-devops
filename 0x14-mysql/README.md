# 0x14. MySQL

## Description

This project involves setting up a MySQL database environment with primary-replica configuration, user management, database creation, and backup strategies. It is part of the ALX System Engineering DevOps curriculum.

## Concepts

For this project, the following concepts are essential:

- **How to:** Fresh Reset and Install MySQL 5.7
- **Database administration**
- **Web stack debugging**

## Resources

**Read or watch:**

- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/understanding-mysql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql)
- [Build a robust database backup strategy](https://www.percona.com/blog/2016/10/12/mysql-backup-strategies-and-implementation/)

**Man or help:**

- `mysqldump`

## Learning Objectives

At the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via `apt-get`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Notes

- Ensure MySQL 5.7.x is installed on both `web-01` and `web-02`.
- Make sure to create necessary users and databases as specified.
- Configure primary-replica setup correctly for redundancy and load distribution.
- Implement a reliable backup strategy to safeguard your data.
