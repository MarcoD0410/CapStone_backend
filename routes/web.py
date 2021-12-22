"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
     RouteGroup([
        Get("/", "ZooController@index").name("index"),
        Get("/@id", "ZooController@show").name("show"),
        Post("/", "ZooController@create").name("create"),
        Put("/@id", "ZooController@update").name("update"),
        Delete("/@id", "ZooController@destroy").name("destroy")
        
    ], prefix="/zoo", name="zoo")
]
