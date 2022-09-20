# battery_level_alert
Vocal alert when the level of the computer's battery reaches a critical value using python for ubuntu.

# How to install and run the project
1. Clone the git repository
2. Make sure you have the **mpg123** and **screen** packages installed. If not, you can do it by running the command:
```
sudo apt-get install mpg123
```
The mpg123 package will be used to read audio files when sending the alert, and the screen package to run the script in the background.
3. Copy the **battery_level_alert_script.sh** file inside your **/home/$user/** directory.
4. Open the **/home/$user/.profile** file by running the command:
```
nano /home/$user/.profild
```
in the terminal. And add this code at the end of the file:
```
screen -d -m bash /home/$user/battery_alert_script.sh
```

> The two previous help to automatically launch the battery_level_aler.py script each time you will log in instead of doing it manually.

> If you have completed all the previous steps, your project is well installed and working.

# How to use the project and additional information
You can personalize the program as you want. For that, open the **battery_level_alert.py** file.
1. **Set the battery level thresholds**: you can do that by modifying the values of the variables **MAX_THRESHOLD** and **MIN_THRESHOLD**.
2. **Set the period of checking the battery level**: you can set the **PERIOD** variable.
3. **Set the message alerts:** go to this link (https://ttsmp3.com), write the message alerts you want to hear for min_threshold and max_threshold, thus download them and save them respectively with names **low_battery_alert.mp3** and **full_battery_alert.mp3**. Replace the two files in the battery_level_alert directory. And you are done. You will now listen to those messages as alerts.
