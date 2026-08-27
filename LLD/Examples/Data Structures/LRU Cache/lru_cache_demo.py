from lru_cache import LRUCache

class LRUCacheDemo:
    @staticmethod
    def main():
        print("=== LRU Cache Demo ===\n")

        cache = LRUCache(3)

        # Test 1: Basic put and get
        print("1. Adding items to cache (capacity = 3)")
        cache.put("a", 1)
        print("   put('a', 1)")
        cache.put("b", 2)
        print("   put('b', 2)")
        cache.put("c", 3)
        print("   put('c', 3)")
        print("   Cache state: {a=1, b=2, c=3}")

        # Test 2: Get operation updates recency
        print("\n2. Accessing 'a' makes it most recently used")
        value_a = cache.get("a")
        print(f"   get('a') = {value_a}")
        print("   Order now: b (LRU) -> c -> a (MRU)")

        # Test 3: Eviction on capacity overflow
        print("\n3. Adding 'd' should evict 'b' (the LRU item)")
        cache.put("d", 4)
        print("   put('d', 4)")

        value_b = cache.get("b")
        print(f"   get('b') = {value_b} (None means evicted)")

        # Test 4: Verify other items still exist
        print("\n4. Verifying other items still accessible")
        print(f"   get('c') = {cache.get('c')}")
        print(f"   get('a') = {cache.get('a')}")
        print(f"   get('d') = {cache.get('d')}")

        # Test 5: Update existing key
        print("\n5. Updating existing key")
        cache.put("c", 30)
        print("   put('c', 30) - updates value and marks as MRU")
        print(f"   get('c') = {cache.get('c')}")

        # Test 6: Add another item, should evict 'a' now
        print("\n6. Adding 'e' should evict 'a' (now the LRU)")
        cache.put("e", 5)
        print("   put('e', 5)")
        print(f"   get('a') = {cache.get('a')} (None means evicted)")
        print(f"   get('d') = {cache.get('d')}")

        print("\n=== Demo Complete ===")

if __name__ == "__main__":
    LRUCacheDemo.main()