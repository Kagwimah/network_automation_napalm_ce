==================================================================
This is a basic python script for network automation using napalm library.
The script is meant to interact with huawei devices via ssh.

Requires:
Three files in the same folder as the script.
i. device_credential.txt -> contains the user login details:
    Example:
   
    username huawei_user
    password Huawei_password
ii. command_file.txt -> contains user defined commands to be executed by the script.
    Example:
    display ip int brief
    command_two
    command_three
iii. inventory file added
     hostname 10.10.10.10
     hostname 10.10.10.10

author: James.kagwima
version: v1.0

==================================================================