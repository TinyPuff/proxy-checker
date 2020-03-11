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

Here's an example:

```
127.0.0.1:9050
127.0.0.1:9150
```

- This only thing that's left is to run the script:

```shell
python filter.py
```

[dl]:https://github.com/TinyPuff/proxy-checker/archive/master.zip
