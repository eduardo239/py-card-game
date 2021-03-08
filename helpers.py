from colorama import init
from termcolor import colored, cprint
import sys

init()


def msg_grey_on_yellow(x):
    cprint(x, 'grey', 'on_yellow', end=' ')
    return None


def msg_grey_on_cyan(x):
    cprint(x, 'grey', 'on_cyan', end=' ')
    return None


def msg_black_on_red(x):
    cprint(x, 'grey', 'on_red')
    return None


def msg_error(x):
    cprint(x, 'red', attrs=['bold'])
    return None


def msg_win(x):
    cprint(x, 'green', attrs=['bold'])
    return None


def msg_success(x):
    cprint(x, 'grey', 'on_green', attrs=['bold'])
    return None


