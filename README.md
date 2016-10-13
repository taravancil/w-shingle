```
usage: w-shingle.py [-h] [-w W] string

Transform a string into tokens of length w.

positional arguments:
  string      the string to tokenise

optional arguments:
  -h, --help  show this help message and exit
  -w W        the number of words per shingle
```

### Example

``` bash
user@user-ThinkPad-T400 ~/c/w-shingle> python w_shingle.py "I am an idiot" -w 2
[['I', 'am'], ['am', 'an'], ['an', 'idiot']]
user@user-ThinkPad-T400 ~/c/w-shingle> python w_shingle.py "I am an idiot" -w 3
[['I', 'am', 'an'], ['am', 'an', 'idiot']]
```
