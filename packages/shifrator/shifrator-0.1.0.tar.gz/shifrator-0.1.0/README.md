## What is this ? ##

Python library for text encryption.

```python
from shifrator.main import Shifrator 

sh = Shifrator()
print(sh.shifr('Hello World!'))
```

output: `Ifmmp Xpsme!`

```python
from shifrator.main import Shifrator 

sh = Shifrator()
print(sh.reshifr('Ifmmp Xpsme!'))
```

output: `Hello World!`

## To encrypt files ##

in file text.txt:
`Hello World!`

```python
from shifrator.main import Shifrator

sh = Shifrator()
sh.shdocs(file='text.txt', op='shifr')
```

after: 
`Ifmmp xpsme!` 

## Additionally ##

The encoder supports text encryption in both Russian and English.

