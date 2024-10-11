import re
import subprocess


def IPAddress():
    data = subprocess.getoutput("ifconfig")
    allIp = re.findall(r"inet [.\d]+", data)

    if allIp:
        if len(allIp) == 3:
            address = re.match(r"inet ([.\d]+)", allIp[0]).group(1)

        else:
            address = re.match(r"inet ([.\d]+)", allIp[0]).group(1)

    return address
