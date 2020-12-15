# Using Huffman coding to compress and decompress text

The goal of the project is to use Huffman coding to compress (encode) and decompress (decode) text while using trees and heaps in the process.

## Functions

### `build_tree`

Constructs a Huffman tree from the text using the following algorithm:

1. Turn each character in the frequency table into an object of type `Node` and add to a heap
2. While the heap contains 2 or more items:
    1. Remove two items (`i1` and `i2`) from the heap
    2. Make a new node with the weight equal to the sum of weight of the two items from 3.1
    3. Assign `i1` and `i2` as left and right children of the new node
    4. Add the new node to the heap
3. Remove the only remaining node from the heap. This is the root of the Huffman tree
4. Return the tree root

### `traverse_tree`

Traverse a tree pre-order and return the result

### `follow_tree`

Follow the code through the tree according to the following algorithm:

1. For every bit of the code check the following:
   1. If the code bit is 0, go to the left child
   2. If the code bit is 1, go to the right child
2. Return the value of the current node
   1. `str` if it's a leaf node
   2. `None` if it's an internal node

### `mark_tree`

Generate code for each letter in the text using the following algorithm:

1. If the `root` is empty, return
2. If the value of the `root` is a valid character:
   1. Add the `value: path` mapping to d1
   2. Add the `path: value` mapping to d2
   3. return
3. Recursively mark nodes in the left subtree (add 0 to the `path`)
4. Recursively mark nodes in the right subtree (add 1 to the `path`)
5. Return (d1, d2) tuple

### `print_codes`

Print letters of the text and their codes. The output is ordered by the letter weight.

### `load_codes`

Build the Huffman tree from the stored code-to-character mapping using the following approach:

1. For every code repeat the following:
   1. For every bit of the code repeat the following:
      1. If the bit is *0*, go to the left child of the current node
      2. If the bit is *1*, go to the right child of the current node
   2. Assign the character as a value of the current node
2. Return the root of the tree

Note that you may have to create a node if it does not exist and the logic requires it.

### `compress`

Compress text using the following approach:

1. Replace each character in the text with its code
2. Pad the result with 0 to the right to make the length a multiple of 8 (i.e. *101010* becomes *10101000*)
3. Convert the resulting number to bytes with the same order of bytes as the original text (i.e. `byteorder='big'`)
4. Return the tuple of the packed text and the padding length as a tuple

### `decompress`

Decompress binary data using the following approach:

1. Convert the binary data to a stream of bits (0s and 1s)
2. Let `code` be the first bit of the stream and follow the tree to find the letter corresponding to the `code`
   1. If such a node exists, append its value to the resulting string
   2. If such a node does not exist (`follow_tree` returns `None`), add the next bit from the stream to `code` and repeat the search
3. Continue until the end of the stream

## Testing

Test and verify your implementation as follows:

```bash
python -m pytest -v tests/projects/compdecomp/
```
