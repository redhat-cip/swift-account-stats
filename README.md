Swift-account-stats
===================

swist-account-stats is a tool to report a bunch of statistics
on swift usage at tenant level and global level.
The tenant used to query all swift account must be configured
to own the ResellerAdmin role in keystone.

For tenant (account) level the given stats are as follow:

 - account_size
 - container_amount
 - container_max_size
 - container_min_size
 - container_avg_size

And for each containers:

 - container_size
 - object_amount
 - object_max_size
 - object_min_size
 - object_avg_size

For the global level the given are :

- account_amount
- account_max_size
- account_min_size
- account_avg_size
- total_size
- container_amount
- container_max_size
- container_min_size
- container_avg_size
- object_amount
- object_max_size
- object_min_size
- object_avg_size

The script outputs results in CSV format on files or
to the standart output.

Usage
-----

To get the global usage, the '-r' option returns :

    $ swift-account-stats http://192.168.56.101:5000/v2.0/ admin:admin wxcvbn
    account_amount,account_max_size,account_min_size,account_avg_size,total_size,container_amount,container_max_size,container_min_size,container_avg_size,object_amount,object_max_size,object_min_size,object_avg_size
    14,0B,0B,0B,0B,30,17K,1K,11K,60,17K,0B,5K
    $ swift-account-stats -r http://192.168.56.101:5000/v2.0/ admin:admin wxcvbn
    account_amount,account_max_size,account_min_size,account_avg_size,total_size,container_amount,container_max_size,container_min_size,container_avg_size,object_amount,object_max_size,object_min_size,object_avg_size
    14,0,0,0,0,30,17438,1358,11332,60,17438,0,5666

To get a detailed usage by tenant (account) :

    $ swift-account-stats -d http://192.168.56.101:5000/v2.0/ admin:admin wxcvbn
    email,account_name,account_id,account_size,container_amount,container_max_size,container_min_size,container_avg_size,container_name,container_size,object_amount,object_max_size,object_min_size,object_avg_size
    tata@toto.com,tenant2,e02c6f7d776847e59aef46b93617e94f,15M,5,5M,1M,3M,container0,1M,1,1M,1M,1M
    tata@toto.com,tenant2,e02c6f7d776847e59aef46b93617e94f,15M,5,5M,1M,3M,container1,2M,1,2M,2M,2M
    tata@toto.com,tenant2,e02c6f7d776847e59aef46b93617e94f,15M,5,5M,1M,3M,container2,3M,1,3M,3M,3M
    tata@toto.com,tenant2,e02c6f7d776847e59aef46b93617e94f,15M,5,5M,1M,3M,container3,4M,1,4M,4M,4M
    tata@toto.com,tenant2,e02c6f7d776847e59aef46b93617e94f,15M,5,5M,1M,3M,container4,5M,1,5M,5M,5M
    titi@toto.com,tenant1,f11eba6f05e643abadb030dc9ddb5e4a,15M,5,5M,1M,3M,container0,1M,1,1M,1M,1M
    titi@toto.com,tenant1,f11eba6f05e643abadb030dc9ddb5e4a,15M,5,5M,1M,3M,container1,2M,1,2M,2M,2M
    titi@toto.com,tenant1,f11eba6f05e643abadb030dc9ddb5e4a,15M,5,5M,1M,3M,container2,3M,1,3M,3M,3M
    titi@toto.com,tenant1,f11eba6f05e643abadb030dc9ddb5e4a,15M,5,5M,1M,3M,container3,4M,1,4M,4M,4M
    titi@toto.com,tenant1,f11eba6f05e643abadb030dc9ddb5e4a,15M,5,5M,1M,3M,container4,5M,1,5M,5M,5M


To limit the statistics to a list of tenants (names or ids), use the "--tenants" options :

    $ swift-account-stats http://localhost:5000/v2.0/ admin:admin admin --tenants TestTenant1,0ae3843b392dff3a
    account_amount,account_max_size,account_min_size,account_avg_size,total_size,container_amount,container_max_size,container_min_size,container_avg_size,object_amount,object_max_size,object_min_size,object_avg_size
    2,70M,20M,45M,90M,3,45M,20M,30M,6,20M,10M,15M

The --tenants option can be used with the other options, like -r or -d.

The '--file-path' option can be used to export results in a CSV file.
