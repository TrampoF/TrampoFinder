package database

import (
	"context"
	"go.mongodb.org/mongo-driver/bson"
)

func (db *Database) Create(ctx context.Context, collectionName string, model interface{}) (interface{}, error) {
	collection := db.DB.Collection(collectionName)

	res, err := collection.InsertOne(ctx, model)
	if err != nil {
		return nil, err
	}

	return res, nil
}

func (db *Database) Read(ctx context.Context, collectionName string, filter interface{}, result interface{}) (interface{}, error) {
	collection := db.DB.Collection(collectionName)

	err := collection.FindOne(ctx, filter).Decode(&result)
	if err != nil {
		return nil, err
	}

	return result, nil
}

func (db *Database) FindAll(ctx context.Context, collectionName string, results []interface{}) ([]interface{}, error) {
	collection := db.DB.Collection(collectionName)
	cur, err := collection.Find(ctx, bson.M{})
	if err != nil {
		return nil, err
	}

	if err = cur.All(context.Background(), &results); err != nil {
		return nil, err
	}

	return results, nil
}

func (db *Database) Update(ctx context.Context, collectionName string, filter interface{}, update interface{}) (interface{}, error) {
	collection := db.DB.Collection(collectionName)

	_, err := collection.UpdateOne(ctx, filter, update)
	if err != nil {
		return nil, err
	}

	return update, nil
}

func (db *Database) Delete(ctx context.Context, collectionName string, filter interface{}) error {
	collection := db.DB.Collection(collectionName)
	_, err := collection.DeleteOne(ctx, filter)
	if err != nil {
		return err
	}

	return nil
}
