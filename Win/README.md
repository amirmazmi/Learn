 # Extract product key from windows as backup

In command prompt  
```
wmic path softwarelicensingservice get OA3xOriginalProductKey
```
<br>

Or in powershell  

```
powershell "(Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey"
```

## Digital licence
Some installations are activated using a digital licence (OEM) 
* use the script key.vbs to extract. This will not match the commands above. 
* download and double-click to run
