from fastapi import Request, Depends


def current_user(request: Request):
    return getattr(request.state, 'user', None)
