from distutils.util import strtobool


def is_user_registered():
    """
    Ask if user is they are already registered.

    Returns
    -------
    is_registered: bool
        True if already registered, False otherwise.
    """
    is_registered_str = input('Do you already own an account? Yes or No?')
    try:
        is_registered = bool(strtobool(is_registered_str))
    except ValueError:
        print("Oops you must enter \'Yes\' or \'No\'")
        return is_user_registered()
    return is_registered
