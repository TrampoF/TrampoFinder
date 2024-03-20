package route

import (
	"JobBoard/Gateway/internal/database"
	"time"
)

type Route struct {
	mongorm         *database.Database
	Path            string        `json:"path" gorm:"type:varchar(255)"`
	ServiceURL      string        `json:"serviceURL" gorm:"type:varchar(255)"`
	Methods         []string      `json:"methods" gorm:"type:json"`
	Headers         []string      `json:"headers" gorm:"type:json"`
	Description     string        `json:"description" gorm:"type:text"`
	IsActive        bool          `json:"isActive"`
	CallCount       int64         `json:"callCount"`
	TotalResponse   time.Duration `json:"totalResponse"`
	RequiredHeaders []string      `json:"requiredHeaders" gorm:"type:json"`
}
