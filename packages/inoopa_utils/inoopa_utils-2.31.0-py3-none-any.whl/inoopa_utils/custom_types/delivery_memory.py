from dataclasses import dataclass, field


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
    best_phone: BestPhone = field(default=BestPhone(None))
    best_email: BestEmail = field(default=BestEmail(None))
    best_website: BestWebsite = field(default=BestWebsite(None))
    decision_maker_ids: list | None = field(default_factory=list)
