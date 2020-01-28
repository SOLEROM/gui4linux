# chromium-mir-kiosk on mir-kiosk

* using snap (https://codeburst.io/how-to-install-and-use-snap-on-ubuntu-18-04-9fcb6e3b34f9)

## install

```
stable
=======
snap install mir-kiosk
snap install --beta chromium-mir-kiosk


dev
====
snap install --devmode mir-kiosk
sudo snap install chromium-mir-kiosk --beta --devmode

```

## config

set connections

```
snap connect chromium-mir-kiosk:wayland mir-kiosk:wayland
```

check connection

```
snap connections chromium-mir-kiosk
====================================
wayland                   chromium-mir-kiosk:wayland                   mir-kiosk:wayland        manual

```

get settings

```
snap get chromium-mir-kiosk
snap get mir-kiosk

```

set settings

```
> sudo snap set chromium-mir-kiosk shownav=true

daemonize mir-kiosk to start after boot:
> sudo snap set mir-kiosk daemon=true

To customize the startup url for chromium use:
> sudo snap set chromium-mir-kiosk url="https://yoururl.com"


```


## run

```
sudo mir-kiosk 
sudo snap start chromium-mir-kiosk
systemctl status snap.chromium-mir-kiosk.chromium-mir-kiosk.service

```


## debug

snap list

```
chromium-mir-kiosk    69.0.3497.100               35    beta      gerboland     devmode
mir-kiosk             1.7.0-snap93                3055  stable    canonical✓    devmode
```

```
sudo snap connections mir-kiosk
================================
Interface  Plug                        Slot               Notes
opengl     mir-kiosk:opengl            :opengl            -
wayland    chromium-mir-kiosk:wayland  mir-kiosk:wayland  manual
x11        mir-kiosk:x11               :x11               -


sudo snap get  mir-kiosk
========================
Key             Value
cursor          auto
daemon          false
display-layout  default
vt              4


sudo snap connections chromium-mir-kiosk 
========================================
Interface                 Plug                                         Slot                     Notes
browser-support           chromium-mir-kiosk:browser-sandbox           :browser-support         -
camera                    chromium-mir-kiosk:camera                    -                        -
cups-control              chromium-mir-kiosk:cups-control              -                        -
desktop                   chromium-mir-kiosk:desktop                   :desktop                 -
gsettings                 chromium-mir-kiosk:gsettings                 :gsettings               -
hardware-observe          chromium-mir-kiosk:hardware-observe          -                        -
home                      chromium-mir-kiosk:home                      :home                    -
mount-observe             chromium-mir-kiosk:mount-observe             -                        -
network                   chromium-mir-kiosk:network                   :network                 -
network-manager           chromium-mir-kiosk:network-manager           -                        -
opengl                    chromium-mir-kiosk:opengl                    :opengl                  -
password-manager-service  chromium-mir-kiosk:password-manager-service  -                        -
pulseaudio                chromium-mir-kiosk:pulseaudio                :pulseaudio              -
removable-media           chromium-mir-kiosk:removable-media           -                        -
screen-inhibit-control    chromium-mir-kiosk:screen-inhibit-control    :screen-inhibit-control  -
wayland                   chromium-mir-kiosk:wayland                   mir-kiosk:wayland        manual
x11                       -                                            chromium-mir-kiosk:x11   -
x11                       chromium-mir-kiosk:x11-plug                  -                        -


sudo snap get chromium-mir-kiosk 
=================================
Key           Value
disablekiosk  false
hidecursor    false
resettime     5
shownav       false
url           https://www.ubuntu.com/internet-of-things



```
