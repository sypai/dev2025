package graphs

import "fmt"

// Graph structure using an adjacency list
type Graph struct{
	adjList map[string][]string 
	directed bool // flag to indicate if the graph is directed
}

// NewGraph creates a new empty Graph
func NewGraph(directed bool) *Graph{
	return &Graph{
		adjList: make(map[string][]string),
		directed: directed,
	}
}

// AddVertex adds a new vertex to the graph
func (g *Graph) AddVertex(vertex string) {
	if _, exists := g.adjList[vertex]; !exists{
		g.adjList[vertex] = []string{}
	}
}

// AddEdge adds an edge between two vertices
func (g *Graph) AddEdge(vertex1, vertex2 string){
	// Add edge from v1 -> v2
	g.adjList[vertex1] = append(g.adjList[vertex1], vertex2)

	// If the graph is undirected, add the reverse edge
	if !g.directed{
		g.adjList[vertex2] = append(g.adjList[vertex2], vertex1)
	}
}

func (g *Graph) PrintGraph(){
	graphType := "Undirected"
	if g.directed {
		graphType = "Directed"
	}
	fmt.Printf("%s Graph:\n", graphType)
	for vertex, neighbors := range g.adjList {
		fmt.Printf("%s -> %v\n", vertex, neighbors)
	}
	fmt.Println()
}

