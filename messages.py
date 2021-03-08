from colorama import init
from termcolor import colored, cprint
from pyfiglet import figlet_format
init()


# https://pypi.org/project/termcolor/


def msg_start(x):
    cprint(figlet_format(x, font='rectangles'), 'green')
    return None


def msg_grey_on_yellow(x):
    cprint(x, 'grey', 'on_yellow', end=' ')
    return None


def msg_grey_on_cyan(x):
    cprint(x, 'grey', 'on_cyan', end=' ')
    return None


def msg_grey_on_red(x):
    cprint(x, 'grey', 'on_red')
    return None


def msg_green_on_yellow(x):
    cprint(x, 'green', 'on_yellow')
    return None


def msg_grey_on_white(x):
    cprint(x, 'grey', 'on_white')
    return None


def msg_error(x):
    cprint(x, 'red', attrs=['bold'])
    return None


def msg_status(x):
    cprint(x, 'magenta', 'on_grey')
    return None


def msg_win(x):
    cprint(figlet_format(x, font='starwars'), 'green', attrs=['bold'])
    return None


def msg_success(x):
    cprint(x, 'grey', 'on_green', attrs=['bold'])
    return None


