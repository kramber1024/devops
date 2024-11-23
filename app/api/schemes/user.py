from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints

from app.core.database import models

type _FirstName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=64,
        max_length=64,
    ),
    Field(
        description="Имя пользователя.",
        examples=["Иван"],
    ),
]

type _LastName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=64,
        max_length=64,
    ),
    Field(
        description="Фамилия пользователя.",
        examples=["Doe"],
    ),
]


class CreateUser(BaseModel):
    first_name: _FirstName
    last_name: _LastName


type Id = Annotated[
    int,
    Field(
        description="Идентификатор.",
        examples=[123],
    ),
]


class User(CreateUser):
    id: Id

    @classmethod
    def from_model(cls: type["User"], user: models.User) -> "User":
        return cls(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
        )


type _UserList = Annotated[
    list[User],
    Field(
        description="Список пользователей.",
    ),
]

type _UserListLength = Annotated[
    int,
    Field(
        description="Количество пользователей.",
        examples=[123],
    ),
]


class UserList(BaseModel):
    users: _UserList
    length: _UserListLength

    @classmethod
    def from_models(
        cls: type["UserList"],
        users: list[models.User],
    ) -> "UserList":
        return cls(
            users=[User.from_model(user) for user in users],
            length=len(users),
        )
