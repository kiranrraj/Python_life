import subprocess

# subprocess.call('dir', shell=True)
output = subprocess.check_output('dir', shell=True)
print(f'Have {len(output)} bytes in output')
print(type(output))