from _datetime import datetime
log_file = 'menu.log'


def log(msg):
    """
    Save a message in a log file {log_file} and prints it in the console
    :param msg: the message to be append in the log file
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:M%:%S')
    formatted= f'{timestamp} - {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')

