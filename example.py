from pycli import cli
from datawhat import datawhat
from datawhat import despacito


def add(*args):
    l = 0
    for i in args: l += i
    return l


cli = cli()
cli.add_func(add)
cli.add_func(despacito)


usr = ['user_here']
datawhat = datawhat(usr, cli)
datawhat.send_message('hello, type /help for list of functions, start each command with /')
datawhat.send_message("arguments follow the command by '>' and are seperated by commas, for example:     /add>60,9")

while True:
    datawhat.command_input()