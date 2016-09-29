#!/usr/bin/env python
# coding: utf8
#
# ./random-passwd.py -n 6 [-P -D -L -U]
#

import click
import string, random

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-n", "--len", default=6, type=int, help="length of random password", show_default=True, metavar='LEN')
@click.option("-p/-P", "punct", default=True, help="include punctuation or not")
@click.option("-d/-D", "digit", default=True, help="include digits or not")
@click.option("-l/-L", "lower", default=True, help="include lowercase or not")
@click.option("-u/-U", "upper", default=True, help="include uppercase or not")
@click.version_option("0.2")
def gen_random_passwd(**kwargs):
    """随机密码生成工具-Python版"""
    print kwargs
    include_chars = ""
    if kwargs.get("punct"): include_chars += string.punctuation
    if kwargs.get("digit"): include_chars += string.digits
    if kwargs.get("lower"): include_chars += string.lowercase
    if kwargs.get("upper"): include_chars += string.uppercase

    if not include_chars:
        click.secho("不能同时使用-D -U -L -P这4个选项!", err=True, fg="red")
        exit(2)

    randpass = ""
    for _ in range(kwargs.get("len")):
        randpass += random.choice(include_chars)

    print randpass

if __name__ == "__main__":
    gen_random_passwd()
