"""
mlte/user/model.py

Model implementation for a User.
"""

from typing import Optional

from mlte.model import BaseModel


class BasicUser(BaseModel):
    """A model class representing a user of the system"""

    username: str
    """The username to uniquely identify a user."""

    email: Optional[str] = None
    """An optional email associated to the user."""

    full_name: Optional[str] = None
    """The full name of the user."""

    disabled: bool = False
    """Whether the user is disabled."""


class User(BasicUser):
    """User with additional information only used locally when stored."""

    hashed_password: str
    """The hashed password of the user."""


class UserCreate(BasicUser):
    """User with additional information only used when creating a user."""

    password: str
    """The plain password of the user."""
