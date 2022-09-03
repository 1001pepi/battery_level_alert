# (c) TANANKEM Rames (1001pepi), September 2022

#import os
#the  os.system function is deprecated since it directly run shell commands; it is not sercure;
#it is recommanded to use the subprocess module
#os.system(cmd)
import subprocess
import re
import time, threading

def get_battery_info():
    #get the state and the percentage of the battery 
    cmd = "upower"
    process = subprocess.Popen([cmd, '-i','/org/freedesktop/UPower/devices/battery_BAT0'], stdout=subprocess.PIPE)
    output = str(process.communicate()[0], 'utf-8')

    state_pattern = "state:.*"
    percentage_pattern = "percentage:.*"

    m = re.search(state_pattern, output)
    state = m.group(0).split(":")[1].strip()

    m = re.search(percentage_pattern, output)
    percentage = int(m.group(0).split(":")[1].strip()[:-1])

    return state, percentage

def play_audio_file(file_name):
    cmd = "mpg123"
    process = subprocess.Popen([cmd, file_name], stdout=subprocess.PIPE)
    process.communicate()

def check_battery():
    state, percentage = get_battery_info()
    print(state, percentage)
    
    if state == 'charging' and percentage > MAX_THRESHOLD:
        play_audio_file('full_battery_alert.mp3')
        
    if state == 'discharging' and percentage < MIN_THRESHOLD:
        play_audio_file('low_battery_alert.mp3')
    
class SetInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()
        
    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime - time.time()):
            nextTime += self.interval
            self.action()
            
    def cancel(self):
        self.stopEvent.set()
        
if __name__ == '__main__':
    
    MAX_THRESHOLD = 70
    MIN_THRESHOLD = 30
    
    #check if the mpg123 package is installed
    cmd = "dpkg"
    process = subprocess.Popen([cmd, '-l', 'mpg123'], stdout=subprocess.PIPE)
    output = str(process.communicate()[0], 'utf-8')
    if process.returncode != 0:#the package is not yet installed
        print("You have to install the mpg123 package.\nYou can do it by running the command 'sudo apt-get install mpg123'.")
        exit()
        
    StartTime = time.time()
        
    inter = SetInterval(5*60, check_battery)