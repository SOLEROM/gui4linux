## ubuControl::topics

## general
* [understand different desktop environments](./desktopEnv.md)
* [understand different desktop displays](./desktopDisp.md)

## ubuntu18 working set:
* option#1: use default vino (locked screen issue)
  - [ubu18 sharing enable](./ubu18DesktopShareIssue1.md)
* option#2: login and bind to locked machine
  - [SwitchToLighDM](./ubu18SwitchToLighDM)
  - [add x11 vnc intead on vino](./vncServers/x11vnc.md)
* option#3: use alternative session
  - [xfc with vnc](./xfcINvnc.md)


## control options

* bash on webpage: terminado

* default ubu18 vnc+remmina
  - [enable desktop sharing - default buildin](./ubu18DesktopShareIssue1.md)
  - [no login to locked machine](./ubu18VncFromLogin.md)

* vncServers:
  - [ubu18x buildin vnc](./vncServers/gnomeVnc.md)
  - [vnc4server](./vncServers/vnc4server.md) -gray screen [x]
  - [tigerVnc](./vncServers/tigerVnc.md) - new ubuntu-session [v]
  - [x11vnc](./vncServers/x11vnc.md) - bind to screen [v]

* novnc
  - [create bind to vnc server](novnc.md)
  - work with external vnc server [use tigerVnc](./vncServers/tigerVnc.md)
  - kiosk app
  - connect to active x [use x11vnc](./vncServers/x11vnc.md)
