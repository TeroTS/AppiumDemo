import subprocess
from subprocess import check_output
import time

status=""
subprocess.call("/bin/launchctl stop teststation.webdriveragent", shell=True)
time.sleep(3)
while(status.find("200 OK") == -1):
  time.sleep(1)
  try:
    status=subprocess.check_output("curl -I -s $DEVICE_URL/status | grep 200", shell=True)
  except subprocess.CalledProcessError:
    pass
  print 'Testing connection...'
print 'ok'  
