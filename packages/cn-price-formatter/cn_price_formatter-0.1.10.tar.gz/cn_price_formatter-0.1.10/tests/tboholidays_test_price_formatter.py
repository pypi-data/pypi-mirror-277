import pytest
from cn_price_formatter.price_formatter import PriceFormatter


@pytest.fixture
def sample_tbo_json_data():
    json_data = {
                  "Name": [
                    "Deluxe Room, 1 King Bed, Accessible,NonSmoking"
                  ],
                  "BookingCode": "1377827!TB!1!TB!82213203-302a-430d-a5ef-39f8c3240f9d",
                  "Inclusion": "Free valet parking,Free self parking",
                  "DayRates": [
                    [
                      {
                        "BasePrice": 208.2800
                      },
                      {
                        "BasePrice": 208.2800
                      },
                      {
                        "BasePrice": 208.2800
                      }
                    ]
                  ],
                  "TotalFare": 765.41,
                  "TotalTax": 140.57,
                  "RoomPromotion": [
                    "Save 15%"
                  ],
                  "CancelPolicies": [
                    {
                      "FromDate": "04-06-2024 00:00:00",
                      "ChargeType": "Percentage",
                      "CancellationCharge": 100.0
                    }
                  ],
                  "MealType": "Room_Only",
                  "IsRefundable": False,
                  "Supplements": [
                    [
                      {
                        "Index": 1,
                        "Type": "AtProperty",
                        "Description": "mandatory_tax",
                        "Price": 60.00,
                        "Currency": "AED"
                      }
                    ]
                  ],
                  "WithTransfers": False
}

    return json_data


def test_initialization():
    formatter = PriceFormatter()
    assert formatter.base_rate == 0
    assert formatter.total == 0
    assert formatter.avg_price_before_tax == 0
    assert formatter.avg_price_after_tax == 0
    assert formatter.total_tax == 0
    assert formatter.total_tax_rate == 0
    assert formatter.rooms_available == 0
    assert formatter.room_count == 0
    assert formatter.pay_now == 0
    assert formatter.cn_fees == 0


def test_tbo_valid_json(sample_tbo_json_data):
    formatter = PriceFormatter()
    formatter.tboholidays(sample_tbo_json_data,3)
    assert formatter.total == 811.3345999999999
    assert formatter.base_rate == 624.8399999999999


# def test_tbo_invalid_json():
#     formatter = PriceFormatter()
#     with pytest.raises(ValueError, match="Invalid JSON data"):
#         formatter.tboholidays("invalid_json",3)


def test_get_total_price_before_tax():
    formatter = PriceFormatter()
    formatter.base_rate = 624.8399999999999
    assert formatter.get_base_rate() == 624.8399999999999


def test_get_total_cn_fee_tbo(sample_tbo_json_data):
    tboholidays = PriceFormatter()
    tboholidays.tboholidays(sample_tbo_json_data,3)
    assert tboholidays.get_total_cn_fee() == 45.9246




