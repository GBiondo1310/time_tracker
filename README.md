# TIME TRACKER

## This tool is built for personal use, but you can clone and use it.

### How to use it (How I use it):

- Place the python script in any folder.
- Put this in ```.bash_aliases```
```
alias timetrack="python3.10 ~/path/to/script/main.py"
```
- Now you can use 
```
timetrack -s
timetrack -e
timetrack -g
```
wherever you want.

---



### Usage:

- Start a tracking time on your project
```
timetrack -s
```

- Always remember to end timetrack, otherwise you will end with thousands of hours of work you never did (lol):
```
timetrack -e
```

- Get your working time:
```
timetrack -g
```

### Notes:
- Please remember that every command referres to your terminal current location, so if you launch ```timetrack -a``` in e.g. ```/home/foofolder```, then you will have to launch ```timetrack -e``` in ```/home/foofolder```.

- Also remember that this script creates a ```.timetrack``` file in your project's folder. 
---

## That's it.