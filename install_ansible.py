"""
Python script to install ansible
"""

import subprocess
import os

def install_ansible():
    """
    The function installs Ansible on the machine
    """
    try:
        # Download get-pip.py
        download_pip = subprocess.run(
            ['wget https://bootstrap.pypa.io/get-pip.py'], 
            shell=True, capture_output=True, text=True, check=True
        )
        print(download_pip.stdout)

        # Run the get-pip.py script
        run_pip_script = subprocess.run(
            ['sudo apt install python3-pip'], 
            shell=True, capture_output=True, text=True, check=True
        )
        print(run_pip_script.stdout)

        # Install Ansible
        install_ansible = subprocess.run(
            ['python3 -m pip install ansible'], 
            shell=True, capture_output=True, text=True, check=True
        )
        print(install_ansible.stdout)

        # Upgrade Ansible
        upgrade_ansible = subprocess.run(
            ['python3 -m pip install --upgrade ansible'], 
            shell=True, capture_output=True, text=True, check=True
        )
        print(upgrade_ansible.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e.stderr}")
        raise

if __name__ == "__main__":
    install_ansible()






