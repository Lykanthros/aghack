import psutil
import os

def stop_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.terminate()
            break

def stop_pguard_pncclient():
    os.system("sc config pncService start=disabled")
    os.system("net stop pncService")
    stop_process("pguard.exe")
    stop_process("pncclient.exe")

stop_pguard_pncclient()
