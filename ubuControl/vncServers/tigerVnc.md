# tigervnc

## Install

```
//basic:
sudo apt install tigervnc-standalone-server
//more:
sudo apt install tigervnc-xorg-extension tigervnc-viewer
```

* 1configure

```
vncpassword
vncserver
vncserver -kill :*
```

* start ubuntu session

```
~/.vnc/xstartup
===============
#!/bin/sh
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
vncconfig -iconic &
dbus-launch --exit-with-session gnome-session &
```

* test

```
vncserver -localhost no -geometry 800x600 -depth 24
```


## start stop systemd


```
/etc/systemd/system/vncserver@.service
======================================
[Unit]
Description=VNC Server by TeknoTut
After=syslog.target network.target

[Service]
Type=forking
User=away

# Clean any existing files in /tmp/.X11-unix environment
ExecStartPre=/usr/bin/vncserver -kill :%i > /dev/null 2>&1 || :
ExecStart=/usr/bin/vncserver -geometry 800x600 -depth 24 -localhost no :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```


```
sudo systemctl enable vncserver@1
sudo systemctl start vncserver@1
```
