"""
Python script to install Ansible
"""

import subprocess

def install_ansible():
    """
    The function installs Ansible on the machine
    """
    try:
        # Download get-pip.py
        print("Downloading get-pip.py...")
        download_pip = subprocess.run(
            ['wget https://bootstrap.pypa.io/get-pip.py'], 
            shell=True, capture_output=True, text=True
        )
        print(download_pip.stdout)
        if download_pip.returncode != 0:
            print(f"Failed to download get-pip.py: {download_pip.stderr}")
            return

        # Run the get-pip.py script
        print("Running get-pip.py...")
        run_pip_script = subprocess.run(
            ['python3 get-pip.py'], 
            shell=True, capture_output=True, text=True
        )
        print(run_pip_script.stdout)
        if run_pip_script.returncode != 0:
            print(f"Failed to run get-pip.py: {run_pip_script.stderr}")
            return

        # Install Ansible
        print("Installing Ansible...")
        install_ansible = subprocess.run(
            ['python3 -m pip install ansible'], 
            shell=True, capture_output=True, text=True
        )
        print(install_ansible.stdout)
        if install_ansible.returncode != 0:
            print(f"Failed to install Ansible: {install_ansible.stderr}")
            return

        # Upgrade Ansible
        print("Upgrading Ansible...")
        upgrade_ansible = subprocess.run(
            ['python3 -m pip install --upgrade ansible'], 
            shell=True, capture_output=True, text=True
        )
        print(upgrade_ansible.stdout)
        if upgrade_ansible.returncode != 0:
            print(f"Failed to upgrade Ansible: {upgrade_ansible.stderr}")
            return

        print("Ansible installation completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e.stderr}")

if __name__ == "__main__":
    install_ansible()
