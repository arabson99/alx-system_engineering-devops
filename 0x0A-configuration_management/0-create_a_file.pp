# The puppet manifest that creates a file school in /tmp.
# The file School has permission 0744, belonging to the user and group www-data.
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
