# 0x06. Regular Expression

## Overview

This project introduces the basics and advanced usage of regular expressions (regex) using the Oniguruma library, which is commonly utilized by Ruby. Participants will learn to construct and apply regexes to solve pattern matching problems effectively.

## Background Context

Regular expressions are a powerful tool for processing text. This project uses Ruby scripts to test regexes, focusing on constructing patterns that match specific criteria. The goal is to familiarize participants with regex syntax and its practical applications in real-world scenarios.

## Learning Objectives

By the end of this project, participants should be able to:

- Construct regular expressions using the Oniguruma library.
- Understand basic and advanced regex concepts.
- Apply regexes to filter and extract data from text.
- Use Ruby scripts to test and validate regex patterns.

## Resources

- **Reading:**
  - [Regular expressions - basics](#)
  - [Regular expressions - advanced](#)
  - [Rubular is your best friend](http://rubular.com)
  - [Use a regular expression against a problem: now you have 2 problems](#)
  - [Learn Regular Expressions with simple, interactive exercises](#)

## Requirements

### General

- **Environment:** All scripts will be interpreted on Ubuntu 20.04 LTS.
- **Script Guidelines:**
  - The first line of all Ruby scripts must be `#!/usr/bin/env ruby` to ensure they are executed using Ruby.
  - Scripts must end with a new line.
  - Scripts must be executable (`chmod +x file`).
  - Regex must be compatible with the Oniguruma library, as this is the standard for Ruby.

### Documentation

- **Project Description:** A README.md file at the root of the folder of this project, explaining the functionality and purpose of each script.

## Example Usage

```ruby
# example.rb: Ruby script to test regular expressions
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join

# Run the script with a test IP address
./example.rb 127.0.0.2  # Outputs: 127.0.0.2
./example.rb 127.0.0.1  # Outputs: 127.0.0.1
./example.rb 127.0.0.a  # Outputs nothing due to regex filter
