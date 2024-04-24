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
        The accounts themselves can be returned in any order.
        """
        graph = {}
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in graph:
                    graph[email] = []
                if email not in email_to_name:
                    email_to_name[email] = name
                if len(graph[email]) > 0:
                    graph[graph[email][0]].append(email)
                    graph[email].append(graph[email][0])
                    graph[email] = [email]
                for i in range(1, len(account) - 1):
                    if account[i] not in graph:
                        graph[account[i]] = []
                    graph[account[i]].append(account[i + 1])
                    if account[i + 1] not in graph:
                        graph[account[i + 1]] = []
                    graph[account[i + 1]].append(account[i])
        visited = set()
        result = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                emails = []
                while stack:
                    node = stack.pop()
                    emails.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                result.append([email_to_name[email]] + sorted(emails))
        return result

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
