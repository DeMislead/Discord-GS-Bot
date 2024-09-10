import os
import json
from sys import stdout
from subprocess import call, check_output

def load_server_config(server_name):
    """
    Load the server configuration from the JSON file.
    
    :param server_name: Name of the server.
    :return: Dictionary containing the server configuration.
    """
    # Construct the path to the server's JSON file
    config_path = os.path.join('servers', (server_name + '.json'))
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No such file or directory '{config_path}'")
    
    with open(config_path, 'r') as file:
        return json.load(file)
        

def start_application(server_name):
    """
    Start the application using the server configuration.
    
    :param server_name: Name of the server.
    """
    config = load_server_config(server_name)
    command = config['start']
    print(f"Starting {command}")
    call(command, shell=True)

def stop_application(server_name):
    """
    Stop the application using the server configuration.
    
    :param server_name: Name of the server.
    """
    config = load_server_config(server_name)
    command = config['stop']
    print(f"Stopping {command}")
    call(command, shell=True)

def check_status(server_name):
    """
    Check the status of the application using the server configuration.
    
    :param server_name: Name of the server.
    :return: Status message.
    """
    config = load_server_config(server_name)
    status_message = isProcessRunning(config['executable'])
    print(status_message)
    return status_message

def onstarted(server_name):
    """
    Check the status of the application using the server configuration.
    
    :param server_name: Name of the server.
    :return: Status message.
    """
    config = load_server_config(server_name)
    status_message = config['onspawn']
    print(status_message)
    return status_message

def isProcessRunning (processName):
    cmd = 'TASKLIST', '/FI', 'IMAGENAME eq %s' % processName
    output = check_output(cmd).decode(stdout.encoding)
    running = output.strip().split('\r\n')[-1].lower().startswith(processName.lower())

    return 'Server is up and running' if running else 'Server is currently not running.'