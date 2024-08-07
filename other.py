import random
from loguru import logger
from sys import stderr
import time
import web3


def wallet_reader(shuffle):
    with open('data/wallets.txt') as file:
        if shuffle:
            accounts = [i.strip() for i in file]
            random.shuffle(accounts)
            return accounts, len(accounts)
        else:
            return [i.strip() for i in file], len([i.strip() for i in file])


def add_logger():
    logger.remove()

    logger.add(
        stderr, diagnose=True,
        format="<bold><blue>{time:HH:mm:ss}</blue> | <level>{level: <8}</level> | <level>{message}</level></bold>"
    )
    logger.add(sink='./log/logfile.log', rotation="50 MB")

    return logger



def clear_file(path):
    with open(path, 'w'):
        pass


def write_success(self=None, data=None):
    with open('result/good proxy.txt', 'a+') as file:
        file.write(f'{data}\n')


def write_failer(self=None, data=None):
    with open('result/bad proxy.txt', 'a+') as file:
        file.write(f'{data}\n')


def interface(_len):

    print(
        f"""\033[36m   Developed by @Irorsss \033[m\033[96m
        
Total proxy loaded: {_len}
\033[m """
    )

    print()
    time.sleep(2)

