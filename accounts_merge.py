from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
        and the rest of the elements are emails representing emails of the account.

        Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts.
        Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
        A person can have any number of accounts initially, but all of their accounts definitely have the same name.

        After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.
        """
        def find(x: str) -> str:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: str, y: str) -> None:
            parent[find(x)] = find(y)

        parent = {}
        owner = {}
        for account in accounts:
            for i in range(1, len(account)):
                parent[account[i]] = account[i]
                owner[account[i]] = account[0]
        for account in accounts:
            for i in range(2, len(account)):
                union(account[i], account[1])
        merged = {}
        for email in parent:
            root = find(email)
            if root not in merged:
                merged[root] = []
            merged[root].append(email)
        return [[owner[k]] + sorted(v) for k, v in merged.items()]


# Time complexity: O(N) where N is the number of emails across all accounts.
# Space complexity: O(N) where N is the number of emails across all accounts.

import unittest

class TestAccountsMerge(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_accounts_merge(self):
        """
        Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        """
        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        self.assertEqual(self.solution.accountsMerge(accounts), [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])


if __name__ == '__main__':
    unittest.main()
