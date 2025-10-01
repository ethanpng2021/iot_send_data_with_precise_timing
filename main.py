import pandas
import time
import socket
from datetime import datetime, timedelta


UDP_IP = "192.168.0.115"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"


def add_seconds_to_datetime(dt, seconds):
    """
    Add a specified number of seconds to a datetime object.

    Args:
        dt (datetime): The datetime object to which seconds will be added.
        seconds (int): The number of seconds to add.

    Returns:
        datetime: The resulting datetime object.
    """
    return dt + timedelta(seconds=seconds)

ticktock = 5
current_datetime = datetime.now()
while True:

    print("main.py send flag to db")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    #current_datetime = datetime(2023, 9, 10, 12, 0, 0)  # Replace with your desired datetime
    
    #duration_seconds = 3600  # Replace with your desired duration in seconds
    
    
    result_datetime = add_seconds_to_datetime(current_datetime, ticktock)
    print(result_datetime)
    current_datetime = result_datetime
    time.sleep(5)
