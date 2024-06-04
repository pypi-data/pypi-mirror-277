from dataclasses import dataclass


# ? Note:
# We have to have this dataclass in dataclass to be able to map the company collection
# with the delivery_memory collection. Otherwise, it's a mess to query the collections together.
# I know it seems overkill, but it's the only way I could get it to work simply in the delivery_manger.


@dataclass(slots=True)
class BestEmail:
    email: str | None

@dataclass(slots=True)
class BestPhone:
    phone: str | None

@dataclass(slots=True)
class BestWebsite:
    website: str | None


@dataclass(slots=True)
class DeliveryMemory:
    """The data schema for the delivery_memory collection."""
    _id: str # delivery_id
    company_id: str
    # Optionals
    best_phone: BestPhone
    best_email: BestEmail
    best_website: BestWebsite
    decision_maker_ids: list | None
