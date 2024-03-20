package route

import "context"

func (r *Route) GetRoutes() ([]*Route, error) {
	var routes []Route
	r.mongorm.FindAll(context.Background(), "routes", &routes)
}
