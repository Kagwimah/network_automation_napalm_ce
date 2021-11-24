
# read  login details from a file.
def read_device_credentials(filename):
    # expected format:  "hostname='10.240.0.4', username='hwuser', password="Password@123", timeout=15"
    commands = {}
    print(len(commands))
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(' ', 1)
            commands[command] = description.strip()

        # host = "{}='{}'".format('hostname', commands['hostname'])
        # user = "{}='{}'".format('username', commands['username'])
        # user_password = "{}='{}'".format('password', commands['password'])
        # timeout = "{}={}".format('timeout', int(commands['timeout']))
        # print(timeout)
        # login_details = "{}, {}, {}, {}".format(host, user, user_password, timeout)

    return commands

# login_credentials = read_device_credentials("device_credential.txt")
# print(login_credentials['timeout'])

#
# if 'hostname' or 'ip' in command:
#     host = "{}='{}'".format(command, description)
#     print(host)
# if 'username' or 'user' in command:
#     user = "{}='{}'".format(command, description)
#     print(user)


def read_inventory_file(filename):
    hosts = []
    with open(filename) as fh:
        for line in fh:
            hostname, ip_address = line.strip().split(' ', 1)
            hosts.append(ip_address)

    return hosts


b= read_inventory_file("../inventory.txt")

for ip in b:
    print(
    'hostname = {}'.format(ip)
    )
