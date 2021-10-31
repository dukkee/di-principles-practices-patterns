from typing import Protocol


class MessageWriter(Protocol):
    def write(self, message: str) -> None:
        ...


class Identity(Protocol):
    is_authenticated: bool


class CurrentUser(Identity):
    @property
    def is_authenticated(self) -> bool:
        return True


class ConsoleMessageWriter(MessageWriter):
    def write(self, message: str) -> None:
        print(message)


class SecurityMessageWriter(MessageWriter):
    _writer: MessageWriter
    _identity: Identity

    def __init__(self, writer: MessageWriter, identity: Identity):
        if writer is None:
            raise ValueError("writer can't be None")
        if identity is None:
            raise ValueError("identity can't be None")

        self._writer = writer
        self._identity = identity

    def write(self, message: str) -> None:
        if self._identity.is_authenticated:
            self._writer.write(message)


class Salutation:
    _writer: MessageWriter

    def __init__(self, writer: MessageWriter):
        if writer is None:
            raise ValueError('Writer can\'t be None')

        self._writer = writer

    def exclaim(self):
        self._writer.write('Hello DI!')


def main():
    writer = SecurityMessageWriter(
        writer=ConsoleMessageWriter(),
        identity=CurrentUser(),
    )
    salutation = Salutation(writer)
    salutation.exclaim()


if __name__ == '__main__':
    main()
