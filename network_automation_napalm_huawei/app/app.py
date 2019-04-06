from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException
from datetime import datetime
import csv
from napalm_ce import ce
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')


# read  login details from a file.
def read_device_credentials(filename):
    # expected format:  "hostname='10.240.0.4', username='hwuser', password="Hq3lab@123", timeout=15"
    commands = {}
    try:
        with open(filename) as fh:
            for line in fh:
                command, description = line.strip().split(' ', 1)
                commands[command] = description.strip()

            # host = "{}='{}'".format('hostname', commands['hostname'])
            # user = "{}='{}'".format('username', commands['username'])
            # user_password = "{}='{}'".format('password', commands['password'])
            # timeout = "{}={}".format('timeout', int(commands['timeout']))
            # login_details = "{}, {}, {}, {}".format(host, user, user_password, timeout)
    except FileNotFoundError as error:
        print("No such file or directory: 'device_credential.txt'")
        with open("errors.txt", 'a') as the_file:
            the_file.write("{}: No such file or directory: 'device_credential.txt'\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    return commands


# read commands to be executed from a file
def read_user_commands(filename):
    commands = ''
    try:
        # read the user commands to be executed
        with open(filename) as f:
            commands = f.read().splitlines()
    except FileNotFoundError as error:
        print("No such file or directory: 'command_file.txt'")
        with open("errors.txt", 'a') as the_file:
            the_file.write("{}: No such file or directory: 'command_file.txt'\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    return commands


# save to file
def save_to_file(text_to_write, file_name):

    w = csv.writer(open(file_name, "w"))
    for key, val in text_to_write.items():
        w.writerow([key, val])


def run():
    print("Please wait, the script is running...")
    try:
        driver = get_network_driver("ce")
        login_credentials = read_device_credentials("device_credential.txt")
        # device_credential.txt file must not be empty
        if len(login_credentials) > 0:
            device = driver(hostname='{}'.format(login_credentials['hostname']),
                            username='{}'.format(login_credentials['username']),
                            password='{}'.format(login_credentials['password']),
                            timeout=int(login_credentials['timeout']))
            device.open()

            commands_to_send = read_user_commands('command_file.txt')
            # commands_to_send file must not be empty.
            if commands_to_send is not '':
                output = device.cli(commands_to_send)
                output_file = "output_{}.csv".format(str(login_credentials['hostname']))
                print("Script executed successfully.\n")
                print("Output file : output_{}.csv".format(str(login_credentials['hostname'])))
                save_to_file(output, output_file)
                # with open("output_{}.txt".format(str(login_credentials['hostname'])), 'a') as the_file:
                #     the_file.write(str(output))
            device.close()
    except ConnectionException as e:
        print("Timeout Error.", e)
        with open("conn_errors.txt", 'a') as the_file:
            the_file.write("connection failed. \n")


