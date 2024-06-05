"""
smoke_test.py
"""

from .decode import decode
from .stuff import print2
from .cue import Cue

# The format for tests is a dict of { "test_name" : value to pass to threefive.decode}
ten_tests = {
    "Base64": "/DAvAAAAAAAA///wBQb+dGKQoAAZAhdDVUVJSAAAjn+fCAgAAAAALKChijUCAKnMZ1g=",
    "Bytes": b"\xfc0\x11\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\x00\x00O%3\x96",
    "Hex String": "0XFC301100000000000000FFFFFF0000004F253396",
    "Hex Literal": 0xFC301100000000000000FFFFFF0000004F253396,
    "Integer": 1439737590925997869941740173214217318917816529814,
    "HTTP/HTTPS Streams": "https://futzu.com/xaa.ts",
    # "Bad" tests are expected to fail.
    "Bad Base64 ": "/DAvAf45AA",
    "Bad File": "/you/me/fake.file",
    "Bad Integer": -0.345,
    " Bad String": "your momma",
}



def json_load_test():
    test_name ="JSON load and encode"
    data='''{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 22,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment_ticks": 0,
        "pts_adjustment": 0.0,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 0,
        "crc": "0x4238aea2"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 37.302567,
        "pts_time_ticks": 3357231
    },
    "descriptors": [],
    "packet_data": {
        "pid": "0x86",
        "program": 1,
        "pts_ticks": 3354228,
        "pts": 37.2692
    }
}
'''
    print(test_name)
    print(data)
    cue = Cue()
    cue.load(data)
    cue.show()
    cue.encode()


def _decode_test(test_name, test_data):
    passed = "✔"
    failed = "✘"
    print2(f"testing {test_name}\n Data: {test_data}\n")
    if decode(test_data):
        return passed
    return failed


def smoke(tests=None):
    """
    calls threefive.decode using the values in tests.
    The format for tests:
    { "test_name" : value to pass to threefive.decode}

    example:

     my_tests ={
    "Base64": "/DAvAAAAAAAA///wBQb+dGKQoAAZAhdDVUVJSAAAjn+fCAgAAAAALKChijUCAKnMZ1g=",
    "Bytes": b"\xfc0\x11\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\x00\x00O%3\x96"
    }

    import threefive
    threefive.smoke_test(my_tests)

    """
    if not tests:
        tests = ten_tests
    results = {k: _decode_test(k, v) for k, v in tests.items()}
    print2("Smoke Test\n")
    for kay, vee in results.items():
        print2(f"{kay}  {vee}")


if __name__ == "__main__":

    json_load_test()
#    smoke()
