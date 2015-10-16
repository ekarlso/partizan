#Create db

mysql -uroot -prootp4ss -e 'CREATE DATABASE partizan'

# Sync
partizan-manage --config-file etc/partizan.ini database upgrade
