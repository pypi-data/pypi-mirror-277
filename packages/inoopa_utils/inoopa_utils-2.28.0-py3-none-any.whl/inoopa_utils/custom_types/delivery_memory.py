from dataclasses import dataclass


@dataclass(slots=True)
class DeliveryMemory:
    """The data schema for the delivery_memory collection."""
    _id: str # delivery_id
    company_id: str
    # Optionals
    phone: str | None
    email: str | None
    website: str | None
    decision_maker_ids: list | None
