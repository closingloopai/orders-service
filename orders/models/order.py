from dataclasses import dataclass, field
@dataclass
class Order:
    id: str
    status: str = "created"     # created|paid|fulfilled|cancelled|refunded
    total_cents: int = 0
    refunded_cents: int = 0
