import pytest

# A simple function for testing the calculation (you can import it from your code)
def calculate_exchange(amount, rate_in, rate_out):
    in_czk = amount * rate_in
    return in_czk / rate_out

def test_conversion_eur_to_usd():
    # Simulation: 100 EUR to USD (at exchange rates e.g. EUR:25, USD:20)
    # Expected result: 100 * 25 / 20 = 125 USD
    result = calculate_exchange(100, 25, 20)
    assert result == 125.0

def test_conversion_zero_amount():
    assert calculate_exchange(0, 25, 20) == 0