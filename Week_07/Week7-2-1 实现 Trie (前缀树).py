# Time: O(N)
# Space: O(N)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        # insert each char in correct posititon and then move my curr
        current = self.root
        for i in range(len(word)):
            char = word[i]
            if current.children[ord(char) - ord('a')] == None:
                current.children[ord(char) - ord('a')] = TrieNode()
            current = current.children[ord(char) - ord('a')]  # move my current to that charcter

        current.isEnd = True  # end insert True meaning the word is in tree

    # Search for a char if not there then return False or if there move my curr
    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for i in range(len(word)):
            char = word[i]
            if current.children[ord(char) - ord('a')] == None:
                return False  # that character is not present in that children
            current = current.children[ord(char) - ord('a')]

        return current.isEnd  # wheather the char is true or false that what we are returning

    # Search for a prefix if not there then return False or if there move my curr till my prefix ends and return True
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if current.children[ord(char) - ord('a')] == None:
                return False  # that character is not present in that children
            current = current.children[ord(char) - ord('a')]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)