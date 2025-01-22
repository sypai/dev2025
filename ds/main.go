package main

import ( 
	"fmt"
	"ds/graphs"
)

func main(){
	fmt.Println("Here we go again!\n\n")

    socialNetwork := graphs.NewGraph(false)

	// Adding People
	socialNetwork.AddVertex("Suyash")
	socialNetwork.AddVertex("Aakshita")
	socialNetwork.AddVertex("Shriya")
	socialNetwork.AddVertex("Sherlock")
	socialNetwork.AddVertex("Utkarsh")

	// Adding Connections (edges)
	socialNetwork.AddEdge("Suyash", "Aakshita") 
	socialNetwork.AddEdge("Shriya", "Sherlock")
	socialNetwork.AddEdge("Shriya", "Utkarsh")
	socialNetwork.AddEdge("Utkarsh", "Suyash")

	socialNetwork.PrintGraph()
	
}