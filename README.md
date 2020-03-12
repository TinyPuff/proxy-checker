# Proxy Checker
> Checking proxies since 1999. (No, I'm not born in 1999)

Give this script your fresh proxies and it'll give you the ones that work. 

## Dependencies

This program, requires two modules available on Python version 3 and above:
- requests
- pysocks

## Installation

Note that this script requires you to use Python 3.
- First of all, you need to [download][dl] proxy-checker and extract it.
- Now, if you don't have the dependencies, you should install them. 
If you're a GNU/Linux, BSD or MacOS user, you can just simply right-click in the proxy-checker folder and open a terminal and enter the commands below.
If you use Windows, you should do "Shift+Right-Click" in the proxy-checker folder and click on "Open command window here" and then enter these.

```shell
$ pip install pipenv
$ pip install -r requirements.txt
```

## How To Use

- Put your proxies in a text file like this (if you don't have proxies, you can just google the kind of proxies you're looking for and you'll find a bunch of proxy-gathering websites.
e.g. "Free HTTP proxies"):

```
IP:PORT
```
Now, save it and it'll be your input file.

- You can run the script like this (you should have a commant prompt/terminal opened in the proxy-checker directory though.)

```shell
$ python filter.py
```

- First, you need to specify what kind of proxies you're using. [HTTP(s) and SOCKS5]

- It will ask you to choose between 0 and 1. If you choose 0, you will have to enter the path to you input and output files.
And if you choose 1, it will use "default.txt" as input and "result.txt" as output. (Both are placed in "proxy-checker/IO")
Make sure that the input file exists. Otherwise, you'll see this happen:

```
Enter 0 for using custom input/output files and enter 1 for using the default ones.
> 0
Enter the path to the input file: (e.g. C:/Downloads/proxies.txt)
> /fsag/asg.txt                
File doesn't exist.
Enter 0 for using custom input/output files and enter 1 for using the default ones.
> 
```

And after that, the program will print the ones that work and put them into your output file.

> Attention: If you use a Unix-like operating system such as GNU/Linux and your input/output files are in your home folder, you can't refer to them like this: "~/input.txt".
You should enter "/home/your_username/input.txt" instead.
> Attention: Even though I don't recommend it, you can just exit the program by using "CTRL+C".

## Here's An Example

In this example, I'm going to use the default input and output files. You can pick your own input/output files as I said above but I think it's much easier to use the default ones.
At first, I put these into "IO/proxies.txt":
```
154.16.202.22:3128
134.209.205.172:8118
176.9.75.42:3128
37.59.87.204:8080
88.198.24.108:8080
80.241.222.137:80
91.205.174.26:80
80.241.222.138:80
```

And now, I run the script.

```
$ python filter.py
Note that every time you check the quality of these proxies, the previous proxies saved in output file will be deleted.
You may want to copy them and save them in another text file
- HTTP
- HTTPS
- SOCKS5
What protocol are your target proxies using?
> http
Enter 0 for using custom input/output files and enter 1 for using the default ones.
> 1
176.9.75.42:3128
37.59.87.204:8080
```

Looks like only two of the proxies that I put in the input file work.
Let's take a look at my output file, which is the default one.

```
176.9.75.42:3128
37.59.87.204:8080
```

As you see, the program put those two proxies in our output file. It seems to be pretty easy, amirite?

### To-Do
- I should use threads to get the job done as quickly as possible.
- Allow the user to enter username and password for SOCKS5 protocols, if needed.

[dl]:https://github.com/TinyPuff/proxy-checker/archive/master.zip
