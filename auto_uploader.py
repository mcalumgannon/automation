import datetime
import subprocess
import time
import random

random_number = random.randint(1,6)
for i in range(random_number):
    file = open(r'C:\Users\nitro\OneDrive\Documents\computing\python\python_functional\time_to_text\text.txt', 'a')

    file.write(f'{datetime.datetime.now()} - The script ran \n')

    time.sleep(5)


    commands = ['git add text.txt', 'git commit -m "first"', 'git branch -M main', 'git push -u origin main']

    for command in commands:
        # PowerShell command to execute
        powershell_command = command

        # Run the PowerShell command
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

        # Check the result
        if result.returncode == 0:
            print("PowerShell command executed successfully.")
            pass
        else:
            print("Error executing PowerShell command.")
            pass
