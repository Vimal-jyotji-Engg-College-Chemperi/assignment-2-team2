# Ring Election Algorithm - Lab Program with User Input

def ring_election(nodes, initiator):

    if initiator not in nodes:
        print("❌ Initiator not found in nodes")
        return

    n = len(nodes)
    start = nodes.index(initiator)
    message = []

    print("\n⚡ Election started by Node:", initiator)

    i = start

    # Pass message around the ring
    while True:
        message.append(nodes[i])
        print("Node", nodes[i], "sends message", message)

        i = (i + 1) % n

        if i == start:
            break

    # Highest ID becomes leader
    leader = max(message)

    print("\n🏆 Leader elected is Node:", leader)

    # Coordinator announcement
    print("\n📢 Coordinator message passing:")

    i = start
    while True:
        print("Node", nodes[i], "acknowledges Leader", leader)

        i = (i + 1) % n

        if i == start:
            break


# ---------------- MAIN PROGRAM ----------------

print("=== Ring Election Algorithm ===")

# Number of nodes
n = int(input("Enter number of nodes: "))

nodes = []

# Node IDs input
print("Enter unique node IDs:")
for i in range(n):
    node_id = int(input(f"Node {i+1} ID: "))
    nodes.append(node_id)

# Initiator input
initiator = int(input("Enter initiator node ID: "))

# Run election
ring_election(nodes, initiator)