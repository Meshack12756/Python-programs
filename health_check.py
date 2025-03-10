import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage()
    free = du.free / du.total * 100

    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percentage(1)
    
    return usage > 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Your PC needs REAL System check!!")
else:
    print("Your PC is Healthy and REAL good!!")
