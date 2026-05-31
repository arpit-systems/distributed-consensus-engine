class Node:

    def __init__(self, node_id):
        self.node_id = node_id
        self.is_leader = False
        self.active = True

    def receive_prepare(self):
        print(f"Node {self.node_id} -> PROMISE")

    def receive_accept(self):
        print(f"Node {self.node_id} -> ACCEPTED")


nodes = []

for i in range(1, 6):
    nodes.append(Node(i))


leader = max(nodes, key=lambda x: x.node_id)
leader.is_leader = True

print("Leader Election Complete")
print(f"Leader is Node {leader.node_id}")

transaction = "TX001 : Pay Rs 100"

print("\nClient Sending Transaction...")
print(f"Leader received: {transaction}")

print("\nPAXOS PREPARE PHASE")
print("-------------------")

for node in nodes:

    if node.node_id != leader.node_id:
        print(f"Leader -> Node {node.node_id} : PREPARE")
        node.receive_prepare()

print("\nPAXOS ACCEPT PHASE")
print("------------------")

accepted_count = 1

for node in nodes:

    if node.node_id != leader.node_id:
        print(f"Leader -> Node {node.node_id} : ACCEPT")
        node.receive_accept()
        accepted_count += 1

print("\nCONSENSUS RESULT")
print("----------------")

if accepted_count >= 3:
    print("Majority Reached")
    print("Transaction COMMITTED")
else:
    print("Consensus Failed")