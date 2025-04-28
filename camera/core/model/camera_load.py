from dataclasses import dataclass
from typing import Self


@dataclass
class CameraLoad:
    date_time: str
    car_number: str
    image_filename: str
    is_recognized: str

    @classmethod
    def from_data(cls, data: list) -> Self:
        return cls(
            date_time=data[0],
            car_number=data[1],
            image_filename=data[2],
            is_recognized=data[3],
        )
