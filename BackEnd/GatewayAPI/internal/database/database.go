package database

import (
	"context"
	"fmt"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/x/mongo/driver/connstring"
	"os"
)

type Database struct {
	DB         *mongo.Database
	collection *mongo.Collection
	client     *mongo.Client
}

func Connect() (*Database, error) {
	connString, err := connstring.Parse(os.Getenv("MONGO_URL"))
	client, err := mongo.Connect(context.Background(), options.Client().ApplyURI(os.Getenv("MONGO_URL")))
	if err != nil {
		return nil, fmt.Errorf("could not connect to mongodb: %w", err)
	}

	db := client.Database(connString.Database)
	return &Database{DB: db}, nil
}
