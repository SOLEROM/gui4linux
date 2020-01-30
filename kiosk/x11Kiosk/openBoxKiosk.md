# openBox kiosk

* ref1: https://projects-42.nl/index.php/2018/ubuntu-18-04-lts-kiosk-for-web-or-rdp/


## deps

app layer: 

```
sudo apt-get install chromium-browser
```

graphic layer

```
on server:
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox -y

on X-server:
sudo apt-get install  xinit openbox 

```

## get to user shell on boot

```
sudo systemctl edit getty@tty1
==============================
    [Service]
    ExecStart=
    ExecStart=-/sbin/agetty -a <username> --noclear %I $TERM

//reboot to check

```

## set graphic env

```
~/.xinitrc
==========
exec openbox-session
```

## run kiosk

config openbox app:

```
/etc/xdg/openbox/autostart
==========================
# Disable any form of screen saver / screen blanking / power management
xset s off
xset s noblank
xset -dpms

# Start Chromium in kiosk mode
chromium-browser --disable-infobars --kiosk '<http://your-url-here>'

```

start on boot

```
.bash_profile
=============
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx
```

