'''In this program I want to implement the breadth first search algorithm,
Pseudo code can be found here: https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/the-breadth-first-search-algorithm'''

class Queue:
    def __init__(self, queue = []):
        self.queue = queue

    def getQueue(self):
        return self.queue

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        try:
            self.queue.pop()
        except IndexError as error:
            print("List is empty so cannot dequeue")

    def getLast(self):
        return self.queue[len(self.queue) - 1]


#This function takes a graph represented by an adjency list (that is a list of all vertices' nearest neighbours:
#so the first element will be a list of neighbours of vertex 0, and the second a list of neighbours of vertex 1 etc)
#It also takes a source which is the index of the source vertex. The function outputs for each vertex the shortest
#distance to source and its predecessor.

def BreadthFirstSearch(graph, source):

    bfs_info = []
    #This will be a list of pairs of numbers [distance,predecessor] where the first index represents shortest distance
    #to source and 2nd index represents the predecessor, ie the previous node on the shortest path

    for i in range(len(graph)):
        bfs_info.append([None, None])

    #Intilally have bfs_info filled with None. Why? Well how do we know which vertex has
    #already been visited? If the distance is None then vertex hasn't yet been visited and
    #we update it once we visit it. Intially we update the source distance to 0:
    bfs_info[source][0] = 0

    #How to keep track of which vertices have already been visited but have not yet been visited from?
    #We use a queue. Whenever we visit a vertex for the first time we enqueue it. To the decide which
    #vertex to visit next we chose the one that has been the longest in the queue. ie the one which is
    #gone after dequeing, (we get that using the getLast() method)
    queue = Queue()
    queue.enqueue(source)

    while not queue.isEmpty(): #while the queue is not empty
        u = queue.getLast() #gets the last element of queue, or the vertex we are currently at
        queue.dequeue() #dequeue this vertex because by the end of the for loop we will have looked at all u's neighbours

        for i in range(len(graph[u])): # recall graph[u] represents all the vertices neighbouring to vertex u in the graph
            v = graph[u][i]            # so for each of those neighbours we give the neighbour a name v.

            if bfs_info[v][0] == None:  #then we check if v's distance is None - ie if it hasn't been visited yet
                bfs_info[v][0] = bfs_info[u][0] + 1 #we let v's shortest distance = the shortest distance of u (its predecessor) + 1
                bfs_info[v][1] = u #and set v's predecessor as u
                queue.enqueue(v) #finally we enqueue v since we will have to look at all it's neighbours later and repeat the same procedure

        #print(queue.getQueue()) #for testing and seeing how algorithm works
        #print(bfs_info)

    return bfs_info



if __name__ == '__main__':

    adjList = [[1],[0, 4, 5],[3, 4, 5],[2, 6],[1, 2],[1, 2, 6],[3, 5],[]]
    result = BreadthFirstSearch(adjList, 3)
    print(result)
    #This gives [[4, 1], [3, 4], [1, 3], [0, None], [2, 2], [2, 2], [1, 3], [None, None]] as expected for this graph
    adjList2 = [[1,2],[3,4],[3,4],[5],[5],[]]
    result2 = BreadthFirstSearch(adjList2, 0)
    print(result2)
    #This gives [[0, None], [1, 0], [1, 0], [2, 1], [2, 1], [3, 3]]
