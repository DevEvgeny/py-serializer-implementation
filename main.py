import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_string = json.dumps(serializer.data)
    return json_string.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    json_string = json.decode("utf-8")
    data = json.loads(json_string)
    serializer = CarSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()
