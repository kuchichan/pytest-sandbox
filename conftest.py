import pytest
import os
from pytest_sandbox.some_function import generate_proto

@pytest.fixture(scope="session")
def create_proto_file():
    root = os.path.dirname(os.path.realpath(__file__))
    src = os.path.join(root, 'data')
    proto_file = os.path.join(src, "example.proto")
    print(src, root, proto_file)
    generate_proto(src, root, proto_file)

