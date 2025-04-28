from dataclasses import dataclass

from core.model.fuel_type import FuelType


@dataclass
class FuelSelectionData:
    fuel_type: FuelType
    fuel_amount: int
    payment_amount: int
