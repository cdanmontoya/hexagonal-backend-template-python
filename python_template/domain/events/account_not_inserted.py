from domain.events.event import Event


class AccountNotInserted(Event):
    def __init__(
        self, data: str, source: str = "python_template", version: str = "1.0.0"
    ) -> None:
        super().__init__(source, version, data)
