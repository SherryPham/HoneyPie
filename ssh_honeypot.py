import logging
from logging.handlers import RotatingFileHandler
import socket
import paramiko

# Constant
logging_format = logging.Formatter('%(message)s')

# Logger and Logging Files
funnel_logger = logging.getLogger('FunnelLogger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

creds_logger = logging.getLogger('CredsLogger')
creds_logger.setLevel(logging.INFO)
creds_handler = RotatingFileHandler('cmd_audits.log', maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(creds_handler)

# Emulated Shell
def emulated_shell(channel, client_ip):
    channel.send(b'corporate-jumpbox2$ ')
    command = b""
    while True:
        char = channel.recv(1)
        channel.send(char)
        if not char:
            channel.close()

        command += char

        if char == b'\r':
            if command.strip() == b'exit':
                response = b'\n Goodbye!\n'
                channel.close()
            elif command.strip() == b'pwd':
                response = b'\\usr\\local' + b'\r\n'
            elif command.strip() == b'whoami':
                response = b"\n" + b"corpuser1" + b"\r\n"
            elif command.strip() == b'ls':
                response = b'\n' + b'jumpbox1.conf' + b'\r\n'
            elif command.strip() == b'cat jumpbox1.conf':
                response = b'\n' + b'Go to deeboodah.com' + b'\r\n'
            else:
                response = b"\n" + bytes(command.strip()) + b"\r\n"

        channel.send(response)
        channel.send(b'corporate-jumpbox2$ ')
        command = b""



