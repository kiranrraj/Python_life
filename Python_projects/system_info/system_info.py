import subprocess

details = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
info_list = []

for detail in details:
    info_list.append(str(detail.strip()))

for info in info_list:
    print(info)

for detail in details:
    info_list.append(str(detail.split("\r")[:-1]))

for info in info_list:
    print(info[2:-2])