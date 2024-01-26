class HashTable:
    def __init__(self, size: int):
        self.size: int = size
        self.table: list[list[tuple[str, any]]] = [[] for _ in range(self.size)]

    def hash_function(self, key: str) -> int:
        return hash(key) % self.size

    def insert(self, key: str, value: any) -> bool | None:
        key_hash: int = self.hash_function(key=key)
        key_value: tuple[str, any] = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key: str) -> bool | None:
        key_hash: int = self.hash_function(key=key)

        if self.table[key_hash] is None:
            return True
        else:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True

    def get(self, key: str):
        key_hash = self.hash_function(key=key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))  # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

H.delete("banana")
print(H.table)

print(H.hash_function("test"))
