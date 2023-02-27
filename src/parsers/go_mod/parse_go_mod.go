package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"golang.org/x/mod/modfile"
)

func build_data_structure(dependencies map[string]string, filePath string) map[string]map[string]string {
	x := make(map[string]map[string]string)

	x[filePath] = make(map[string]string)

	for path, version := range dependencies {
		x[filePath][path] = version
	}

	return x
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a command line argument.")
		return
	}

	filePath := os.Args[1]

	fileContents, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	parsedFile, err := modfile.Parse(filePath, fileContents, nil)
	if err != nil {
		fmt.Println("Error parsing file:", err)
		return
	}

	dependencies := make(map[string]string)
	for _, require := range parsedFile.Require {
		dependencies[require.Mod.Path] = require.Mod.Version
	}

	dataStructure := build_data_structure(dependencies, filePath)

	jsonBytes, err := json.Marshal(dataStructure)
	if err != nil {
		fmt.Println("Error converting to JSON:", err)
		return
	}
	jsonString := string(jsonBytes)
	fmt.Println(jsonString)
}
