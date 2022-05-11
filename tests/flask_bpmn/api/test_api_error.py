"""Test cases for the __main__ module."""
import io

from flask_bpmn.api.api_error import ApiError


def test_is_jsonable_can_succeed() -> None:
    """It exits with a status code of zero."""
    result = ApiError.is_jsonable("This is a string and should pass json.dumps")
    assert result is True


def test_is_jsonable_can_fail() -> None:
    """It exits with a status code of zero."""
    result = ApiError.is_jsonable(io.StringIO("BAD JSON OBJECT"))
    assert result is False
