import time
from locust import HttpUser, task, between, events, constant

class RandomHashMachineUser(HttpUser):
    wait_time = constant(1)  # 1 second wait time between tasks

    @task
    def test_endpoint2(self):
        response = self.client.get("/endpoint2")
        if response.status_code == 200:
            data = response.json()
            print(f"Example of SHA-256 hash:\n{data['hash']}")
            last_char = data["hash"][-1]
            if last_char.isdigit():
                if int(last_char) % 2 == 0:
                    print(f"The last 4 character are `{last_char}`. This is an even number. Does not Pass.")
                else:
                    print(f"The last 4 character are `{last_char}`. This is a number and odd number. Pass!")
            else:
                print(f"The last 4 character are `{last_char}`. This is an alphabet. Does not Pass.")

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    RandomHashMachineUser.environment = environment

if __name__ == "__main__":
    from locust.main import main
    main()
