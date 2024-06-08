from typing import Optional

from montelo.MonteloClient import InnerMonteloClient
from montelo.core import MonteloChatClient
from montelo.core.MonteloDatapoints import MonteloDatapoints
from montelo.core.MonteloDatasets import MonteloDatasets
from montelo.core.MonteloExperiments import MonteloExperiments


class Montelo:
    def __init__(
            self,
            *,
            api_key: Optional[str] = None,
            base_url: Optional[str] = None,
    ):
        self._montelo_client = InnerMonteloClient(api_key=api_key, base_url=base_url)

        self.datasets = MonteloDatasets(montelo_client=self._montelo_client)
        self.datapoints = MonteloDatapoints(montelo_client=self._montelo_client)
        self.experiments = MonteloExperiments(montelo_client=self._montelo_client)
        self.client = MonteloChatClient(montelo_client=self._montelo_client)
