# vnc4server

## about
vncserver doesn't connect to the actual desktop; it creates a virtual desktop that is configured separately. If you want to access the actual desktop then you need to use either the VNC X extension or Vino

* install
```
apt -y install vnc4server
```

* run to activate
```
# set VNC password
ubuntu@dlp:~$ vncpasswd

# start VNC server
ubuntu@dlp:~$ vncserver :1

# stop once
ubuntu@dlp:~$ vncserver -kill :1
// will create ~/.vnc/xstartup
```

* edit what to start:
* default config is giving gray screen //TBD

```
~/.vnc/xstartup_original default
================================
#!/bin/sh

# Uncomment the following two lines for normal desktop:
# unset SESSION_MANAGER
# exec /etc/X11/xinit/xinitrc

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &
x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
x-window-manager &

```



```
~/.vnc/xstartup
===============

//start firefox only:
#!/bin/sh
/usr/bin/firefox



```

* test
```
## start to test
ubuntu@dlp:~$ vncserver :1 -geometry 800x600 -depth 24
```
