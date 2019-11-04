---
title: "B-Tree"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

* Database background
* B-Tree organization
* B-Tree implementation
* B-Tree operations

## Database background

### Database design

![Dairy DB design](images/dairyDBdesign.png)

::: notes

<http://knuth.luther.edu/~leekent/CS2Plus/chap10/chap10.html#figures-from-text>

:::

### Relational database

* Many *relations* (entities) connected via *relationships*
* Represented as an *LDS* or an *ERD*
* Relationships could be: *1-1*, *1-M*, *M-M*
* *M-M* relationships must be *reified* for the schema to work properly
* Schema should be *normalized* to remove functional dependencies
* Reification and normalization yield new entities
* Data can be retrieved from tables using *join* operation

### Textbook example

* Relation *Feed* contains items like corn silage and alfalfa
  * Those items are composed of many nutrients
* Relation *FeedAttribType* contains nutrients (calcium, iron, sugar etc)
  * Those nutrients can be part of many feeds
* Relation *FeedAttribute* is used to reify many-many relationship between feed and nutrient
* *FeedAttribute* adds the value for the quantity

### Textbook example LDS

![Feed-FeedAttribType](images/dairyDBlds.png)

### Challenge

```sql
select Feed.FeedNum, Feed.FeedName, FeedArribType.Name, FeedAttribute.Value
from Feed, FeedAttribute, FeedAttribType
where Feed.FeedID = FeedAttribute.FeedID and FeedAttribute.FeetAttribTypeID = FeetAttribType.FeetAttribTypeID
```

### Database organization

* Each relation (table) is stored as a separate file
* Joining tables means reading 2 files
  * In the worst case, sequentially
* Data can be stored in increasing order (of the key)
  * Parts of a file can be accessed directly using Python's `seek` function
* Big question: **are tables always ordered?**

::: notes

<http://knuth.luther.edu/~leekent/CS2Plus/chap10/chap10.html#the-inefficient-join-program>

:::

### Database index

* A structure that allows efficient lookup time on any record in the table
* Implementation details are left up to a specific DBMS

### B-Tree history

* Invented by Rudolf Bayer and Edward McCreight
* Bayer also invented *red-black tree* in 1972
* The meaning of **B** is unknown (could be Boeing, balanced, Bayer)

::: notes

"The more you think about what the B in B-trees means, the better you understand B-trees."

--McCreight

:::

## B-Tree organization

### Properties

* Balanced tree that consists of nodes
* Each node is a combination of pointers and items
* The *degree* of a tree is the minimum number of items that a node (except the root) can contain
* The *capacity* is the maximum number of items that a node can contain
* Items in a node are stored in increasing order of their *keys*
  * First value in the tuple
  * The second value is the record id (offset within a file)
* A pointer to the **left** of an *item* points to a node with smaller items
* A pointer to the **right** of an *item* points to a node with larger items

### B-Tree example

![B-Tree](images/btree1.png)

### B-Tree advantages

* Multiple indices can be built on a single table
* $O(\log_d{n})$ lookup, where $d$ is the degree of the tree and $n$ is the number of items
* Ordered **sequential** access to the index, as opposed to hashing
* Suitable to store **very large** amounts of data
* As a tree gets wider, access time improves
* Index itself can be a file
* Record can be removed from the tree (index) without rewriting the file (table)
* Tree (index) does not have to be rebuilt

## B-Tree implementation

Wednesday

## B-Tree operations

* Lookup is similar to other search trees
* Insertion can cause splitting
* Removal may cause rebalancing

### B-Tree Insert

### B-Tree Delete

## Summary

* Database background
* B-Tree organization
* B-Tree implementation
* B-Tree operations

## Thank you

Got questions?

## References

* [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
* [B-tree - Wikipedia](https://en.wikipedia.org/wiki/B-tree)
* [Organization and maintenance of large ordered indexes | SpringerLink](https://link.springer.com/article/10.1007%2FBF00288683)
