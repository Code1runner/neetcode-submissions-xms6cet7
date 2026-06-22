class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        while students_queue:
            if sandwiches_queue[0] not in students_queue:
                break
            s = students_queue.popleft()
            if s == sandwiches_queue[0]:
                sandwiches_queue.popleft()
            else:
                students_queue.append(s)
    
        return len(students_queue) 