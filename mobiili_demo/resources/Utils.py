import subprocess

class Utils(object):

    def send_keys_adb(self, id, text):
        command = "/Users/teststation/teststation/android-sdk/platform-tools/adb -s {} shell input text {}".format(id, text)
        subprocess.call(command, shell=True)