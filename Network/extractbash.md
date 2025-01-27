
#### Recover wifi password
```sudo cat /etc/NetworkManager/system-connections/<SSID> | grep psk=```
<br><br>

#### If you don’t know the network name, use the following command.
```
# list all
sudo grep psk= /etc/NetworkManager/system-connections/*

# split into columns
sudo grep psk= /etc/NetworkManager/system-connections/* | sed 's/\//  /g'

# just get the output 
sudo grep psk= /etc/NetworkManager/system-connections/* | cut -d/ -f5 | sed 's/:psk=/\n\t/g'
```
<br><br>
