

* using snap (https://codeburst.io/how-to-install-and-use-snap-on-ubuntu-18-04-9fcb6e3b34f9)

## install

```
snap install mir-kiosk
snap install --beta chromium-mir-kiosk

snap install --devmode mir-kiosk
sudo snap install chromium-mir-kiosk --beta --devmode

```

```
snap install --edge mir-kiosk-apps
snap connect mir-kiosk-apps:wayland
sudo snap set mir-kiosk-apps daemon=true
sudo snap restart mir-kiosk-apps
```


## config

```
snap connections chromium-mir-kiosk

snap get chromium-mir-kiosk

```

```
sudo snap set chromium-mir-kiosk shownav=true

sudo snap start chromium-mir-kiosk

systemctl status snap.chromium-mir-kiosk.chromium-mir-kiosk.service

```


```
daemonize mir-kiosk to start after boot:
> sudo snap set mir-kiosk daemon=true

To customize the startup url for chromium use:
> sudo snap set chromium-mir-kiosk url="https://yoururl.com"

```



```
mir-kiosk --devmode
```

