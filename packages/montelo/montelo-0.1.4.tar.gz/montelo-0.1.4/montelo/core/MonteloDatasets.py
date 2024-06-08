from typing import Optional

from montelo.MonteloClient import InnerMonteloClient
from montelo.client.openapi_client.models.create_dataset_input import CreateDatasetInput
from montelo.client.openapi_client.models.dataset_dto import DatasetDto


class MonteloDatasets:
    def __init__(self, montelo_client: InnerMonteloClient):
        self._montelo_client = montelo_client

    def create(
            self,
            *,
            name: str,
            description: Optional[str] = None,
    ) -> DatasetDto:
        params = CreateDatasetInput(
            name=name,
            description=description,
        )
        return self._montelo_client.create_dataset(create_dataset_input=params)
