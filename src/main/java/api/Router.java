package api;

import static spark.Spark.*;

public class Router {

	public static void main(String[] args) {
		get("/", (request, response) -> "Hello World");
	}
}
