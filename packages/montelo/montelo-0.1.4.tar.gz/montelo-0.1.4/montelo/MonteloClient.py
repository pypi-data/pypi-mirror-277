import os
from typing import Optional, List

from pydantic import StrictStr

from montelo.client.openapi_client.api.datapoint_api import DatapointApi
from montelo.client.openapi_client.api.datapoint_run_api import DatapointRunApi
from montelo.client.openapi_client.api.dataset_api import DatasetApi
from montelo.client.openapi_client.api.experiment_api import ExperimentApi
from montelo.client.openapi_client.api.inference_api import InferenceApi
from montelo.client.openapi_client.api_client import ApiClient
from montelo.client.openapi_client.configuration import Configuration
from montelo.client.openapi_client.models.add_to_dataset_input import AddToDatasetInput
from montelo.client.openapi_client.models.batch_add_to_dataset_input import BatchAddToDatasetInput
from montelo.client.openapi_client.models.create_datapoint_run_input import CreateDatapointRunInput
from montelo.client.openapi_client.models.create_dataset_input import CreateDatasetInput
from montelo.client.openapi_client.models.create_experiment_input import CreateExperimentInput
from montelo.client.openapi_client.models.datapoint_dto import DatapointDto
from montelo.client.openapi_client.models.datapoint_run_dto import DatapointRunDto
from montelo.client.openapi_client.models.dataset_dto import DatasetDto
from montelo.client.openapi_client.models.experiment_dto import ExperimentDto
from montelo.client.openapi_client.models.inference_input import InferenceInput
from montelo.client.openapi_client.models.paginated_experiment_with_datapoints_dto import \
    PaginatedExperimentWithDatapointsDto
from montelo.client.openapi_client.models.success_dto import SuccessDto
from montelo.client.openapi_client.models.update_datapoint_run_input import UpdateDatapointRunInput


class InnerMonteloClient:
    def __init__(
            self,
            *,
            api_key: Optional[str] = None,
            base_url: Optional[str] = None
    ):
        api_key = api_key or os.environ.get("MONTELO_API_KEY")
        base_url = base_url or os.environ.get("MONTELO_BASE_URL", "https://api.montelo.ai")

        if not api_key:
            raise Exception("Montelo API key not set.")

        self.configuration = Configuration(
            host=base_url,
            access_token=api_key,
        )
        self.default_headers = {
            "x-montelo-sdk": "true",
        }

    def create_dataset(self, create_dataset_input: CreateDatasetInput) -> DatasetDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = DatasetApi(api_client)
            return api_instance.dataset_controller_create_dataset(
                create_dataset_input=create_dataset_input,
                _headers=self.default_headers
            )

    def create_datapoint(
            self,
            *,
            dataset_id: StrictStr,
            add_to_dataset_input: AddToDatasetInput
    ) -> DatapointDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = DatapointApi(api_client)
            return api_instance.datapoint_controller_create_datapoint(
                dataset_id=dataset_id,
                add_to_dataset_input=add_to_dataset_input,
                _headers=self.default_headers
            )

    def create_batch_datapoints(self, *, dataset_id: StrictStr, datapoints: List[AddToDatasetInput]) -> None:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = DatapointApi(api_client)
            batch_params = BatchAddToDatasetInput(datapoints=datapoints)
            api_instance.datapoint_controller_batch_create_datapoint(
                dataset_id=dataset_id,
                batch_add_to_dataset_input=batch_params,
                _headers=self.default_headers
            )

    def create_experiment(
            self,
            *,
            dataset_id: StrictStr,
            create_experiment_input: CreateExperimentInput
    ) -> ExperimentDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = ExperimentApi(api_client)
            return api_instance.experiment_controller_create(
                dataset_id=dataset_id,
                create_experiment_input=create_experiment_input,
                _headers=self.default_headers,
            )

    def create_datapoint_run(self, create_datapoint_run_input: CreateDatapointRunInput) -> DatapointRunDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = DatapointRunApi(api_client)
            return api_instance.datapoint_run_controller_create_datapoint_run(
                create_datapoint_run_input=create_datapoint_run_input,
                _headers=self.default_headers,
            )

    def update_datapoint_run(self, update_datapoint_run_input: UpdateDatapointRunInput) -> SuccessDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = DatapointRunApi(api_client)
            return api_instance.datapoint_run_controller_update_datapoint_run(
                update_datapoint_run_input=update_datapoint_run_input,
                _headers=self.default_headers,
            )

    def get_datapoints_by_experiment_id(
            self,
            *,
            experiment_id: StrictStr,
            take: Optional[int] = None,
            skip: Optional[int] = None
    ) -> PaginatedExperimentWithDatapointsDto:
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = ExperimentApi(api_client)
            take_str = str(take) if take is not None else None
            skip_str = str(skip) if skip is not None else None

            return api_instance.experiment_controller_get_paginated_datapoints_for_experiment(
                experiment_id=experiment_id,
                take=take_str,
                skip=skip_str,
                _headers=self.default_headers,
            )

    def inference(
            self,
            *,
            model: StrictStr,
            inference_input: InferenceInput,
    ):
        with ApiClient(configuration=self.configuration) as api_client:
            api_instance = InferenceApi(api_client)

            return api_instance.inference_controller_inference(
                model=model,
                inference_input=inference_input
            )
