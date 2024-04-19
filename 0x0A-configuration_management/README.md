
# 0x0A. Configuration Management

## Background Context

During my time at SlideShare, I worked on an auto-remediation tool called Skynet. Skynet monitored, scaled, and fixed Cloud infrastructure using a parallel job-execution system called MCollective. This system allowed me to execute commands to one or multiple servers simultaneously, applying actions based on filters such as server hostname or metadata like server type and environment. However, a bug in my code caused nil to be sent to the filter method.

There were two significant issues:

1. When MCollective receives nil as an argument for its filter method, it interprets it as 'all servers'.
2. The action I sent was to terminate the selected servers.

As a result, I unintentionally shut down 75% of SlideShare's conversion infrastructure, rendering users unable to convert their documents.

Fortunately, with the help of Puppet, we were able to restore our infrastructure in under an hour. Imagine the time and effort it would have taken if we had to do everything manually.

Writing Puppet code for infrastructure requires an investment of time and energy, but it's a crucial aspect for maintaining complex systems in the long term.

[Source](https://twitter.com/devopsreact/status/836971570136375296)

## Resources

### Read or Watch:

- [Intro to Configuration Management](https://example.com)
- [Puppet resource type: file](https://example.com) (check "Resource types" for all manifest types in the left menu)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://example.com)
- [Puppet lint](https://example.com)
- [Puppet emacs mode](https://example.com)

## Requirements

### General

- All files will be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifest files must end with the extension `.pp`.

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

#### Install puppet

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://example.com)

#### Install puppet-lint

```
$ gem install puppet-lint
```
