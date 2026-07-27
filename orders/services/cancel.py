"""Cancel an order and refund if it was paid."""
def cancel(order):
    """Cancel ``order``; if it was already paid, refund the full total.

    BUG: it refunds on EVERY cancel, including orders that were never paid
    (status 'created'), issuing a refund for money never captured. Only refund
    when the order was in a paid/fulfilled state.
    """
    order.refunded_cents = order.total_cents
    order.status = "cancelled"
    return order
