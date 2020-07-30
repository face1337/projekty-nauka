#! python 3
# pw.py - a insecure password locker program
import sys, pyperclip

PASSWORDS = {'email': 'B\K6O$=edb.pyRXc',
             'facebook': 'Q^or)EfRAiLBWw!6',
             'YouTube': 'y3>KFW_Sj<\mN~Z@'}


if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard.')
else:
    print('THere is no account named ' + account)
