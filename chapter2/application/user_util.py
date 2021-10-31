"""This code part is needed to parse user into controller scope
to simulate ASP.NET Core MVC behavior. It was implemented with
a helper to parse 'role' query parameter and use it to construct
a User object.

"""

from pydantic import BaseModel

__all__ = ['User', 'user_role']


class User(BaseModel):
    role: str

    def is_in_role(self, role: str) -> bool:
        return self.role == role


async def user_role(role: str = '') -> User:
    return User(role=role)
