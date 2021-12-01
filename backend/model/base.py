from typing import List, Optional

from backend.model import utils


class BaseData:
    def __init__(self, data_file_name: str) -> None:
        self.data_file_name = data_file_name

    def get_all(self) -> List[dict]:
        data: List[dict] = self._get_data()
        return data

    def get_by_id(self, id: int) -> Optional[dict]:
        for post in self.get_all():
            if post['pk'] == id:
                return post
        return None

    def _get_data(self) -> List[dict]:
        return utils.get_json_from_file(self.data_file_name)
