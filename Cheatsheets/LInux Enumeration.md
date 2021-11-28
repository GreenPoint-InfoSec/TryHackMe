# Linux Enumeration

### ssh
ssh user@IP:Port

hostname

uname -a

env

cat /etc/issue

cat /etc/passwd  // cat /etc/passwd | -d ":" -f 1

cat /etc/passwd

cat /etc/shadow

unshadow **************

ps

ps -A

ps aux

ps axjf

cat /etc/passwd | grep home

ifconfig

ip route

netstat -a

netstat -at

netstat -au

netstat -l

netstat -s / -st / -su

netstat -tp

netstat -i

sudo -l

sudo -V




### Telnet

telnet <IP> <Port>
  
{HTTP} 

GET / HTTP/1.1  // GET /page.html HTTP/1.1

{pop3}

USER name

PASS password

STAT

LIST

RETR

QUIT

{IMAP}

LOGIN <name> <password>

LIST

EXAMINE INBOX

LOGOUT

  
### ftp
  
ftp IP Port

login

ftp> ls

ftp> ascii

ftp> get ftp_flag.txt

ftp> exit

  
  
### Find
  
find /location
-type f / d
-user
-size 150c / 10Mc / 30Kc / -50Mc / +80c
-perm 644 / -u=r
-perm -444
-perm /666
-atime +10 = accessed more than 10 days
-mmin -120 = modified within 2 hours
-ctime 0 = status change in last 24 hours
2> /dev/null
  
find . -name flag1.txt: find the file named “flag1.txt” in the current directory
find /home -name flag1.txt: find the file names “flag1.txt” in the /home directory
find / -type d -name config: find the directory named config under “/”
find / -type f -perm 0777: find files with the 777 permissions (files readable, writable, and executable by all users)
find / -perm a=x: find executable files
find /home -user frank: find all files for user “frank” under “/home”
find / -mtime 10: find files that were modified in the last 10 days
find / -atime 10: find files that were accessed in the last 10 day
find / -cmin -60: find files changed within the last hour (60 minutes)
find / -amin -60: find files accesses within the last hour (60 minutes)
find / -size 50M: find files with a 50 MB size
find / -writable -type d 2>/dev/null : Find world-writeable folders
find / -perm -222 -type d 2>/dev/null: Find world-writeable folders
find / -perm -o w -type d 2>/dev/null: Find world-writeable folder
find / -perm -o x -type d 2>/dev/null : Find world-executable folders
find / -name perl*
find / -name python*
find / -name gcc*
find / -perm -u=s -type f 2>/dev/null: Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user. 
find / -type f -perm -04000 -ls 2>/dev/null will list files that have SUID or SGID bits set.
  
  
### Netcat Reverse Shell > tty (text terminal)

python3 -c 'import pty; pty.spawn("/bin/bash")'

perl -e 'exec "/bin/bash"
