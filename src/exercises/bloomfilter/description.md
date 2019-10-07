# Bloom filter

Implement a simple spell checker using *Bloom filter* and `crc32` hashing function.

The size *n* of the dictionary is *26*, false positive probability *p* is *0.01*.

Using formulas on page 209 of the textbook calculate size $m$ of the filter as *250* and number of hash functions *k* as *7*.

Our filter is a single bit vector of size *m*.

We are going to use a single hash function as follows:
  * first, hash the word (e.g. *fox*) using `crc32` and find the index value modulo *m*
  * next, hash the word concatenated to itself (e.g. *foxfox*) and find the second index value
  * continue until there are *k* indices and return a `tuple`

If implemented properly, your spellchecker must detect **all** misspelled words and pass the provided tests.
