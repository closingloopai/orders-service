"""Order state machine."""
from orders.errors import InvalidTransition

_ALLOWED = {
    "created": {"paid", "cancelled"},
    "paid": {"fulfilled", "cancelled", "refunded"},
    "fulfilled": {"refunded"},
    "cancelled": set(),
    "refunded": set(),
}
def transition(order, to):
    """Move ``order`` to state ``to`` if allowed.

    BUG: it mutates order.status BEFORE checking whether the transition is
    allowed, so an invalid transition still corrupts the order (and only then
    raises). Validate first, mutate only on success.
    """
    order.status = to
    if to not in _ALLOWED.get(order.status, set()):
        raise InvalidTransition(f"{order.status} -> {to}")
    return order
