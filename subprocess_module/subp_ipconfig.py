import subprocess

out = subprocess.run('ipconfig', shell=True)
if out.returncode == 0:
    print(f'Command executed with code {out.returncode}')