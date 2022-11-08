# sets file limits for holberton user
exec { 'sets file limits':
  provider => shell,
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/" /etc/security/limits.conf; \
sed -i "s/holberton soft nofile 4/holberton soft nofile 50000/" /etc/security/limits.conf'
}