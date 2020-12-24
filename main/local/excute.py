import subprocess
import sys


def excute(command):
    # return bytes data 
    try:
        res = subprocess.run([command],check=True, shell=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        return "Error".encode()
    res = res.stdout
    return res

if __name__ == "__main__":
    res = excute('ls /Application')
    print(res.decode())
