# Proxy Checker
> Checking proxies since 1901

Give this script some fresh proxies and it'll put the ones that work in a file named "result.txt".
The text files "result.txt" and "default.txt" are placed inside the IO folder.

## Dependencies

- Python Requests Module

## Installation

Note that this script requires you to use Python 3.
- First of all, you need to [download][dl] proxy-checker and extract it.
- Now, if you don't have the dependencies, you should install them. 
If you're GNU/Linux or BSD user, you can just simply right-click in the proxy-checker folder and open a terminal and enter the commands below.
If you use Windows, you should do "Shift+Right-Click" in the proxy-checker folder and click on "Open command window here" and then enter these.

```shell
$ pip install pipenv
$ pip install -r requirements.txt
```

## How To Use

- Put your proxies in a text file like this:

```
IP:PORT
```

- This only thing that's left is to run the script:

```shell
$ python filter.py
```

## Here's An Example

At first, I put these into default.txt:
```
104.244.75.26:8080
178.62.193.19:3128
138.201.223.250:31288
142.93.224.87:8118
37.59.87.204:8080
212.227.11.130:80
91.205.174.26:80
5.79.72.118:8118
80.187.140.26:8080
80.241.222.138:80
```

And now, I run the script.

```shell
$ python filter.py
Note that every time you check the quality of these proxies, the previous proxies saved in result.txt
will be deleted. You may want to copy them and save them in another text file
Are you sure you want to do this?(y/n)
> y
Here we go...
104.244.75.26:8080
138.201.223.250:31288
212.227.11.130:80
5.79.72.118:8118
```

### To-Do
- I should use threads to get the job done as quickly as possible.
- Let the user now if the chosen input file doesn't exist.
- Allow the user to enter username and password for SOCKS5 protocols, if needed.
- Update the "How To Use" section in README.md

[dl]:https://github.com/TinyPuff/proxy-checker/archive/master.zip
