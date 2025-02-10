import psutil
import time 
import os
from datetime import datetime
#test "sublime_text.exe",    
sleeping_block = ["msedge.exe"]       
blocked_app = ["leagueclient.exe"]
blocked_time = {
    8:10,
    12:16,
    18:23
}
def is_within_block_time():
    now = datetime.now().hour
    for start_time in blocked_time:
        end_time = blocked_time[start_time]
        if start_time <= now < end_time :
            return True
    return False
def is_sleeping_time():
    now = datetime.now().hour
    if now >= 23 or now <= 7:
        return True
    return False
def block_apps():
    while True:
        if is_sleeping_time():
            for process in psutil.process_iter(attrs=['pid','name']):
                try:
                    if process.info['name'].lower() in sleeping_block:
                        print(f"Shut down {process.info['name']}(PID: {process.info['pid']})")
                        os.system(f"taskkill /F /PID {process.info['pid']}")
                        continue
                except (psutil.NoSuckProcess,psutil.AccessDenied):
                    continue
        # if is_within_block_time():
        #     for process in psutil.process_iter(attrs=['pid','name']):
        #         try:
        #             if process.info['name'].lower() in blocked_app:
        #                 print(f"Shut down {process.info['name']}(PID: {process.info['pid']})")
        #                 os.system(f"taskkill /F /PID {process.info['pid']}")
        #         except (psutil.NoSuchProcess,psutil.AccessDenied):
        #             continue
        else:
            print("It's free time")
        time.sleep(5)
if __name__ == "__main__":
    print(f"blocker is running...")
    block_apps()