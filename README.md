# Alex: a Python BOT for IRC

A simple Python Bot that works over TOR connection.

## Requirements:
- TOR
- Python

## Configuration

### Base section
IRC server paramenters

```
[base]
server: onionaddress
port: 6697
nickname: username
password: password
channels: #chan1,#chan2
chanpwd: group_pwd
```

### BOT answers

```
[bot]
placeholder : !
replies = {
	'menu' : 'ansa,weather,time',
	'ansa' : 'Ultime notizie',
	'weather' : 'previsioni del tempo',
	'@' : 'Si scusa sono impegnato',
	'time': 'Sono le ore'
	}
```
