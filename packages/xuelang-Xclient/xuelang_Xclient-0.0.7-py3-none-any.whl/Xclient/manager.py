import json
import logging
from typing import Dict, Iterable, Tuple
from tritonclient.grpc import InferenceServerClient
from Xclient.client import ModelClient
from Xclient.utils import parse_grpc_response,get_model_state
from Xclient.utils import TritonUrl

LOGGER = logging.getLogger(__name__)

class ModelManager:
    """ModelManager class for maintaining Triton models."""

    def __init__(
        self,
        triton_url: list[str],
    ):
        """Create ModelManager object.

        Args:
            triton_url: Triton server URL
        """
        self._triton_url = [TritonUrl.from_url(url).without_scheme for url in triton_url]
        self._models: Dict[Tuple[str, str], str] = {}

    def get_model_repository_index(self):
        for url in self._triton_url:
            repository_index  = InferenceServerClient(url).get_model_repository_index()
            models_states = parse_grpc_response(models=repository_index.models)
            self._models.update({
                (url,name): state for (name, version), state in models_states.items()
            })
        return self._models
    
    def get_model_config(self,model:Tuple[str, str]):
        with ModelClient(
            url=model[0], model_name=model[1], 
        ) as client: 
            return  client.model_config

    def get_inference_statistics(self,model:Tuple[str, str]):
        with ModelClient(
            url=model[0], model_name=model[1], 
        ) as client: 
            return  client._general_client.get_inference_statistics(model[1])

    def unload_model(self,model:Tuple[str, str]):
        with ModelClient(
            url=model[0], model_name=model[1], 
        ) as client: 
            client.wait_for_server(timeout_s=60)
            client.unload_model()

    def load_model(self, model:Tuple[str, str]):
        with ModelClient(
            url=model[0], model_name=model[1], 
        ) as client: 
            client.wait_for_server(timeout_s=60)
            client.load_model()