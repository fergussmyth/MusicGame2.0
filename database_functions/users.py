import json


class UserNotFound(Exception):
    pass


def get_users():
    """
    Returns list of all users in database.

    Returns
    -------
    users: list[str]
    """
    with open(r'C:\Users\fergg\PycharmProjects\MusicGame2.0\users.json') as json_file:
        users = json.load(json_file)
    return users


def get_user(username):
    """
    Return user with the given username.

    Parameters
    ----------
    username: str

    Returns
    -------
    user: dict

    Raises
    -------
    UserNotFound
        raised if no user exists with given username.
    """
    users = get_users()
    for user in users:
        if user['username'] == username:
            return user

    raise UserNotFound
