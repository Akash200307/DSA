# Last updated: 2/3/2026, 9:40:21 PM
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)
        
        

        UN=0
        VISITG=1
        VISITD=2
        states=[0]*numCourses

        def dfs(node):
            state=states[node]

            if state==VISITD:
                 return True
            elif state==VISITG:
                 return False

            states[node]=VISITG

            for adj in g[node]:
                if not dfs(adj):
                    return False

            states[node]=VISITD
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False


        return True

            



        

    

       