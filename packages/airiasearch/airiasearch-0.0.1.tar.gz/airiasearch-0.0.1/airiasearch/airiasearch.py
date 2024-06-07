class Airiasearch:
    def __init__(self, name: str = "world"):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"