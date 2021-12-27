from decouple import config
from tolha.myais import get_all_call_history



def test_get_all_call_history():
    invoices, call_usages = get_all_call_history(config("PHONE_NUMBER"), config("PASSWORD"), config("NATIONAL_ID"))

    assert isinstance(invoices, list)
    assert isinstance(call_usages, dict)