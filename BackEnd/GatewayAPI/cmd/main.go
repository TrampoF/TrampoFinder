package main

import (
	"JobBoard/Gateway/internal/database"
	"JobBoard/Gateway/pkg/logging"
	"go.uber.org/zap"
	"log"
	"net/http"
)

func main() {
	logger, err := logging.NewLogger()
	if err != nil {
		// handle error
		logger.Error("Error initializing logger: %v\n", zap.Error(err))
		return
	}

	db, err := database.Connect()
	if err != nil {
		logger.Fatal("Failed to initialize database", zap.Error(err))
	}

	router, err :=

	srv := &http.Server{
		Addr: ":8080",
		Handler: router
	}

	// Graceful server shutdown - https://github.com/gin-gonic/examples/blob/master/graceful-shutdown/graceful-shutdown/server.go
	go func() {
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("Failed to initialize server: %v\n", err)
		}
	}()
}
