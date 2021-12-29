# FJ-ez-pass
Bot solves ropots (odpovedniky) in FJ1028 in one session that is specified

# Motivation
I'm lazy to do the fcking ropots and they take forever

# Installation

```
pip install selenium
git clone https://github.com/undy45/FJ-ez-pass.git
```

To use this bot you need to have a Chrome webdriver corresponding to your version of Chrome (Yes you can only use Chrome sorry).
You can find out your version of Chrome by going to ... (in top right) -> Help -> About Google Chrome

After that you can download the correct version of driver from:
[Link](https://sites.google.com/chromium.org/driver/)

Extract file somewhere on you system and add path to the driver to the config.py file (leave the r before the string) as well with your UCO, primary password and the lecture index starting by 1

# How to use?
After Installation you can just run the program.

# Known bugs
* If you have recently selected some of yours past semesters and it is remembered you will have to change it back to the current one as this will break the bot as it doesn't know how to check which semester it is in
* If you recently did a ropot and forcefully closed it (for example by closing the tab), IS gives you a little prompt asking you if you are sure that you want to open said ropot again. This will break the bot as it doesn't check for this.
