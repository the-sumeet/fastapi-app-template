from fastapi import Request


def current_user(request: Request):
    return getattr(request.state, "user", None)
