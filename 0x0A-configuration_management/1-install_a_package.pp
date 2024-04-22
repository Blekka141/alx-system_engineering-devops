#!/usr/bin/pup
# Install Flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/local/bin/flask --version | grep -q "2.1.0"',
  require => Package['python3-pip'],
}