[Home](/fundamentals/)

# Hash Tables

## Overview
Python is built around dictionaries. Instances have dictionaries behind them. In python 3.6, the dictionary byte size is 112. The keys are ordered by chronological addition and it is deterministic (consistently repeatable). (Different from 3.5, which has scrambled dictionaries.)

### Origin
Databases with indexes (1970s). Lists of tuples. 

Dictionaries start to win when a list gets to size two. 

A hash table is something that reduces the search space by cutting it into smaller clusters.

Hash collisions are when two keys convert to the same hash.

Collisions are avoided by creating more buckets. Several buckets will be empty. This wastes space. However, it also accelerates lookups
by reducing the chance that more than one instance occupies the same hash.

### Dynamic Resizing
As the dictionary gets bigger without increasing its buckets, it will slow down. This is because each bucket contains several entries that
must be searched linearly.

To address this, all the values of the dictionary will be copied [(O(n))](https://wiki.python.org/moin/TimeComplexity) out and placed into a dictionary with more buckets. To reduce the cost of
resizing, the original hash for the value is cached in the hash table. This cached hash is used in the process of rehashing the new dictionary.

### Faster Matching
Equality checking in an object oriented program like python can be very slow, such as when a key is a decimal. This makes it expensive to check for equality
when searching in a bucket.

Shortcuts to bypass equality testing (==)  

1. Identity implies equality: when two variables point to the same object then they are equal (is)
2. If two objects have unequal hashes, then the objects must be unequal as well
    - The chance that the hashes are equal to each other and the objects are equal to each other is on the order of 2**64
    - git takes advantage of this by only comparing hashes, rather than files.
    - Uses SHA1 as of May 2017. Looking into a new hashing algorithm since then.

### Linear Probing
Idea is to keep the dictionaries small by taking advantage of as many slots as possible

### Lookup
Knuth-Algorithm D (1960s)

### Multiple Hashing
Whenever you get a collision, do a rehash.
Perturbing gradually adds in bits to the hash as they are needed. (https://wiki.python.org/moin/BitwiseOperators)
Each slot is eventually visited through the generation of a linear congruential random number.

### Versioning of dictionaries
Updates an internal dict version number everytime the dictionary is updated. Versions can be checked, rather than going through a whole new lookup.

### Compact Dictionaries
Data is stored in a tuple (hash, key, and value). Additionally data is stored in a list of indexes.
In the future (from 2017), the list of indexes could be expanded for cheap. This could greatly improve sparsity without taking up much
additional memory. We've come full circle to databases with indexes.

### Key Sharing dictionaries
When the hashes and keys are the same, the values will be shared in the same tuple.


[Raymond Hettinger, Modern Python Dictionaries](https://www.youtube.com/watch?v=npw4s1QTmPg)
