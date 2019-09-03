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
