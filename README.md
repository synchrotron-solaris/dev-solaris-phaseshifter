DEVICE CLASS PHASE SHIFTER SOLARIS
==================================

This repository contains Phase Shifter device class based on the facadedevice library.

This project follows
[NSRC SOLARIS coding policies](http://gitlab.m.cps.uj.edu.pl/CSIT/doc-solaris-coding-policies).


What's inside
-------------
There is directory for source code, documentation as well as
`LICENCE` file as well as a setup script.

How to install
--------------
Tested on CentOS7

Firstly, open TangoTest Container as a root:
```console
docker exec -it -u 0 tangotestcontainername bash
```
Then install GIT:
```console
yum install git
```
Clone repository and enter to it:
```console
git clone URL
cd NAME
```
Finally, you can use:
```console
python setup.py install
```
or:
```console
pip install .
```
Now simply type:
```console
DS_NAME DS_INSTANCE
```
**WARNING**: both DS_NAME and DS_INSTANCE must be already declared in database

How to use
----------
I recommend using `Jive` as it allows you to monitor your device. At the beggining, simply configure device
(use *device wizard*) by defining:
- voltage source
- path to the configuraction `.csv` file

Requirements
------------
Requirements for this project are:
 - `setuptools`
 - `facadedevice`
 - `pytango`

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
