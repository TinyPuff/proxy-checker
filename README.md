# Proxy Checker
> Checking proxies since 1901

Give this script some fresh proxies and it'll put the ones that work in a file named "result.txt".
The text files "result.txt" and "default.txt" are placed inside the IO folder.

## Dependencies

- Python Requests Module

## Installation

Note that this proxy requires Python 3.
- First of all, you need to [download][dl] proxy-checker and extract it.
- Now, if you don't have the dependencies, you should install them:

```shell
pip install -r requirements.txt
```

- Put your proxies in "IO/default.txt" like this:
```
IP:PORT
```

- This only thing that's left is to run the script:

```shell
python filter.py
```

## Here's an example

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

[dl]:https://github.com/TinyPuff/proxy-checker/archive/master.zip
