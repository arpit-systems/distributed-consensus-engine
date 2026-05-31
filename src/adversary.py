class AdversaryNode:

    def __init__(self, node_id):
        self.node_id = node_id

    def send_fake_message(self):
        print(f"Adversary Node {self.node_id} sent conflicting transaction")