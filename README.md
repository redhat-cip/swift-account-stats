Swift-account-stat
==================

swist-acount-stat is a tool to report a bunch of stat
on swift usage at tenant level and global level.
The tenant used to query all swift account must be configured
to own the ResellerAdmin role in keystone.

For tenant (account) level the given stats are as follow:

 - container_amount
 - container_max_size
 - container_min_size
 - container_avg_size

And for each containers:

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
 account_name,container_amount,container_max_size,container_min_size,container_avg_size,container_name,object_amount,object_max_size,object_min_size,object_avg_size
 account_FIOKXEC4,3,16K,5K,12K,container_I1PECAGR,2,16K,0B,8K
 account_FIOKXEC4,3,16K,5K,12K,container_NKS4CB7R s,2,15K,0B,7K
 account_FIOKXEC4,3,16K,5K,12K,container_SEJV2ZGJ_ʶͰΏ,2,5K,0B,2K
 account_B4WAH0OS,3,16K,3K,11K,container_8KPQC7FJ,2,15K,0B,7K
 account_B4WAH0OS,3,16K,3K,11K,container_A7PJ60OL_ѪÆř,2,16K,0B,8K
 account_B4WAH0OS,3,16K,3K,11K,container_RZFXL9XE s,2,3K,0B,1K
 account_F1DWWVK6,3,14K,5K,8K,container_GOX0KRPI_ϪѪÆ,2,6K,0B,3K
 account_F1DWWVK6,3,14K,5K,8K,container_HJQLQC1Q,2,14K,0B,7K
 account_F1DWWVK6,3,14K,5K,8K,container_NSYWSYRF s,2,5K,0B,2K
 account_63TJQORI,3,17K,1K,11K,container_3STOBY0O_řɧÆ,2,17K,0B,8K
 account_63TJQORI,3,17K,1K,11K,container_C409F1OW s,2,14K,0B,7K
 account_63TJQORI,3,17K,1K,11K,container_U8U3EVI9,2,1K,0B,679B
 account_O1LO7CYR,3,12K,2K,8K,container_5EPFN697,2,2K,0B,1K

The '--file-path' option can be use to export results in a CSV file.
