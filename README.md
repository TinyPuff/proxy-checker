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
pip install <module>
```

and in this case, you should use the command below:

```shell
pip install requests
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

The code above fetches the `README-default.md` file from this repository and
renames it to `README.md`.

## Fill with your own text

The default template has some guiding text to get you started. However you'll
need to edit the file with your own text to use it with your project.

```shell
atom README.md
```

If you're using [Atom](https://atom.io/) code editor, the code above opens the
file for editing. If necessary, substitute with your preferred markdown editor.

### Add to git and push

After you've filled your `README.md` file with your own project's text, you
should push it to your GitHub project:

```shell
git add README.md
git commit -m "Added: README"
git push
```

This adds the `README.md` file to your git repository, creates a commit for it
and pushes it to GitHub (or other preferred remote repository).
