from fastapi import Depends, Request


def current_user(request: Request):
    return getattr(request.state, "user", None)
