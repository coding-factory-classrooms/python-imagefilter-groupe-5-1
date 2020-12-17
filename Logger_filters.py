from _datetime import datetime
log_file = 'main.log'


def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:M%:%S')
    formatted= f'{timestamp} - {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')

def dump_log():

    try:
        with open(log_file, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError as error:
        print(error)