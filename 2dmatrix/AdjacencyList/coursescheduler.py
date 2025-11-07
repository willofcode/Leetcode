'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.


Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]
Output: true


Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false


class solution:
    def courseschedule(numCourses, prerequisites):
        row = len(prerequisites)
        col = len(prerequisites[0])
        
        visited = set()
        dfs():
            traverse the graph
            track the visited 
            -> 1,0 -> 0,1
            
            for r in range(row):
                for c in range(col):
                    [0,1] if this only course requisite it must true
                    [0,1],[1,0] because we define 1 must be taken before 0, the second subarray is contradiction
                    
[[1, 3], [2, 3], [1, 2]] -> this is true, because of levels within the courses

1: 3, 2
2: 3
3: 
4: 5
5: 
       1
      /  \ 
     3     2      4 -> 5
           
          
             
         


[[3, 1], [2, 3], [1, 2]] -> [2, 3]-> [1, 2] -> [3, 1] this false this creates a cycle

1: 2
2: 3
3: 1

        1 
       ^ 
       |   \
             
       |    2 
       |     \ 
       |_____ 3 



transform prereq to adjacency list

dfs(course): 

base case: 
- is it in visited
    - return false
- when a course does not have prereqs => adj_list[course] = []
    - return true
- stopping condition

recursive case:
add the course to visited

for pre_course in adj_list[course]:

    if not dfs(pre_course):
        return false

visited.remove(course)
adj_list[course] = []
return true

implementation for DFS
alternage implementation Top sort
'''
def course_schedule(numCourses, prerequisites): #3, [[0, 2], [1, 2], [0, 1]]

    preMap = defaultdict(list)
    for courses in prerequisites:
        preMap[course[0]].append(course[1]) 
    '''
    0: 2, 1
    1: 
    2:  
    '''
    
    visited = set() 
    def dfs(course): #1

        if course in visited: #
            return False
        
        if preMap[course] == []:
            return True
        
        visited.add(course) # {0, 1}
        for pre in preMap[course]:
            if not dfs(pre): #1 
                return False 
        
        visited.remove(course) #{0}
        preMap[course] = []
        return True 
    
    for c in range(numCourses):
        if not dfs(c):
            return False 

    return True

  # time complexity: O(V + E)
  # space complexity: O(V + E)
