import random
import hashlib

# Function to generate unique flow IDs
def generate_unique_flow_ids(num):
    flow_ids = set()
    while len(flow_ids) < num:
        flow_id = random.randint(1, 10**6)
        flow_ids.add(flow_id)
    return list(flow_ids)

# First hash function using MD5
def hash1(flow_id, table_size):
    m = hashlib.md5()
    m.update(str(flow_id).encode('utf-8'))
    return int(m.hexdigest(), 16) % table_size

# Second hash function using SHA256
def hash2(flow_id, table_size):
    s = hashlib.sha256()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

# Third hash function using SHA1
def hash3(flow_id, table_size):
    s = hashlib.sha1()
    s.update(str(flow_id).encode('utf-8'))
    return int(s.hexdigest(), 16) % table_size

# Function to attempt to insert a flow ID in the Cuckoo hash table
def cuckoo_insert(flow_id, table, hash_funcs, cuckoo_steps):
    # Calculate hash positions using all hash functions
    hash_positions = [func(flow_id, len(table)) for func in hash_funcs]
    # Check for available positions in the table
    for pos in hash_positions:
        if table[pos] == 0:
            table[pos] = flow_id
            return True
            
    # Attempt to relocate existing elements and insert the new flow ID
    for i, pos in enumerate(hash_positions):
        if cuckoo_move(table, flow_id, hash_positions, i, cuckoo_steps):
            return True
    return False

# Function to move existing flow ID and place the new flow ID in the table
def cuckoo_move(table, flow_id, hash_positions, idx, cuckoo_steps):
    if cuckoo_steps == 0:
        return False  # Base case: exhausted cuckoo steps
    
    pos = hash_positions[idx]
    displaced_flow_id = table[pos]
    displaced_hash_positions = [func(displaced_flow_id, len(table)) for func in hash_funcs]
    table[pos] = flow_id  # Temporarily place the new flow ID in the table
    
    # Find available position for displaced flow ID or move its neighbors
    for i, new_pos in enumerate(displaced_hash_positions):
        if new_pos == pos:
            continue  # Skip the current position
        if table[new_pos] == 0 or cuckoo_move(table, displaced_flow_id, displaced_hash_positions, i, cuckoo_steps - 1):
            table[new_pos] = displaced_flow_id
            return True
    # Revert the temporary placement if failed to find a position for the displaced flow ID
    table[pos] = displaced_flow_id
    return False

# Function to create a Cuckoo hash table and insert flow IDs
def cuckoo_hash_table(num_entries, num_flows, cuckoo_steps):
    table = [0] * num_entries  # Initialize the hash table
    flow_ids = generate_unique_flow_ids(num_flows)  # Generate unique flow IDs
    global hash_funcs
    hash_funcs = [hash1, hash2, hash3]  # List of hash functions
    successful_inserts = 0  # Counter for successful inserts
    
    for flow_id in flow_ids:
        if cuckoo_insert(flow_id, table, hash_funcs, cuckoo_steps):
            successful_inserts += 1  # Increment counter if insertion is successful
    
    # Write the results to a file
    with open("cuckoo-hash.txt", "w") as f:
        f.write(str(successful_inserts) + "\n")
        for entry in table:
            f.write(str(entry) + "\n")

# Execute the function to create Cuckoo hash table
if __name__ == "__main__":
    cuckoo_hash_table(1000, 1000, 10)
