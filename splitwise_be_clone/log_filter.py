from crum import get_current_user


def add_my_custom_attribute(record):
    if "user_id" not in dir(record):
        record.user_id = (
            get_current_user().pk if get_current_user() is not None else "AnonymousUser"
        )
    return True
