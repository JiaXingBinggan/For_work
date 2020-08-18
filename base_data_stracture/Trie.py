class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            if letter not in cur: # 要判断字典里是否有这个键
                cur.setdefault(letter, {})
            cur = cur[letter]
        cur['$'] = None # 末尾标记

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for letter in word:
            if letter not in cur: # 要判断字典里是否有这个键
                return False
            cur = cur[letter]
        return '$' in cur

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            if letter not in cur: # 要判断字典里是否有这个键
                return False
            cur = cur[letter]
        return True
# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'apple'
prefix = 'app'
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(obj.root)
print(param_2)
print(param_3)
word = 'append'
prefix = 'ab'
obj.insert(word)
param_4 = obj.search('appen')
param_5 = obj.startsWith(prefix)
print(obj.root)
print(param_4)
print(param_5)