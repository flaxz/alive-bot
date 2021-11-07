# Alivebot

A script to find and react to !ALIVE commands in comments on the Hive blockchain.

*Please note that this software is in early Alpha stage, and that you need to know what you are doing to use it, plus that the instructions below are not yet complete.*

## Installation 

For Ubuntu and Debian install these packages:
```
sudo apt-get install python3-pip build-essential libssl-dev python3-dev python3-setuptools python3-gmpy2
```

For Termux on Android install these packages:
```
pkg install clang openssl python
```

Signing and Verify can be fasten (200 %) by installing cryptography (you may need to replace pip3 by pip):
```
pip3 install -U cryptography
```

or (you may need to replace pip3 by pip):
```
pip3 install -U secp256k1prp
```

### Install Python Packages

Clone the git repository and install alivebot by:
```
pip3 install -U beem hiveengine
git clone https://github.com/flaxz/alivebot
cd alivebot
python3 setup.py install
```

## Configure And Run Alivebot

These instructions will be added after further testing