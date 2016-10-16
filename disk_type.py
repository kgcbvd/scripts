import os
import json

disks = os.popen("sg_map |awk '{print $1'}").read()
disks = disks.split("\n")

devtypes = ('sat', 'scsi', 'ata')
data = {}
data["data"] = []
for disk in disks:
    for dev_type in devtypes:
        dev_name_type = {}
        if disk and dev_type:
            line = 'smartctl -d {0} -a {1} > /dev/null'.format(dev_type, disk)
            exit_code = os.system(line)
            if not exit_code:
                dev_name_type["{#DEVNAME}"] = disk
                dev_name_type["{#DEVTYPE}"] = dev_type
        data["data"].append(dev_name_type)

print(json.dumps(data))

