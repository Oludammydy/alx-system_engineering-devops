# Installs flask from pip3, version 2.1.0

exec { 'install flask':
  command => 'sudo pip3 install flask -v 2.1.0',
  path    => '/usr/bin'
}
