A file for NoSql functions
Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)
$ sudo mkdir -p /data/db

Or if /etc/init.d/mongod is missing, please find here an example of the file:

Click to expand/hide file contents Use “container-on-demand” to run MongoDB Ask for container Ubuntu 18.04 - MongoDB Connect via SSH Or via the WebTerminal In the container, you should start MongoDB before playing with it:

$ service mongod start

Starting database mongod [ OK ] $ $ cat 0-list_databases | mongo MongoDB shell version v4.2.8 connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") } MongoDB server version: 4.2.8 admin 0.000GB config 0.000GB local 0.000GB bye $
