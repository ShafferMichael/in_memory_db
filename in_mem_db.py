class InMemoryDB:
    def __init__(self):
        self.db = {}               # committed data
        self.transaction = None    # uncommitted changes

    def get(self, key):
        # show only committed state
        return self.db.get(key, None)

    def put(self, key, value):
        if self.transaction is None:
            print("no transaction in progress")
            return
        self.transaction[key] = value

    def begin_transaction(self):
        if self.transaction is not None:
            print("transaction already in progress")
            return
        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            print("no transaction to commit")
            return
        for key, value in self.transaction.items():
            self.db[key] = value
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            print("no transaction to rollback")
            return
        self.transaction = None





if __name__ == "__main__":
    db = InMemoryDB()

    print(db.get("A"))  # none
    db.put("A", 5)       # no transaction in progress

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # still none (not committed)

    db.put("A", 6)
    db.commit()

    print(db.get("A"))  # 6

    db.commit()         # no transaction to commit
    db.rollback()       # no transaction to rollback

    print(db.get("B"))  # None

    db.begin_transaction()
    db.put("B", 10)
    db.rollback()

    print(db.get("B"))  # None
