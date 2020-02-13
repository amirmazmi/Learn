
#### Recover wifi password
```sudo cat /etc/NetworkManager/system-connections/<SSID> | grep psk=```
<br><br>

#### If you don’t know the network name, use the following command.
```sudo grep psk= /etc/NetworkManager/system-connections/*```
<br><br>
