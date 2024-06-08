from typing import Optional, List, Union

from pydantic import StrictFloat, StrictInt

from montelo.MonteloClient import InnerMonteloClient
from montelo.client.openapi_client import ResponseFormatDto, ToolDto
from montelo.client.openapi_client.models.datapoint_dto import DatapointDto
from montelo.client.openapi_client.models.inference_input import InferenceInput
from montelo.client.openapi_client.models.message_dto import MessageDto


class MonteloChatClient:
    def __init__(self, montelo_client: InnerMonteloClient):
        self._montelo_client = montelo_client

    def chat(
            self,
            *,
            model: str,
            messages: List[MessageDto],
            tools: Optional[List[ToolDto]] = None,
            max_tokens: Optional[Union[StrictFloat, StrictInt]] = None,
            prompt_truncate_len: Optional[Union[StrictFloat, StrictInt]] = None,
            temperature: Optional[Union[StrictFloat, StrictInt]] = None,
            top_p: Optional[Union[StrictFloat, StrictInt]] = None,
            top_k: Optional[Union[StrictFloat, StrictInt]] = None,
            frequency_penalty: Optional[Union[StrictFloat, StrictInt]] = None,
            presence_penalty: Optional[Union[StrictFloat, StrictInt]] = None,
            n: Optional[Union[StrictFloat, StrictInt]] = None,
            response_format: Optional[ResponseFormatDto] = None,
    ) -> DatapointDto:
        payload = InferenceInput(
            messages=messages,
            tools=tools,
            max_tokens=max_tokens,
            prompt_truncate_len=prompt_truncate_len,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            n=n,
            response_format=response_format
        )
        return self._montelo_client.inference(
            model=model,
            inference_input=payload
        )
