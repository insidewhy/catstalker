# Usage

```
% catstalker -h
usage: catstalker.py [-h] [-s SOCKET] [-o]

control energenie remote board for raspberry pi

optional arguments:
  -h, --help            show this help message and exit
  -s SOCKET, --socket SOCKET
                        control specified socket from 1-4 (default = all)
  -o, --off             turn socket(s) off (default is to turn on)

% catstalker        # turn on all sockets
% catstalker -o     # turn off all sockets
% catstalker -s1    # turn on socket 1
% catstalker -s1 -o # turn off socket 1
```
