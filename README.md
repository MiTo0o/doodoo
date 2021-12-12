# doodoo
________
Don't like using .pop(0) because it looks weird? .pop(0) feels weird to
type out for a queue?

LOOK NO FURTHER

The doodoo package contains a poop() function which does the same thing as
.pop(0). BUTTTTTTT since your digestive system is basically a queue (First
In First Out) it only makes sense to use poop(queue) instead of queue.pop(0)


## install
    pip install doodoo

If that doesnt work try:

    pip3 install doodoo

## usage

```py
from doodoo import poop
queue = [1, 2, 3, 4, 5]

poo = poop(queue)
# poo = 1

# queue = [2, 3, 4, 5]
```