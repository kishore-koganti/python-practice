import time

class CircuitBreaker:
    def __init__(self, max_failures=3, reset_timeout=10):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.is_circuit_open = False

    def execute(self, func, *args, **kwargs):
        if self.is_circuit_open:
            return None  # Circuit is open, don't execute the function

        try:
            result = func(*args, **kwargs)
            self.reset()
            return result
        except Exception as e:
            print(f"Exception: {e}")
            self.handle_failure()
            return None

    def handle_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.max_failures:
            self.open_circuit()

    def open_circuit(self):
        self.is_circuit_open = True
        self.last_failure_time = time.time()
        print("Circuit is open. Waiting for reset timeout...")

    def reset(self):
        if self.is_circuit_open and time.time() - self.last_failure_time > self.reset_timeout:
            print("Circuit is closed.")
            self.is_circuit_open = False
            self.failure_count = 0
            self.last_failure_time = None

# Example usage:
def potentially_failing_function():
    if time.time() % 2 == 0:
        raise ValueError("This is a simulated failure.")
    return "Function executed successfully."

circuit_breaker = CircuitBreaker()

for _ in range(10):
    result = circuit_breaker.execute(potentially_failing_function)
    if result is not None:
        print(result)
    time.sleep(1)
