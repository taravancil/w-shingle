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
$ python w_shingle.py "a rose is a rose is a rose" -w 4
[['a', 'rose', 'is', 'a'], ['rose', 'is', 'a', 'rose'], ['is', 'a', 'rose', 'is'], ['a', 'rose', 'is', 'a'], ['rose', 'is', 'a', 'rose']]
```
