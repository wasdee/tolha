from pathlib import Path
import pytest
from tolha.models.call import CallUsageResponse, Call

@pytest.fixture
def response():
    file = Path(__file__).parent / 'author_response.json'
    with file.open('r', encoding="utf-8") as stream:
        yield stream.read() 

def test_parse(response):
    call_response = CallUsageResponse.parse_raw(response)

    calls = Call.parse_usage_detail_groups(call_response.data.usage_detail_groups)
    assert len(calls) == 54
    


