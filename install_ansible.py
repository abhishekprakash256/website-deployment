"""
Python script to install ansible
"""

import subprocess
import os

def install_ansible():
    """
    The function of install ansible on the machine
    """
    #install pip
    install_pip = subprocess.run(['wget https://bootstrap.pypa.io/get-pip.py'], shell=True, capture_output=True, text=True, check=True)

    #install ansible
    install_pip = subprocess.run(['python3 -m pip install ansible'], shell=True, capture_output=True, text=True, check=True)

    #upgrade pip
    upgrade_ansible = subprocess.run(['python3 -m pip install --upgrade ansible'], shell=True, capture_output=True, text=True, check=True)



if __name__ == "__main__":
    install_ansible()





