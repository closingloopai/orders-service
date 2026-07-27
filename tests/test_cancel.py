from orders.models.order import Order
from orders.services.cancel import cancel
def test_unpaid_cancel_has_no_refund():
    o=Order(id="o1", status="created", total_cents=5000)
    cancel(o)
    assert o.refunded_cents == 0, "an unpaid order must not be refunded on cancel"
