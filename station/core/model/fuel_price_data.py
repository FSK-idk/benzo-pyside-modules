from dataclasses import dataclass

from core.model.fuel_type import FuelType


@dataclass
class FuelPriceData:
    price: dict[FuelType, int]
