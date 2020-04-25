import os
from pprint import pprint


def my_apps():
    apt_programs = [
        'ubuntu-restricted-extras',
        'build-essential checkinstall',
        'wireshark',
        'libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev',
        'vlc',
        'gimp',
        'putty',
        'curl',
        'wget',
        'remmina',
        'kdenlive',
        'darktable',
        'Gdebi',
        'ufw',
        'neofetch',
        'git',
        'unity-tweak-tool',
        'nautilus-dropbox'
    ]
    print()
    print('INSTALLING YOUR APT apps...')
    print('*' * 80)
    os.system('sudo apt-get update && sudo apt-get upgrade -y')
    for app in apt_programs:
        print('*' * 80)
        print(f'INSTALLING {app}...')
        print('*' * 80)
        os.system(f'sudo apt-get install {app} -y')
        print()
    os.system('sudo apt-get autoremove -y')
    print()
    print('YOUR APT APPS HAVE BEEN INSTALLED')
    print()
    input('PRESS ENTER KEY TO CONTINUE...')


def my_snap():
    snap_app = [
        'snap-store',
        'notepad-plus-plus',
        'brave',
        'shotcut -- classic',
        'obs-studio'        
    ]
    print()
    print('INSTALLING YOUR SNAP APPS...')
    print('*' * 80)
    for app in snap_app:
        os.system(f'sudo snap install {app}')
        print('*' * 80)
    print()
    print('YOUR SNAP APPS HAVE BEEN INSTALLED')
    print()
    input('PRESS ENTER KEY TO CONTINUE...')


def my_downloads():
    deb_list = [
        'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
        'wget http://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/9080/wps-office_11.1.0.9080.XA_amd64.deb > ~/Downloads/wps-office_11.1.0.9080.XA_amd64.deb',
        'wget https://github.com/balena-io/etcher/releases/download/v1.5.76/balena-etcher-electron-1.5.76-linux-ia32.zip > ~/Downloads/etcher.zip',
        'wget https://dl2.cdn.filezilla-project.org/client/FileZilla_3.47.2.1_x86_64-linux-gnu.tar.bz > ~/Downloads/FileZilla_3.47.2.1_x86_64-linux-gnu.tar.bz',
        'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > ~/Downloads/google-chrome-stable_current_amd64.deb'
        ]
    print()
    print('DOWNLOADING YOUR APPS...')
    print('*' * 80)
    for app in deb_list:
        os.system(f'sudo {app}')
        print('*' * 80)
    print()
    print('YOUR APPS HAVE BEEN DOWNLOADED')
    
    print()
    input('PRESS ENTER KEY TO CONTINUE...')


def install_external_apps():
    external_app = {
        'gns3': [
            'sudo add-apt-repository ppa:gns3/ppa',
            'sudo apt update',
            'sudo apt install gns3-gui gns3-server'
        ],
        'vscode': [
            'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg',
            'sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg',
            "sudo sh -c 'echo 'deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main' > /etc/apt/sources.list.d/vscode.list",
            'sudo apt update',
            'sudo apt install code'
        ],
        'vmware_workstation': [
            'wget -O ~/vmware.bin https://www.vmware.com/go/getWorkstation-linux',
            'sudo apt install build-essential',
            'sudo bash ~/vmware.bin'
        ],
        'openshot': [
            'sudo add-apt-repository ppa:openshot.developers/ppa',
            'sudo apt update',
            'sudo apt install openshot-qt'
        ],
        'ubuntu-cleaner':[
            'sudo add-apt-repository ppa:gerardpuig/ppa',
            'sudo apt-get update',
            'sudo apt-get install ubuntu-cleaner'
        ],
        'simplescreenrecorder':[
            'sudo add-apt-repository ppa:marten-baert/simplescreenrecorder',
            'sudo apt-get update',
            'sudo apt-get install simplescreenrecorder'
        ],
        'Stacer':[
            'sudo add-apt-repository ppa:oguzhaninan/stacer',
            'sudo apt-get update',
            'sudo apt-get install stacer'
        ]
    }

    print()
    print('INSTALLING YOUR REPO(s) AND APPS...')
    print('*' * 80)
    for app, lines in external_app.items():
        print(f'INSTALLING {app}')
        print('*' * 80)
        print()
        for line in lines:
            os.system(line)
            print('*' * 80)
        print()
    print()
    print('YOUR REPO(s) AND APPS ARE INSTALLED')
    print()
    input('PRESS ENTER KEY TO CONTINUE...')


if __name__ == "__main__":
    my_apps()
    my_snap()
    my_downloads()
    install_external_apps()
    os.system('sudo apt-get update -y && sudo apt-get autoremove')
    print()
    print('CONGRATS!!! ALL YOUR REQUESTED APPS ARE INSTALLED AND UPDATED')