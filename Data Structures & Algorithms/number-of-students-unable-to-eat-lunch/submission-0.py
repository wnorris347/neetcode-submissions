class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        for i, sandwich in enumerate(sandwiches):
            sandwich_taken = False
            for i in range(len(queue)):
                if queue[0] == sandwich:
                    queue.popleft()
                    sandwich_taken = True
                    break
                else:
                    temp = queue.popleft()
                    queue.append(temp)
            if sandwich_taken == False:
                return len(queue)
        return 0
            

            

