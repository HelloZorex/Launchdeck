<img src='https://github.com/HelloZorex/Launchdeck/blob/main/img/screenshot1.png' alt='gui' width='400'>

## Launchdeck

Simple application that turns your novation launchpad mk2 into a customizable controller

```
python gui.py
```
*Currently supported on windows, linux coming soon

<!--```bash-->
<!--pip3 install git+https://github.com/HelloZorex/Launchdeck.git --upgrade-->
<!--```-->

### Features:
- open .exe file
- open chrome tab
- execute keyboard shortcut
- play sound

### How To Use:
1. Connect your Novation Launchpad MK2 into your computer
2. Open Launchdeck
3. Select a button you desire to change, then select "Change Func"
4. Select your button function from the dropdown menu and complete the prompts
5. Start Launchpad Midi input by pressing "Start"
6. Stop Midi input by pressing "Stop"

- *to open websites using Chrome, please select your Chrome file location using the "Settings" button and selecting "Chrome path"*
- *keyboard shortcut example: "command", "control + s", "left", "up", "command + space"*
- *to see what a button is assigned to, hover over the button*

## Trouble Shooting

### "Select button you want to change first" prompt shows up after I try to change function
Don't install Launchdeck into Program Files, Program Files (x86), or any folder that needs file permissions
