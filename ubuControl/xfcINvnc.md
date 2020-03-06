# use xfce desktop with vnc

* working on locked station!

## Install

```
sudo apt install xfce4
```


## vnc start xfce4

```
~/.vnc/xstartup
===============
#!/bin/sh
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
vncconfig -iconic &
startxfce4 &
```
