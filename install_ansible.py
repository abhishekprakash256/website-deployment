"""
Python script to install Ansible
"""

import subprocess

def install_ansible():
    """
    The function installs Ansible on the machine
    """
    try:

        # Run the get-pip.py script
        print("Running get pipx...")
        run_pip_script = subprocess.run(
            ['sudo apt install pipx'], 
            shell=True, capture_output=True, text=True
        )

        print(run_pip_script.stdout)
        if run_pip_script.returncode != 0:
            print(f"Failed to run get-pip.py: {run_pip_script.stderr}")
            return
        
        # Install Ansible
        print("Installing Ansible...")
        install_ansible = subprocess.run(
            ['pipx install --include-deps ansible'], 
            shell=True, capture_output=True, text=True
        )
        print(install_ansible.stdout)
        if install_ansible.returncode != 0:
            print(f"Failed to install Ansible: {install_ansible.stderr}")
            return


        print("Ansible installation completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e.stderr}")

if __name__ == "__main__":
    install_ansible()
