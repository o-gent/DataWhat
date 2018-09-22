from pycli import cli
from datawhat import datawhat

cli = cli()

def add(*args):
    l = 0
    for i in args: l += i
    return l

cli.add_func(add)
usr = ['put_usr_here']
datawhat = datawhat(usr, cli)
datawhat.send_message('hello, type /help for list of functions, start each command with /')
datawhat.send_message("arguments follow the command by '>' and are seperated by commas, for example:     /add>60,9")

while True:
    datawhat.command_input()