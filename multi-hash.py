import random
import hashlib

def generate_unique_flow_ids(num):
    """Generate unique flow IDs."""
    flow_ids = set()
    while len(flow_ids) < num:
        flow_id = random.randint(1, 10**6)
        flow_ids.add(flow_id)
    return list(flow_ids)

def hash1(flow_id, table_size):
    """First hash function using md5."""
    m = hashlib.md5()
    m.update(str(flow_id).encode('utf-8'))
    return int(m.hexdigest(), 16) % table_size

def hash2(flow_id, table_size):
    """Second hash function using sha256."""
    s = hashlib.sha256()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

def hash3(flow_id, table_size):
    """Third hash function using sha512."""
    s = hashlib.sha512()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

def multi_hash_table(num_entries, num_flows, num_hashes):
    """Multi-hash table function."""
    table = [0] * num_entries
    flow_ids = generate_unique_flow_ids(num_flows)
    
    # print(flow_ids)
    for flow_id in flow_ids:
        positions = set([
            hash1(flow_id, num_entries),
            hash2(flow_id, num_entries),
            hash3(flow_id, num_entries)
        ])
        for pos in positions:
            if table[pos] == 0:
                table[pos] = flow_id
                break

    # Write output to file
    with open("multihash.txt", "w") as f:
        valid_flows = len([i for i in table if i != 0])
        f.write(str(valid_flows) + "\n")
        for entry in table:
            f.write(str(entry) + "\n")

if __name__ == "__main__":
    multi_hash_table(1000, 1000, 3)
