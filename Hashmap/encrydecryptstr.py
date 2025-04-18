class Encrypter:
    # def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
    #     # build direct encryption map: char -> 2‐char code
    #     self.encmap = {keys[i]: values[i] for i in range(len(keys))}
        
    #     # precompute, for each dict word, its encrypted form (if possible)
    #     # and count how many words map to that encrypted string
    #     self.count = {}
    #     for word in dictionary:
    #         e = self.encrypt(word)
    #         if e:  # only count dictionary words that can actually be encrypted
    #             self.count[e] = self.count.get(e, 0) + 1

    #     # time complexity: O(K + D*L) for initialize
    #     # space complexity: O(K + D)

    # def encrypt(self, word1: str) -> str:
    #     # return the encrypted form of word1, or "" if any char has no mapping.
    #     out = []
    #     for c in word1:
    #         code = self.encmap.get(c)
    #         if code is None:
    #             return ""      # cannot encrypt
    #         out.append(code)
    #     return "".join(out)

    #     # time complexity: O(L) for appending
    #     # space complexity: O(L) for storing into list

    # def decrypt(self, word2: str) -> int:
    #     # return how many dictionary words encrypt to exactly word2.
    #     return self.count.get(word2, 0)

    #     # time complexity: O(1) for lookup
    #     # space complexity: O(1) for accessing hashmap

# alternative method

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.hashmap = dict()
        for i in range(len(keys)):
            self.hashmap[keys[i]] = values[i]
        self.dictmap = defaultdict(int)
        for word in dictionary:
            self.dictmap[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        output = ''
        for char in word1:
            output += self.hashmap[char]
        return output

    def decrypt(self, word2: str) -> int:
        return self.dictmap[word2]

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
