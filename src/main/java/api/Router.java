package api;

import static spark.Spark.*;

public class Router {

	private static final int DEFAULT_PORT = 4567;
	
	private static int getHerokuPort() {
		ProcessBuilder pb = new ProcessBuilder();
		String port = pb.environment().get("PORT");
		if (port != null) {
			return Integer.parseInt(port);
		} else {
			return DEFAULT_PORT;
		}
	}
	
	public static void main(String[] args) {
		port(getHerokuPort());
		get("/", (request, response) -> "Hello World");
	}
}
