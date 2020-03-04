# screen sharing not enable

## problem:
unity control center > sharing > screen sharing > no network selected for sharing ; connection is working fine / but don't show in sharing setting /

the root cause was Gnome not allowing ScreenSharing when no network connected. Gnome gets the information from the NetworkManager. And it is not reporting any network because it is not set to manage those connections.

## fix:

```
/etc/netplan/01-network-manager-all.yaml
=========================================
network:
  version: 2
  renderer: NetworkManager      //AddTHIS!!!!


change managed to true in
/etc/NetworkManager/NetworkManager.conf
=======================================
  [ifupdown]
  managed=true

```

```
sudo netplan apply
```
