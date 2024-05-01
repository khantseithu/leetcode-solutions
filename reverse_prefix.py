class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
        """
        if ch not in word:
            return word
        i = word.index(ch)
        return word[:i + 1][::-1] + word[i + 1:]
