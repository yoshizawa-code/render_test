import datetime

REWORD_AMOUNT = 999

class BlockChain(object):

    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.chain = {"blocks": []}

    def add_transaction_pool(self, transaction):
        transaction_dict = transaction.dict()
        self.transaction_pool["transactions"].append(transaction_dict)
    
    def create_new_block(self, creator):
        time = datetime.datetime.now().isoformat()
        reword_transaction_dict = {
            "time": time,
            "sender": "Blockchain",
            "receiver": creator,
            "amount": REWORD_AMOUNT,
            "description": "reword",
            "signature": "not need"
        }

        transactions = self.transaction_pool["transactions"].copy()
        transactions.append(reword_transaction_dict)

        block = {
            "time":time,
            "transactions":transactions,
            "hash":"hash_sample",
            "nonce":0
        }

        self.chain["blocks"].append(block)
        self.transaction_pool["transactions"] = []