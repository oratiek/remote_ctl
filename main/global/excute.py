import subprocess
import sys


def excute(command):
    # return bytes data 
    res = subprocess.run([command],check=True, shell=True, stdout=subprocess.PIPE)
    res = res.stdout
    return res

if __name__ == "__main__":
    excute('ls')
