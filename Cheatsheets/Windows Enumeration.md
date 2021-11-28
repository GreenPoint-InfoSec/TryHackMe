# Windows Command Prompt

### Check Hostname 
hostname

### Current user’s privileges
whoami /priv

### List users
net users

### List details of a user (e.g. net user Administrator)
net user username

### Other users logged in simultaneously (the query session command can be used the same way)
qwinsta  

### User groups defined on the system 
net localgroup

### List members of a specific group (e.g. net localgroup Administrators) 
net localgroup groupname

### systeminfo
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

### Find
findstr /si password *.txt

“.txt”, “.xml”, “.ini”, “*.config”, and “.xls”
Command breakdown:
findstr: Searches for patterns of text in files.
/si: Searches the current directory and all subdirectories (s), ignores upper case / lower case differences (i)
password: The command will search for the string “password” in files
*.txt: The search will cover files that have a .txt extension

### List updates:
wmic qfe get Caption,Description,HotFixID,InstalledOn

### Installed software:
wmic product get name,version,vendor

### Running services:
wmic service list brief
wmic service list brief | findstr  "Running"
wmic service get name,displayname,pathname,startmode  
sc qc <service>
wmic service get name,displayname,pathname,startmode | findstr /i "C:\Windows"
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i "C:\Windows"
wmic service get name,displayname,pathname,startmode | findstr /i /v "C:\Windows"

icacls "C:\<name>"


### Anti-virus:
sc query windefend
sc queryex type=service


### netstat
netstat -ano
-a: Displays all active connections and listening ports on the target system.
-n: Prevents name resolution. IP Addresses and ports are displayed with numbers instead of attempting to resolves names using DNS.
-o: Displays the process ID using each listed connection. 


### Others 
schtasks /query /fo LIST /v
driverquery
