import os
from getpass import getpass


def main():

    user = input('Please enter your user email: ')
    name = input('Please enter your name: ')
    pwd = getpass('Password ')
    os.system(f'git config --global user.email "{user}"')
    os.system(f'git config --global user.name "{name}"')
    
    os.system('git status')
    os.system('git add .')
    os.system('git status')
    comment = input('Please enter your update comment: ')
    os.system(f'git commit -m "{comment}"')
    os.system('git push')


if __name__ == "__main__":
    main()