import pytest
from tamil_translite import translite


def translite_func(sentence):
    return translite(sentence)


def test_translite():
    assert (
        translite(
            """ஓர் ஊர்தியில் ஏறி, கீழே இறங்கி சூடான சுத்தமான நெய் உணவு ஆவினை எடுத்து, திடீரென ஐந்நூறு கூடை குண்டூசியும் ஈரேழு ஔடத மின்னூல்களும் அனுப்பி ஞாபகமூட்டியது ஒரு தூதுக்குழு"""
        )
        == "or oordhiyil yeri, keezhae irangi soodaana suththamaana nei unavu aavinai eduththu, thideerena ainnooru koodai kundoosiyum eeraezhu audadha minnoolgalum anuppi njaabagamoottiyadhu oru thoodhukkuzhu"
    )


@pytest.mark.parametrize(
    "input_word, expected_value",
    [
        ("காக்கா", "kaakkaa"),
        ("அகம்", "agam"),
    ],
)
def test_ka_ga_variation(input_word, expected_value):
    assert translite(input_word) == expected_value


@pytest.mark.parametrize(
    "input_word, expected_value",
    [
        ("சச்சரவு", "sachcharavu"),
        ("பசலை", "pasalai"),
    ],
)
def test_sa_cha_variation(input_word, expected_value):
    assert translite(input_word) == expected_value


@pytest.mark.parametrize(
    "input_word, expected_value",
    [("சம்மட்டி", "sammatti"), ("படி", "padi"), ("டபரா", "dabaraa")],
)
def test_ta_da_variation(input_word, expected_value):
    assert translite(input_word) == expected_value


@pytest.mark.parametrize(
    "input_word, expected_value",
    [
        ("பதம்", "padham"),
        ("சத்தம்", "saththam"),
        ("துணை", "thunai"),
    ],
)
def test_tha_dha_variation(input_word, expected_value):
    assert translite(input_word) == expected_value


@pytest.mark.parametrize(
    "input_word, expected_value",
    [
        ("பாப்பா", "paappaa"),
        ("செண்பகம்", "senbagam"),
    ],
)
def test_pa_ba_variation(input_word, expected_value):
    assert translite(input_word) == expected_value
