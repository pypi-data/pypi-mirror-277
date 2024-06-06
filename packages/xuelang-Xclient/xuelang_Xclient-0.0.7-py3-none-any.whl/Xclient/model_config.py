import dataclasses
from typing import Dict, Optional, Sequence, Type, Union
import enum
import numpy as np
import json
import logging
import pathlib
from google.protobuf import json_format, text_format
from Xclient.exceptions import PyTritonModelConfigError, PyTritonBadParameterError
try:
    import tritonclient.grpc as grpc_client
    from tritonclient import utils as client_utils  # noqa: F401
except ImportError:
    try:
        import tritonclientutils as client_utils  # noqa: F401
        import tritongrpcclient as grpc_client
    except ImportError:
        client_utils = None
        grpc_client = None
        
LOGGER = logging.getLogger(__name__)

class DeviceKind(enum.Enum):
    """Device kind for model deployment.

    Args:
        KIND_AUTO: Automatically select the device for model deployment.
        KIND_CPU: Model is deployed on CPU.
        KIND_GPU: Model is deployed on GPU.
    """

    KIND_AUTO = "KIND_AUTO"
    KIND_CPU = "KIND_CPU"
    KIND_GPU = "KIND_GPU"

class TimeoutAction(enum.Enum):
    """Timeout action definition for timeout_action QueuePolicy field.

    Args:
        REJECT: Reject the request and return error message accordingly.
        DELAY: Delay the request until all other requests at the same (or higher) priority levels
           that have not reached their timeouts are processed.
    """

    REJECT = "REJECT"
    DELAY = "DELAY"

@dataclasses.dataclass
class QueuePolicy:
    """Model queue policy configuration.

    More in Triton Inference Server [documentation]
    [documentation]: https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto#L1037

    Args:
        timeout_action: The action applied to timed-out request.
        default_timeout_microseconds: The default timeout for every request, in microseconds.
        allow_timeout_override: Whether individual request can override the default timeout value.
        max_queue_size: The maximum queue size for holding requests.
    """

    timeout_action: TimeoutAction = TimeoutAction.REJECT
    default_timeout_microseconds: int = 0
    allow_timeout_override: bool = False
    max_queue_size: int = 0

@dataclasses.dataclass
class DynamicBatcher:
    """Dynamic batcher configuration.

    More in Triton Inference Server [documentation]
    [documentation]: https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto#L1104

    Args:
        max_queue_delay_microseconds: The maximum time, in microseconds, a request will be delayed in
                                      the scheduling queue to wait for additional requests for batching.
        preferred_batch_size: Preferred batch sizes for dynamic batching.
        preserve_ordering : Should the dynamic batcher preserve the ordering of responses to
                            match the order of requests received by the scheduler.
        priority_levels: The number of priority levels to be enabled for the model.
        default_priority_level: The priority level used for requests that don't specify their priority.
        default_queue_policy: The default queue policy used for requests.
        priority_queue_policy: Specify the queue policy for the priority level.
    """

    max_queue_delay_microseconds: int = 0
    preferred_batch_size: Optional[list] = None
    preserve_ordering: bool = False
    priority_levels: int = 0
    default_priority_level: int = 0
    default_queue_policy: Optional[QueuePolicy] = None
    priority_queue_policy: Optional[Dict[int, QueuePolicy]] = None

@dataclasses.dataclass
class ResponseCache:
    """Model response cache configuration.

    More in Triton Inference Server [documentation]
    [documentation]: https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto#L1765
    """

    enable: bool


@dataclasses.dataclass
class TensorSpec:
    """Stores specification of single tensor. This includes name, shape and dtype."""

    name: str
    shape: tuple
    dtype: Union[Type[np.dtype], Type[object]]
    optional: Optional[bool] = False

@dataclasses.dataclass
class TritonModelConfig:
    """Triton Model Config dataclass for simplification and specialization of protobuf config generation.

    More in Triton Inference Server [documentation]
    [documentation]: https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto
    """

    model_name: str
    model_version: int = 1
    max_batch_size: int = 4
    batching: bool = True
    batcher: Optional[DynamicBatcher] = None
    instance_group: Dict[DeviceKind, Optional[int]] = dataclasses.field(default_factory=lambda: {})
    decoupled: bool = False
    backend_parameters: Dict[str, str] = dataclasses.field(default_factory=lambda: {})
    inputs: Optional[Sequence[TensorSpec]] = None
    outputs: Optional[Sequence[TensorSpec]] = None
    response_cache: Optional[ResponseCache] = None

    @property
    def backend(self) -> str:
        """Return backend parameter."""
        return "python"
    
class ModelConfigParser:
    """Provide functionality to parse dictionary or file to ModelConfig object."""

    @classmethod
    def from_dict(cls, model_config_dict: Dict) -> TritonModelConfig:
        """Create ModelConfig from configuration stored in dictionary.

        Args:
            model_config_dict: Dictionary with model config

        Returns:
            A ModelConfig object with data parsed from the dictionary
        """
        LOGGER.debug(f"Parsing Triton config model from dict: \n{json.dumps(model_config_dict, indent=4)}")

        if model_config_dict.get("max_batch_size", 0) > 0:
            batching = True
        else:
            batching = False

        dynamic_batcher_config = model_config_dict.get("dynamic_batching")
        if dynamic_batcher_config is not None:
            batcher = cls._parse_dynamic_batching(dynamic_batcher_config)
        else:
            batcher = None

        instance_group = {
            DeviceKind(entry["kind"]): entry.get("count") for entry in model_config_dict.get("instance_group", [])
        }

        decoupled = model_config_dict.get("model_transaction_policy", {}).get("decoupled", False)

        backend_parameters_config = model_config_dict.get("parameters", [])
        if isinstance(backend_parameters_config, list):
            # If the backend_parameters_config is a list of strings, use them as keys with empty values
            LOGGER.debug(f"backend_parameters_config is a list of strings: {backend_parameters_config}")
            backend_parameters = {name: "" for name in backend_parameters_config}
        elif isinstance(backend_parameters_config, dict):
            # If the backend_parameters_config is a dictionary, use the key and "string_value" fields as key-value pairs
            LOGGER.debug(f"backend_parameters_config is a dictionary: {backend_parameters_config}")
            backend_parameters = {
                name: backend_parameters_config[name]["string_value"] for name in backend_parameters_config
            }
        else:
            # Otherwise, raise an error
            LOGGER.error(
                f"Invalid type {type(backend_parameters_config)} for backend_parameters_config: {backend_parameters_config}"
            )
            raise TypeError(f"Invalid type for backend_parameters_config: {type(backend_parameters_config)}")

        inputs = [
            cls.rewrite_io_spec(item, "input", idx) for idx, item in enumerate(model_config_dict.get("input", []))
        ] or None
        outputs = [
            cls.rewrite_io_spec(item, "output", idx) for idx, item in enumerate(model_config_dict.get("output", []))
        ] or None

        response_cache_config = model_config_dict.get("response_cache")
        if response_cache_config:
            response_cache = cls._parse_response_cache(response_cache_config)
        else:
            response_cache = None
            
        sequence_batching_config  = model_config_dict.get("sequence_batching")

        if sequence_batching_config is not None:
            try:
                for c in sequence_batching_config['control_input']:
                    if c["name"] == "CORRID":
                        backend_parameters['is_corrid_string'] = c["control"][0]["data_type"] == "TYPE_STRING"
                        break
            except:
                print("Error in corrid type!!", flush=True)
                exit(7)

        return TritonModelConfig(
            model_name=model_config_dict["name"],
            batching=batching,
            max_batch_size=model_config_dict.get("max_batch_size", 0),
            batcher=batcher,
            inputs=inputs,
            outputs=outputs,
            instance_group=instance_group,
            decoupled=decoupled,
            backend_parameters=backend_parameters,
            response_cache=response_cache,
        )

    @classmethod
    def from_file(cls, *, config_path: pathlib.Path) -> TritonModelConfig:
        """Create ModelConfig from configuration stored in file.

        Args:
            config_path: location of file with model config

        Returns:
            A ModelConfig object with data parsed from the file
        """
        from tritonclient.grpc import model_config_pb2  # pytype: disable=import-error

        LOGGER.debug(f"Parsing Triton config model config_path={config_path}")

        with config_path.open("r") as config_file:
            payload = config_file.read()
            model_config_proto = text_format.Parse(payload, model_config_pb2.ModelConfig())

        model_config_dict = json_format.MessageToDict(model_config_proto, preserving_proto_field_name=True)
        return ModelConfigParser.from_dict(model_config_dict=model_config_dict)

    @classmethod
    def rewrite_io_spec(cls, item: Dict, io_type: str, idx: int) -> TensorSpec:
        """Rewrite the IO Spec provided in form of dictionary to TensorSpec.

        Args:
            item: IO data for input
            io_type: Type of the IO (input or output)
            idx: Index of IO

        Returns:
            TensorSpec with input or output data
        """
        name = item.get("name")
        if not name:
            raise PyTritonModelConfigError(f"Name for {io_type} at index {idx} not provided.")

        data_type = item.get("data_type")
        if not data_type:
            raise PyTritonModelConfigError(f"Data type for {io_type} with name `{name}` not defined.")

        data_type_val = data_type.split("_")
        if len(data_type_val) != 2:
            raise PyTritonModelConfigError(
                f"Invalid data type `{data_type}` for {io_type} with name `{name}` not defined. "
                "The expected name is TYPE_{type}."
            )

        data_type = data_type_val[1]
        if data_type == "STRING":
            dtype = np.object_
        else:
            dtype = client_utils.triton_to_np_dtype(data_type)
            if dtype is None:
                raise PyTritonModelConfigError(f"Unsupported data type `{data_type}` for {io_type} with name `{name}`")

            dtype = np.dtype("bool") if dtype == bool else dtype

        dims = item.get("dims", [])
        if not dims:
            raise PyTritonModelConfigError(f"Dimension for {io_type} with name `{name}` not defined.")

        shape = tuple(int(s) for s in dims)

        optional = item.get("optional", False)
        return TensorSpec(name=item["name"], shape=shape, dtype=dtype, optional=optional)

    @classmethod
    def _parse_dynamic_batching(cls, dynamic_batching_config: Dict) -> DynamicBatcher:
        """Parse config to create DynamicBatcher object.

        Args:
            dynamic_batching_config: Configuration of dynamic batcher from config

        Returns:
            DynamicBatcher object with configuration
        """
        default_queue_policy = None
        default_queue_policy_config = dynamic_batching_config.get("default_queue_policy")
        if default_queue_policy_config:
            default_queue_policy = QueuePolicy(
                timeout_action=TimeoutAction(
                    default_queue_policy_config.get("timeout_action", TimeoutAction.REJECT.value)
                ),
                default_timeout_microseconds=int(default_queue_policy_config.get("default_timeout_microseconds", 0)),
                allow_timeout_override=bool(default_queue_policy_config.get("allow_timeout_override", False)),
                max_queue_size=int(default_queue_policy_config.get("max_queue_size", 0)),
            )

        priority_queue_policy = None
        priority_queue_policy_config = dynamic_batching_config.get("priority_queue_policy")
        if priority_queue_policy_config:
            priority_queue_policy = {}
            for priority, queue_policy_config in priority_queue_policy_config.items():
                queue_policy = QueuePolicy(
                    timeout_action=TimeoutAction(queue_policy_config.get("timeout_action", TimeoutAction.REJECT.value)),
                    default_timeout_microseconds=int(queue_policy_config.get("default_timeout_microseconds", 0)),
                    allow_timeout_override=bool(queue_policy_config.get("allow_timeout_override", False)),
                    max_queue_size=int(queue_policy_config.get("max_queue_size", 0)),
                )
                priority_queue_policy[int(priority)] = queue_policy

        batcher = DynamicBatcher(
            preferred_batch_size=dynamic_batching_config.get("preferred_batch_size"),
            max_queue_delay_microseconds=int(dynamic_batching_config.get("max_queue_delay_microseconds", 0)),
            preserve_ordering=bool(dynamic_batching_config.get("preserve_ordering", False)),
            priority_levels=int(dynamic_batching_config.get("priority_levels", 0)),
            default_priority_level=int(dynamic_batching_config.get("default_priority_level", 0)),
            default_queue_policy=default_queue_policy,
            priority_queue_policy=priority_queue_policy,
        )
        return batcher

    @classmethod
    def _parse_response_cache(cls, response_cache_config: Dict) -> ResponseCache:
        """Parse config for response cache.

        Args:
            response_cache_config: response cache configuration

        Returns:
            ResponseCache object with configuration
        """
        response_cache = ResponseCache(
            enable=bool(response_cache_config["enable"]),
        )
        return response_cache
    
class ModelConfigGenerator:
    """Generate the protobuf config from ModelConfig object."""

    def __init__(self, config: TritonModelConfig):
        """Initialize generator.

        Args:
            config: model config object
        """
        self._config = config

    def to_file(self, config_path: Union[str, pathlib.Path]) -> str:
        """Serialize ModelConfig to prototxt and save to config_path directory.

        Args:
            config_path: path to configuration file

        Returns:
            A string with generated model configuration
        """
        from tritonclient.grpc import model_config_pb2  # pytype: disable=import-error

        # https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto
        model_config = self.get_config()
        LOGGER.debug(f"Generated Triton config:\n{json.dumps(model_config, indent=4)}")

        config_payload = json_format.ParseDict(model_config, model_config_pb2.ModelConfig())
        LOGGER.debug(f"Generated Triton config payload:\n{config_payload}")

        config_path = pathlib.Path(config_path)
        config_path.parent.mkdir(parents=True, exist_ok=True)

        model_config_bytes = text_format.MessageToBytes(config_payload)

        # WAR: triton requires max_batch_size = 0 to be explicit written
        # while this is not stored in payload during MessageToBytes
        if model_config["max_batch_size"] == 0:
            model_config_bytes += b"max_batch_size: 0\n"

        with config_path.open("wb") as cfg:
            cfg.write(model_config_bytes)

        LOGGER.debug(f"Generated config stored in {config_path}")

        return config_payload

    def get_config(self) -> Dict:
        """Create a Triton model config from ModelConfig object.

        Returns:
            Dict with model configuration data
        """
        model_config = {"name": self._config.model_name, "backend": self._config.backend}
        self._set_batching(model_config)
        self._set_model_signature(model_config)
        self._set_instance_group(model_config)
        self._set_model_transaction_policy(model_config)
        self._set_backend_parameters(model_config)
        self._set_response_cache(model_config)
        return model_config

    def _set_batching(self, model_config: Dict) -> None:
        """Configure batching for model deployment on Triton Inference Server.

        Args:
            model_config: Dict with model config for Triton Inference Server
        """
        if not self._config.batching:
            model_config["max_batch_size"] = 0
            LOGGER.debug("Batching for model is disabled. The `max_batch_size` field value set to 0.")
            return
        elif self._config.max_batch_size < 1:
            raise PyTritonBadParameterError("The `max_batch_size` must be greater or equal to 1.")

        model_config["max_batch_size"] = self._config.max_batch_size
        if isinstance(self._config.batcher, DynamicBatcher):
            dynamic_batching_config = {}
            if self._config.batcher.max_queue_delay_microseconds > 0:
                dynamic_batching_config["maxQueueDelayMicroseconds"] = int(
                    self._config.batcher.max_queue_delay_microseconds
                )

            if self._config.batcher.preferred_batch_size:
                dynamic_batching_config["preferredBatchSize"] = [
                    int(bs) for bs in self._config.batcher.preferred_batch_size
                ]

            if self._config.batcher.preserve_ordering:
                dynamic_batching_config["preserveOrdering"] = self._config.batcher.preserve_ordering

            if self._config.batcher.priority_levels:
                dynamic_batching_config["priorityLevels"] = self._config.batcher.priority_levels

            if self._config.batcher.default_priority_level:
                if self._config.batcher.default_priority_level > self._config.batcher.priority_levels:
                    raise PyTritonBadParameterError(
                        "The `default_priority_level` must be between 1 and " f"{self._config.batcher.priority_levels}."
                    )
                dynamic_batching_config["defaultPriorityLevel"] = self._config.batcher.default_priority_level

            if self._config.batcher.default_queue_policy:
                priority_queue_policy_config = {
                    "timeoutAction": self._config.batcher.default_queue_policy.timeout_action.value,
                    "defaultTimeoutMicroseconds": int(
                        self._config.batcher.default_queue_policy.default_timeout_microseconds
                    ),
                    "allowTimeoutOverride": self._config.batcher.default_queue_policy.allow_timeout_override,
                    "maxQueueSize": int(self._config.batcher.default_queue_policy.max_queue_size),
                }
                dynamic_batching_config["defaultQueuePolicy"] = priority_queue_policy_config

            if self._config.batcher.priority_queue_policy:
                if not self._config.batcher.priority_levels:
                    raise PyTritonBadParameterError(
                        "Provide the `priority_levels` if you want to define `priority_queue_policy` "
                        "for Dynamic Batching."
                    )

                priority_queue_policy_config = {}
                for priority, queue_policy in self._config.batcher.priority_queue_policy.items():
                    if priority < 0 or priority > self._config.batcher.priority_levels:
                        raise PyTritonBadParameterError(
                            f"Invalid `priority`={priority} provided. The value must be between "
                            f"1 and {self._config.batcher.priority_levels}."
                        )

                    priority_queue_policy_config[priority] = {
                        "timeoutAction": queue_policy.timeout_action.value,
                        "defaultTimeoutMicroseconds": int(queue_policy.default_timeout_microseconds),
                        "allowTimeoutOverride": queue_policy.allow_timeout_override,
                        "maxQueueSize": int(queue_policy.max_queue_size),
                    }

                dynamic_batching_config["priorityQueuePolicy"] = priority_queue_policy_config

            model_config["dynamic_batching"] = dynamic_batching_config
        else:
            LOGGER.debug("Default batching used")

    def _set_instance_group(self, model_config: Dict) -> None:
        """Configure instance group for model deployment on Triton Inference Server.

        Args:
            model_config: Dict with model config for Triton Inference Server
        """
        instance_groups = []
        for device_kind, count in self._config.instance_group.items():
            instance_groups.append(
                {
                    "count": count,
                    "kind": device_kind.value,
                }
            )

        if instance_groups:
            model_config["instance_group"] = instance_groups

    def _set_model_transaction_policy(self, model_config: Dict) -> None:
        """Configure model transaction policy for model deployment on Triton Inference Server.

        Args:
            model_config: Dict with model config for Triton Inference Server
        """
        if self._config.decoupled:
            model_config["model_transaction_policy"] = {"decoupled": True}

    def _set_backend_parameters(self, model_config: Dict) -> None:
        """Configure backend parameters for model deployment on Triton Inference Server.

        Args:
            model_config: Dict with model config for Triton Inference Server
        """
        parameters = {}
        for key, value in self._config.backend_parameters.items():
            parameters[key] = {
                "string_value": str(value),
            }

        if parameters:
            model_config["parameters"] = parameters

    def _set_model_signature(self, model_config: Dict) -> None:
        """Configure model signature  for model deployment on Triton Inference Server.

        Args:
            model_config: Dict with model config for Triton Inference Server

        """

        def _rewrite_io_spec(spec_: TensorSpec) -> Dict:
            if spec_.dtype in [np.object_, object, bytes, np.bytes_]:
                dtype = "TYPE_STRING"
            else:
                # pytype: disable=attribute-error
                dtype = spec_.dtype().dtype
                # pytype: enable=attribute-error
                dtype = f"TYPE_{client_utils.np_to_triton_dtype(dtype)}"

            dims = spec_.shape

            item = {
                "name": spec_.name,
                "dims": list(dims),
                "data_type": dtype,
            }

            if spec_.optional:
                item["optional"] = True

            return item

        if self._config.inputs:
            model_config["input"] = [_rewrite_io_spec(spec) for spec in self._config.inputs]

        if self._config.outputs:
            outputs = [_rewrite_io_spec(spec) for spec in self._config.outputs]
            if outputs:
                optional_outputs = [o for o in outputs if o.get("optional")]
                if optional_outputs:
                    raise PyTritonBadParameterError(
                        "Optional flag for outputs is not supported. "
                        f"Outputs marked as optional: {', '.join([o['name'] for o in optional_outputs])}."
                    )
                model_config["output"] = outputs

    def _set_response_cache(self, model_config: Dict):
        """Configure response cache for model.

        Args:
            model_config: Dictionary where configuration is attached.
        """
        if self._config.response_cache:
            model_config["response_cache"] = {
                "enable": self._config.response_cache.enable,
            }