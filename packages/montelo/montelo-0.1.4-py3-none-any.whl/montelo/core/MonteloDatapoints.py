from typing import Any, Dict, Literal, Optional, List

from montelo.MonteloClient import InnerMonteloClient
from montelo.client.openapi_client.models.add_to_dataset_input import AddToDatasetInput
from montelo.client.openapi_client.models.datapoint_dto import DatapointDto


class MonteloDatapoints:
    def __init__(self, montelo_client: InnerMonteloClient):
        self._montelo_client = montelo_client

    def create(
            self,
            *,
            dataset: str,
            input: Dict[str, Any],
            expected_output: Dict[str, Any],
            split: Optional[Literal["TRAIN", "TEST"]] = None,
            metadata: Optional[Dict[str, Any]] = None,
    ) -> DatapointDto:
        payload = AddToDatasetInput(
            input=input,
            expected_output=expected_output,
            split=split,
            metadata=metadata,
        )
        return self._montelo_client.create_datapoint(
            dataset_id=dataset,
            add_to_dataset_input=payload
        )

    def create_many(
            self,
            *,
            dataset: str,
            datapoints: List[Dict[str, Any]],
    ) -> None:
        def chunk_list(data, size):
            return (data[i:i + size] for i in range(0, len(data), size))

        chunks = chunk_list(datapoints, 10)

        def process_chunk(chunk):
            dps = [
                AddToDatasetInput(
                    input=datapoint["input"],
                    expected_output=datapoint["expected_output"],
                    metadata=datapoint.get("metadata", None),
                    split=datapoint.get("split", None),
                ) for datapoint in chunk
            ]
            self._montelo_client.create_batch_datapoints(dataset_id=dataset, datapoints=dps)

        [process_chunk(chunk) for chunk in chunks]
