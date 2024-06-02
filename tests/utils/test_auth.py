from src.utils.auth import verify_password, get_password_hash
import pytest


def test_verify_password():
    password = "mysecretpassword"
    hashed_password = get_password_hash(password)

    assert verify_password(password, hashed_password) == True
    assert verify_password("wrongpassword", hashed_password) == False
    assert verify_password("", hashed_password) == False
    with pytest.raises(TypeError):
        verify_password(None, hashed_password)