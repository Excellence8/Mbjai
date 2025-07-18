import pytest
from src.main import validate_environment
from unittest.mock import patch

def test_missing_keys():
    with patch.dict('os.environ', clear=True):
        with pytest.raises(ValueError):
            validate_environment()