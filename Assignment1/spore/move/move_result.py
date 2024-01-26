class MoveResult:
    def __init__(self, stamina_usage: int = 0, speed: int = 0) -> None:
        self.stamina_usage = stamina_usage
        self.speed = speed

    def get_stamina_usage(self) -> int:
        return self.stamina_usage

    def get_speed(self) -> int:
        return self.speed
