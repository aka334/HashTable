import random
import hashlib

def generate_unique_flow_ids(num):
    flow_ids = set()
    while len(flow_ids) < num:
        flow_id = random.randint(1, 10**6)
        flow_ids.add(flow_id)
    return list(flow_ids)

def hash1(flow_id, table_size):
    m = hashlib.md5()
    m.update(str(flow_id).encode('utf-8'))
    return int(m.hexdigest(), 16) % table_size

def hash2(flow_id, table_size):
    s = hashlib.sha256()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

def hash3(flow_id, table_size):
    s = hashlib.sha1()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

def hash4(flow_id, table_size):
    s = hashlib.sha512()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

def d_left_insert(flow_id, table, segment_size, hash_funcs):
    for i, func in enumerate(hash_funcs):
        start_idx = i * segment_size
        pos = start_idx + func(flow_id, segment_size)
        if table[pos] == 0: 
            table[pos] = flow_id  
            return 

def d_left_hash_table(num_entries, num_flows, num_hashes):
    segment_size = num_entries // num_hashes
    table = [0] * num_entries
    flow_ids = generate_unique_flow_ids(num_flows)
    hash_funcs = [hash1, hash2, hash3, hash4]
    successful_inserts = 0
    
    for flow_id in flow_ids:
        initial_table = list(table)  # copy the initial state of the table
        d_left_insert(flow_id, table, segment_size, hash_funcs)
        if table != initial_table:  # if the table has changed, flow was inserted successfully
            successful_inserts += 1
    
    with open("d-hash.txt", "w") as f:
        f.write(str(successful_inserts) + "\n")
        for entry in table:
            f.write(str(entry) + "\n")

if __name__ == "__main__":
    d_left_hash_table(1000, 1000, 4)
