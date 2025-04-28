package main

import (
	"ds/graphs"
	"fmt"
)

func main() {
	fmt.Println("Here we go again!")
	fmt.Println()

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

	website_nav := graphs.NewGraph(true)

	website_nav.AddVertex("Home")
	website_nav.AddVertex("About")
	website_nav.AddVertex("Contact")
	website_nav.AddVertex("Blog")

	website_nav.AddEdge("Home", "About")
	website_nav.AddEdge("Home", "Blog")
	website_nav.AddEdge("About", "Contact")
	website_nav.AddEdge("Blog", "Contact")

	website_nav.PrintGraph()
}
