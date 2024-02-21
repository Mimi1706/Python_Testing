from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def visit_home(self):
        self.client.get("/")

    @task
    def visit_point_board(self):
        self.client.get("/pointBoard")

    @task
    def show_summary(self):
        response = self.client.post("/showSummary", {"email": "john@simplylift.co"})
        if response.status_code != 200:
            response.failure("Failed to show summary")

    @task
    def book(self):
        response = self.client.get("/book/Spring%20Festival/Simply%20Lift")
        if response.status_code != 200:
            response.failure("Failed to book")

    @task
    def purchase_places(self):
        response = self.client.post(
            "/purchasePlaces",
            {
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "10",
            },
        )
        if response.status_code != 200:
            response.failure("Failed to purchase places")

    @task
    def logout(self):
        self.client.get("/logout")
