# 0x17. Web Stack Debugging #3

## DevOps | SysAdmin | Scripting | Debugging

**Project Start:** Jun 4, 2024 6:00 AM  
**Project End:** Jun 6, 2024 6:00 AM  
**Checker Release:** Jun 5, 2024 1:12 PM  
**Auto Review:** At the deadline

## Concepts

For this project, you should be familiar with the following concepts:

- [Web Server](https://intranet.alxswe.com/concepts/17)
- [Web Stack Debugging](https://intranet.alxswe.com/concepts/68)

## Background Context

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In these cases, you will need to go down the stack. The good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, allowing you to run blogs, portfolios, e-commerce, and company websites. It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements

### General

- All your files will be interpreted on Ubuntu 14.04 LTS.
- All your files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## More Info

### Install `puppet-lint`

To install `puppet-lint`, run the following commands:

```sh
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
