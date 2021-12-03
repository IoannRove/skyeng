from typing import List, Optional, TypeVar, NamedTuple, Type

from model import utils


SchemaType = TypeVar("SchemaType", bound=NamedTuple)


class BaseData:
    def __init__(self, data_file_name: str, schema: Type[SchemaType]) -> None:
        self.data_file_name = data_file_name
        self.schema = schema

    def get_all(self) -> List[SchemaType]:
        data: List[SchemaType] = [self.schema(**data) for data in self._get_data()]
        return data

    def get_by_id(self, id: int) -> Optional[SchemaType]:
        for data in self.get_all():
            if data.pk == id:
                return data
        return None

    def _get_data(self) -> List[dict]:
        return utils.get_json_from_file(self.data_file_name)
