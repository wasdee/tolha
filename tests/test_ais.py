from decouple import config
from tolha.myais import get_recent_call_history

def test_get_recent_call_history():
    call_usage = get_recent_call_history(config("PHONE_NUMBER"), config("PASSWORD"), config("NATIONAL_ID_CARD"))
    import pickle
    with open("data.pkl", mode="wb") as f:
        pickle.dump(call_usage, f)
    print(call_usage)
    assert call_usage