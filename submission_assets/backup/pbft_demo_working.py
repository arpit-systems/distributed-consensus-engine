from adversary import AdversaryNode

class Node:

    def __init__(self, node_id):
        self.node_id = node_id

    def pbft_prepare(self):
        print(f"Node {self.node_id} -> PREPARE")

    def pbft_commit(self):
        print(f"Node {self.node_id} -> COMMIT")


nodes = []

for i in range(1, 6):
    nodes.append(Node(i))

print("PBFT MODE")
print("==========")

print("\nPRE-PREPARE PHASE")
print("-----------------")
print("Primary Node -> TX001 : Pay Rs 100")

print("\nPREPARE PHASE")
print("-------------")

for node in nodes:
    node.pbft_prepare()

print("\nBYZANTINE ATTACK")
print("----------------")

adversary = AdversaryNode(99)
adversary.send_fake_message()

print("Signature Verification Failed")
print("Ignoring Malicious Node")

print("\nCOMMIT PHASE")
print("------------")

for node in nodes:
    node.pbft_commit()

print("\nPBFT RESULT")
print("-----------")
print("Transaction COMMITTED")