def get_full_name(first_name: str, last_name: str):
    # full_name = f"{first_name.title()} {last_name.title()}"
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("super", "mario"))

def get_name_with_age(name: str, age: int):
    # name_with_age = f"{name} is this old: {age}"
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("super", 35))

def process_items(items: list[str]):
    for item in items:
        print(item)

from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# Pydantic Models - https://docs.pydantic.dev/latest/

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}


user = User(**external_data)
print(user)
print(user.id)

from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

print(say_hello("super"))
print(say_hello.__annotations__)