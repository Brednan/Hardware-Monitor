import os
import subprocess

# speed = os.system(r'wmic cpu get CurrentClockSpeed')
speed = subprocess.check_output(["powershell", r'Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance"'])
print(speed)
