==================================================================
This is a basic python script for network automation using napalm library.
The script is meant to interact with huawei devices via ssh.

Requires:
Two files in the same folder as the script.
i. device_credential.txt -> contains the user login details:
    Example:
    hostname 10.10.10.10
    username huawei_user
    password Huawei_password
ii. command_file.txt -> contains user defined commands to be executed by the script.
    Example:
    display ip int brief
    command_two
    command_three

author: James.kagwima
version: v1.0

==================================================================