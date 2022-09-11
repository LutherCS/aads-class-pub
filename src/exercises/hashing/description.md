# Hashing it out

Complete the following hashing functions. Note that you are not required to address collisions, so duplicates are expected.

1. Implement a hash function for **integers** using the *simple remainder* method.

    ```python
    12 % 3 == 0
    ```

2. Implement a hash function for **integers** using the *mid-square method* (use 2 middle digits, pad the square with leading 0, if necessary).

    ```python
    12 ** 2 == 144 == 0144
    14 % 3 == 2
    13 ** 2 == 0169
    16 % 3 == 1
    330 ** 2 == 108900
    89 % 3 == 2
    ```

3. Implement a hash function for **integers** using the *folding method* (extract two digits at a time, the last item may be a single-digit number).

    ```python
    123 == 12 + 3 == 15
    15 % 3 == 0
    330 == 33 + 0 == 33
    33 % 3 == 0
    ```

4. Implement the hash function for **strings** using *sum of values* of all characters.

    ```python
    "cat" == 99 + 97 + 116 == 312
    312 % 3 == 0
    ```

5. Implement the hash function for **strings** using *character value and its position as a weight*.

    ```python
    "cat" == 0 + 97 + 232 == 329
    329 % 3 == 2
    ```
