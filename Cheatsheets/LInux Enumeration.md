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
