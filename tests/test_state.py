import pytest
from orders.models.order import Order
from orders.services.state import transition
from orders.errors import InvalidTransition
def test_invalid_transition_does_not_corrupt():
    o=Order(id="o1", status="created")
    with pytest.raises(InvalidTransition):
        transition(o, "refunded")
    assert o.status == "created", "status must not change on an invalid transition"
