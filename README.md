# OdedProject

Installation:
```
$ git clone https://github.com/OdedViner/OdedProject.git
$ cd OdedProject/
$ python3.8 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip setuptools
$ pip install -e .
```


Local Disk Task:
```
$ local-disk
Number of Files (2): 3
File Size [M] (3): 4
df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p3  476G   16G  459G   4% /home

echo $USER
odedviner

0.040605779999999994 Seconds
```


SSH Task:
```
$ ssh-setup 
number_of_session (2): 
ip address (127.0.0.1): 
username (odedviner): 
password (): 123
command (pwd): pwd
ip address (127.0.0.1): 
username (odedviner): 
password (): 123
command (pwd): date
{'127.0.0.1_0': b'/home/odedviner\n', '127.0.0.1_1': b'Sun Nov 13 07:46:21 PM IST 2022\n'}
```

