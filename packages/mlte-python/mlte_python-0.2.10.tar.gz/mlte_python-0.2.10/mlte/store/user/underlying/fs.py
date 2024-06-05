"""
mlte/store/artifact/underlying/fs.py

Implementation of local file system artifact store.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import mlte.store.error as errors
from mlte.store.base import StoreURI
from mlte.store.common.fs import JsonFileStorage, parse_root_path
from mlte.store.user.store import UserStore, UserStoreSession
from mlte.user.model import BasicUser, User, UserCreate
from mlte.user.model_logic import convert_to_hashed_user, update_user

BASE_USERS_FOLDER = "users"
"""Base fodler to store users in."""


# -----------------------------------------------------------------------------
# FileSystemUserStore
# -----------------------------------------------------------------------------


class FileSystemUserStore(UserStore):
    """A local file system implementation of the MLTE user store."""

    def __init__(self, uri: StoreURI) -> None:
        super().__init__(uri=uri)

        self.storage = JsonFileStorage()
        """The underlying storage for the store."""

        # Initialize default user.
        self._init_default_user()

    def session(self) -> FileSystemUserStoreSession:
        """
        Return a session handle for the store instance.
        :return: The session handle
        """
        return FileSystemUserStoreSession(self.uri.uri, storage=self.storage)


# -----------------------------------------------------------------------------
# FileSystemUserStoreSession
# -----------------------------------------------------------------------------


class FileSystemUserStoreSession(UserStoreSession):
    """A local file-system implementation of the MLTE user store."""

    def __init__(self, uri: str, storage: JsonFileStorage) -> None:
        self.storage = storage
        """A reference to underlying storage."""

        self.root = parse_root_path(uri)
        """The remote artifact store URL."""

        if not self.root.exists():
            raise FileNotFoundError(
                f"Root data storage location does not exist: {self.root}."
            )

        try:
            self.storage.create_folder(self._base_path())
        except FileExistsError:
            # If it already existed, we just ignore warning.
            pass

    def close(self) -> None:
        """Close the session."""
        # Closing a local FS session is a no-op.
        pass

    # -------------------------------------------------------------------------
    # CRUD Elements
    # -------------------------------------------------------------------------

    def create_user(self, user: UserCreate) -> User:
        if self._user_path(user.username).exists():
            raise errors.ErrorAlreadyExists(f"User '{user.username}'")

        new_user = convert_to_hashed_user(user)
        return self._write_user(new_user)

    def edit_user(self, user: Union[UserCreate, BasicUser]) -> User:
        if not self._user_path(user.username).exists():
            raise errors.ErrorNotFound(f"User '{user.username}'")

        updated_user = update_user(self._read_user(user.username), user)
        return self._write_user(updated_user)

    def read_user(self, username: str) -> User:
        return self._read_user(username)

    def list_users(self) -> List[str]:
        return [
            self.storage.get_just_filename(user_path)
            for user_path in self.storage.list_json_files(self._base_path())
        ]

    def delete_user(self, username: str) -> User:
        self._ensure_user_exists(username)
        user = self._read_user(username)
        self.storage.delete_file(self._user_path(username))
        return user

    # -------------------------------------------------------------------------
    # Internal helpers.
    # -------------------------------------------------------------------------

    def _base_path(self) -> Path:
        """Returns the base path for storing."""
        return Path(self.root, BASE_USERS_FOLDER)

    def _ensure_user_exists(self, username: str) -> None:
        """Throws an ErrorNotFound if the given user does not exist."""
        if not self._user_path(username).exists():
            raise errors.ErrorNotFound(f"User {username}")

    def _read_user(self, username: str) -> User:
        """
        Lazily construct a User object on read.
        :param username: The username
        :return: The user object
        """
        self._ensure_user_exists(username)
        return User(**self.storage.read_json_file(self._user_path(username)))

    def _write_user(self, user: User) -> User:
        """Writes a user to storage."""
        self.storage.write_json_to_file(
            self._user_path(user.username),
            user.model_dump(),
        )
        return user

    def _user_path(self, username: str) -> Path:
        """
        Gets the full filepath for a stored user.
        :param username: The user identifier
        :return: The formatted path
        """
        return Path(self._base_path(), self.storage.add_extension(username))

    def _user_name(self, user_path: Path) -> str:
        """
        Gets the name of a user given a full filepath.
        :param username: The full path
        :return: The username
        """
        return self.storage.get_just_filename(user_path)
