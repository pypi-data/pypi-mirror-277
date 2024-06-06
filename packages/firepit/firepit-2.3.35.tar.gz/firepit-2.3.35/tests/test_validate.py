import uuid
import pytest

from firepit.exceptions import InvalidStixPath
from firepit.exceptions import InvalidViewname
from firepit.validate import validate_name
from firepit.validate import validate_path


@pytest.mark.parametrize(
    'name, expected', [
        ('foo', True),
        ('[*]', False),
        ('__tmp_6668fcc6300f40e39c255c6573d79180', True),
        ('__tmp_' + uuid.uuid4().hex, True),
        ('foo;', False),
        ('foo; --', False),
        ('network-traffic', True),
        ('x509-certificate', True),
        ("admin'--", False),
        ('admin"--', False),
        ('foo OR "1" = "1', False),
        ('ipv4-addr" union select * from "user-account', False),
        ('foo; select value from "ipv4-addr', False),
    ]
)
def test_validate_name(name, expected):
    if expected:
        validate_name(name)
    else:
        with pytest.raises(InvalidViewname):
            validate_name(name)


@pytest.mark.parametrize(
    'path, expected', [
        ('foo', True),
        ('things[*]', True),
        ('one.two', True),
        ('foo;', False),
        ('foo; --', False),
        ('foo."bar"', False),
        ('ipv4_addr:value', False),
        ("hashes.'SHA-256'", True),
        ("values[*].name", True),
        ("extensions.'http-request-ext'.request_headers.'Content-Type'", True),
        ("ipv4-addr:value", True),
        ("file:hashes.'SHA-1'", True),
        ("file:hashes.IMPHASH", True),
        ("windows-registry-key:values[*].data", True),
        ("network-traffic:protocols[*]", True),
        ("src_port", True),
        ("x_unique_id", True),
        ("admin'--", False),
        ('admin"--', False),
        ('foo OR "1" = "1', False),
        ('ipv4-addr" union select * from "user-account', False),
        ('foo; select value from "ipv4-addr', False),
        ('x-qradar:high_level_category_id', True),
        ('high_level_category_id', True),
        ("x_com_ibm_ariel.cre_event_list[*]", True), # old stix-shifter qradar weirdness
    ]
)
def test_validate_path(path, expected):
    if expected:
        validate_path(path)
    else:
        with pytest.raises(InvalidStixPath):
            validate_path(path)
