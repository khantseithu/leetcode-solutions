from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
        which is expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        queue = []
        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            course = queue.pop(0)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return not any(indegree.values())

# Time complexity: O(V + E) where V is the number of courses and E is the number of prerequisites.
# Space complexity: O(V + E) where V is the number of courses and E is the number of prerequisites.

import unittest

class TestCourseSchedule(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_course_schedule(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
        numCourses = 3
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))

if __name__ == '__main__':
    unittest.main()
