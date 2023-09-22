# Hash Table Implementations

This repository contains implementations of three different hash table strategies: Multi Hash Table, Cuckoo Hash Table, and D-Left Hash Table. These implementations are meant to illustrate the use of different hash functions and collision resolution strategies.

## Table of Contents

1. [Multi Hash Table](#multi-hash-table)
2. [Cuckoo Hash Table](#cuckoo-hash-table)
3. [D-Left Hash Table](#d-left-hash-table)
4. [Prerequisites](#prerequisites)
5. [Execution](#execution)
6. [Output](#output)

## Multi Hash Table
<a name="multi-hash-table"></a>

This hash table implementation uses multiple hash functions: MD5, SHA-256, and SHA-512, to manage collisions and place the flow IDs effectively. The placement is stopped once an empty slot is found.

### Key Functions and Explanation
- **`generate_unique_flow_ids(num)`:** Generates `num` unique flow IDs.
- **`hash1(flow_id, table_size)`:** Uses MD5 to hash `flow_id`.
- **`hash2(flow_id, table_size)`:** Uses SHA-256 to hash `flow_id`.
- **`hash3(flow_id, table_size)`:** Uses SHA-512 to hash `flow_id`.
- **`multi_hash_table()`:** Main function to insert flow IDs in the table.

## Cuckoo Hash Table
<a name="cuckoo-hash-table"></a>

Cuckoo hashing allows constant worst-case lookup time and efficient utilization of storage with multiple hash functions. It employs three hash functions: MD5, SHA-256, and SHA-1.

### Key Functions and Explanation
- **`cuckoo_insert()`, `cuckoo_move()`, `cuckoo_hash_table()`:** Manage the insertion, rearrangement, and collision resolution in the Cuckoo hash table.

## D-Left Hash Table
<a name="d-left-hash-table"></a>

D-Left hashing reduces collision probability by dividing the table into segments, each having its own hash function. It utilizes four hash functions: MD5, SHA-256, SHA-1, and SHA-512.

### Key Functions and Explanation
- **`d_left_insert()`, `d_left_hash_table()`:** Handle insertion and manage flow IDs in the D-Left hash table.

## Prerequisites
<a name="prerequisites"></a>

- Python 3.x
- No additional packages are required.

## Execution
<a name="execution"></a>

To execute any of the hash table implementations, navigate to the implementation and run:

```sh
python <filename>.py
```
Replace <filename> with the appropriate file name, e.g., multi_hash_table, cuckoo_hash_table, or d_left_hash_table.
## Output
<a name="output"></a>
Each implementation writes the output, including successful inserts and the final state of the table, to a corresponding text file: multihash.txt, cuckoo-hash.txt, and d-hash.txt.


