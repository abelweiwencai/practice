package main

import (
    "fmt"
    "encoding/json"
)

func HandleJson() error {

	jsonV := `
	{
		"user": {
		  "mspid": "admin",
		  "email": "admin@domain.com"
		}
	  }`
    byteValue := []byte(jsonV) 
    // We have known the outer json object is a map, so we define  result as map.
	// otherwise, result could be defined as slice if outer is an array
	
    var result map[string]interface{}
    err := json.Unmarshal(byteValue, &result)
    if err != nil {
        return err
    }

    // handle peers

	result["mspid"] = "aaaaaaaaaaaaa"

	fmt.Println(result)
    // Convert golang object back to byte
    byteValue, err = json.Marshal(result)
    if err != nil {
        return err
    }
    return err
}

func main() {
	HandleJson()	
}