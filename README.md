# Alivebot

A script to find and react to !ALIVE commands in comments on the Hive blockchain.

*Please note that this software is in early Beta stage, and that you need to know what you are doing to use it.*

## Installation 

For Ubuntu and Debian install these packages:
```
sudo apt-get install python3-pip build-essential libssl-dev python3-dev python3-setuptools python3-gmpy2
```

### Install Python Packages

Install alivebot by (you may need to replace pip3 by pip):
```
sudo pip3 install -U alivebot beem hiveengine
```

## Configure And Run Alivebot

First clone the Github repository to your home directory:
```
cd ~
git clone https://github.com/flaxz/alivebot
```

After that edit your comment templates using Nano, there are 4 comment templates.
```
sudo apt install nano 
cd ~/alivebot/templates
ls
nano COMMENT-TEMPLATE-1-2-3-4
```

Then edit your configuration file.
```
cd ~/alivebot
nano alivebot.config
```

Copy your configuration and comment templates to your working directory.
```
cd ~/alivebot
sudo cp -R templates /usr/local/bin
sudo cp alivebot /usr/local/bin
sudo cp alivebot.config /usr/local/bin
sudo cp run-alivebot.sh /usr/local/bin
```

Make the startup scripts executable.
```
cd /usr/local/bin
sudo chmod u+x alivebot
sudo chmod u+x run-alivebot.sh
```

Copy the Systemd config to it's directory.
```
cd ~/alivebot
sudo cp alivebot.service /etc/systemd/system
```

Reload Systemd and start the bot.
```
sudo systemctl daemon-reload
sudo systemctl start alivebot.service
```

Get status and error messages.
```
sudo systemctl status alivebot.service
q
```

Stop the bot.
```
sudo systemctl stop alivebot.service
```

As has been stated above this bot is in early Beta and bugs and issues are likely to occur.

