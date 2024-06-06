## What is this ? ##

Python library for text encryption.

```python
from shifrator.main import Shifrator 

sh = Shifrator()
print(sh.encrypt('Hello World!', 'test111'))
```

output: `Wtааг Кгёаs!`

```python
from shifrator.main import Shifrator 

sh = Shifrator()
print(sh.decrypt('Ifmmp Xpsme!', 'test111'))
```

output: `Hello World!`

## To encrypt files ##

in file text.txt:
`Hello World!`

```python
from shifrator.main import Shifrator

sh = Shifrator()
sh.shdocs(file='text.txt', op='shifr', key='test111')
```

after: 
`Wtааг Кгёаs` 

## Additionally ##

The encoder supports text encryption in both Russian and English.

