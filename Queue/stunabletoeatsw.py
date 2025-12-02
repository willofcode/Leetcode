from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        u: for each sw and student in queue, sw is stacked and student are in rotation meaning enqueue 
        for the sw, if sw and student match, remove student and sw, otherwise remove student and insert
        at the end of queue

        edge case: 
        - does # of sw and # of student are always 1 to 1? (Yes, problem constraints say so)
        - if current sw top of stack has no correspondind student (mismatch causes stalemate early) (Yes, this is the main problem)

        '''
        
        # # Convert the students list to a deque (double-ended queue).
        # # This is efficient for queue operations (popleft() and append()),
        # # which are both O(1) time complexity.
        # q = deque(students)
        
        # # 'i' will be our pointer to the current sandwich at the "top" of the stack.
        # # We use an index instead of popping from the 'sandwiches' list.
        # i = 0
        
        # # 'rotate' is our stalemate detector. It counts how many students in a row
        # # have seen the top sandwich, didn't want it, and moved to the back.
        # rotate = 0
        
        # # We loop as long as two conditions are met:
        # # 1. 'q' is not empty (there are still students left to feed).
        # # 2. 'rotate < len(q)' is our stalemate check.
        # #    If 'rotate' becomes equal to 'len(q)', it means that *every*
        # #    student currently in the queue has cycled past the top sandwich
        # #    at least once, and none of them wanted it. We are stuck.
        # while q and rotate < len(q):
            
        #     # Check if the student at the front of the line wants the top sandwich
        #     if q[0] == sandwiches[i]:
        #         # --- MATCH ---
        #         # The student takes the sandwich. Remove them from the front of the queue.
        #         q.popleft()
        #         # Move our pointer to the next sandwich in the stack.
        #         i += 1
        #         # **CRITICAL**: A student was successfully fed.
        #         # This breaks any potential stalemate, so we reset the
        #         # 'rotate' counter back to 0.
        #         rotate = 0
        #     else:
        #         # --- MISMATCH ---
        #         # The student does not want this sandwich.
        #         # Move the student from the front (q.popleft())
        #         # to the back (q.append(...)) of the queue.
        #         q.append(q.popleft())
        #         # Increment our stalemate counter. We have seen one more
        #         # student rotate past this sandwich unsuccessfully.
        #         rotate += 1
        
        # # The loop terminates for one of two reasons:
        # # 1. q is empty (len(q) == 0). Everyone ate. We return 0.
        # # 2. rotate == len(q). A stalemate was reached.
        # #    We return the number of students left in the queue (len(q)).
        # return len(q)

        # alternative implementation
        n = len(students)
        q = deque(students)

        res = n
        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                break
        return res
        
        # time complexity: O(n^2)
        # space complexity: O(n)
        
        # alternate implementation with frequency count
        
#        res = len(students)
#        cnt = Counter(students)
#
#        for s in sandwiches:
#            if cnt[s] > 0:
#                res -= 1
#                cnt[s] -= 1
#            else:
#                break
#
#        return res

        # time complexity: O(n)
        # space complexity: O(1)
        
