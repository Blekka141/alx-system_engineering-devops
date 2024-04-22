# create a process named killmenow 

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/local/bin:/usr/bin:/bin',
  onlyif      => 'pgrep killmenow',
}