from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Union

import yaml


class ClientException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Cloud(Enum):
    AWS = "aws"
    LAMBDA_LABS = "lambda"


@dataclass(kw_only=True)
class MachineConfig:
    name: str
    workdir: Optional[str] = None
    num_nodes: int = 1
    resources: Dict[str, dict] = field(default_factory=lambda: {})
    envs: Dict[str, Any] = field(default_factory=lambda: {})
    file_mounts: Dict[str, Union[str, dict]] = field(default_factory=lambda: {})
    setup: str = ""
    notebook: bool = False

    @staticmethod
    def _from_dict(config: dict, **overrides) -> "MachineConfig":
        updated_config = config.copy()
        for k, v in overrides.items():
            keys = k.split("/")
            curr_obj = updated_config
            for key in keys[:-1]:
                if key not in curr_obj:
                    curr_obj[key] = {}
                elif not isinstance(curr_obj[key], dict):
                    raise Exception(
                        f"Cannot set property {k} in config because it already has a non-dict value"
                    )

                curr_obj = curr_obj[key]

            curr_obj[keys[-1]] = v

        machine_config = MachineConfig(**updated_config)
        return machine_config

    @staticmethod
    def from_yaml(config_file: str, **overrides) -> "MachineConfig":
        with open(config_file, "r") as f:
            config = yaml.load(f, yaml.FullLoader)

        return MachineConfig._from_dict(config, **overrides)


@dataclass(kw_only=True)
class JobConfig:
    name: Optional[str] = None
    workdir: Optional[str] = None
    num_nodes: int = 1
    resources: Dict[str, dict] = field(default_factory=lambda: {})
    envs: Dict[str, Any] = field(default_factory=lambda: {})
    file_mounts: Dict[str, Union[str, dict]] = field(default_factory=lambda: {})
    setup: str = ""
    run: str

    @staticmethod
    def _from_dict(config: Dict, **overrides) -> "JobConfig":
        updated_config = config.copy()
        for k, v in overrides.items():
            keys = k.split("/")
            curr_obj = updated_config
            for key in keys[:-1]:
                if key not in curr_obj:
                    curr_obj[key] = {}
                elif not isinstance(curr_obj[key], dict):
                    raise Exception(
                        f"Cannot set property {k} in config because it already has a non-dict value"
                    )

                curr_obj = curr_obj[key]

            curr_obj[keys[-1]] = v

        job_config = JobConfig(**updated_config)
        return job_config

    @staticmethod
    def from_yaml(config_file: str, **overrides) -> "JobConfig":
        with open(config_file, "r") as f:
            config = yaml.load(f, yaml.FullLoader)

        job_config = JobConfig._from_dict(config, **overrides)
        return job_config


@dataclass(kw_only=True)
class ServiceConfigReadinessProbeSection:
    path: str
    post_data: Optional[dict] = None
    initial_delay_seconds: Optional[dict] = None


@dataclass(kw_only=True)
class ServiceConfigReplicaPolicySection:
    min_replicas: int
    max_replicas: Optional[int] = None
    target_qps_per_replica: Optional[int] = None
    upscale_delay_seconds: Optional[int] = None
    downscale_delay_seconds: Optional[int] = None


@dataclass(kw_only=True)
class ServiceConfigServiceSection:
    readiness_probe: ServiceConfigReadinessProbeSection
    replica_policy: ServiceConfigReplicaPolicySection

    @staticmethod
    def _from_dict(config: dict) -> "ServiceConfigServiceSection":
        readiness_probe = ServiceConfigReadinessProbeSection(
            **config["readiness_probe"]
        )
        replica_policy = ServiceConfigReplicaPolicySection(**config["replica_policy"])

        service_section = ServiceConfigServiceSection(
            readiness_probe=readiness_probe, replica_policy=replica_policy
        )
        return service_section


@dataclass(kw_only=True)
class ServiceConfig:
    name: str
    workdir: Optional[str] = None
    num_nodes: int = 1
    resources: Dict[str, dict] = field(default_factory=lambda: {})
    envs: Dict[str, Any] = field(default_factory=lambda: {})
    file_mounts: Dict[str, Union[str, dict]] = field(default_factory=lambda: {})
    setup: str = ""
    run: str
    service: ServiceConfigServiceSection

    @staticmethod
    def _from_dict(config: dict, **overrides) -> "ServiceConfig":
        updated_config = config.copy()
        for k, v in overrides.items():
            keys = k.split("/")
            curr_obj = updated_config
            for key in keys[:-1]:
                if key not in curr_obj:
                    curr_obj[key] = {}
                elif not isinstance(curr_obj[key], dict):
                    raise Exception(
                        f"Cannot set property {k} in config because it already has a non-dict value"
                    )

                curr_obj = curr_obj[key]

            curr_obj[keys[-1]] = v

        updated_config["service"] = ServiceConfigServiceSection._from_dict(
            updated_config["service"]
        )
        service_config = ServiceConfig(**updated_config)
        return service_config

    @staticmethod
    def from_yaml(config_file: str, **overrides) -> "ServiceConfig":
        with open(config_file, "r") as f:
            config = yaml.load(f, yaml.FullLoader)

        service_config = ServiceConfig._from_dict(config, **overrides)
        return service_config


class JobStatus(Enum):
    PENDING = "pending"
    INITIALIZING = "initializing"
    RUNNING_SETUP = "running_setup"
    RUNNING = "running"
    SHUTTING_DOWN = "shutting_down"
    FINISHED = "finished"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    ERROR = "error"
    UNKNOWN = "unknown"
    NOT_FOUND = "not found"
    UNAUTHORIZED = "unauthorized"
    UNREACHABLE = "unreachable"

    @classmethod
    def executing_statuses(cls):
        return [cls.RUNNING_SETUP, cls.RUNNING]


class MachineStatus(Enum):
    PENDING = "pending"
    INITIALIZING = "initializing"
    RUNNING_SETUP = "running_setup"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    TERMINATING = "terminating"
    TERINATED = "terminated"
    ERROR = "error"
    UNKNOWN = "unknown"
    NOT_FOUND = "not found"
    UNAUTHORIZED = "unauthorized"
    UNREACHABLE = "unreachable"

    @classmethod
    def executing_statuses(cls):
        return [cls.RUNNING_SETUP, cls.RUNNING]


class ServiceStatus(Enum):
    CONTROLLER_INIT = "CONTROLLER_INIT"
    REPLICA_INIT = "REPLICA_INIT"
    CONTROLLER_FAILED = "CONTROLLER_FAILED"
    READY = "READY"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    FAILED = "FAILED"
    FAILED_CLEANUP = "FAILED_CLEANUP"
    NO_REPLICA = "NO_REPLICA"
    DELETED = "DELETED"
    UNAUTHORIZED = "unauthorized"
    NOT_FOUND = "not found"
    UNKNOWN = "unknown"


class ReplicaStatus(Enum):
    PENDING = "PENDING"
    PROVISIONING = "PROVISIONING"
    STARTING = "STARTING"
    READY = "READY"
    NOT_READY = "NOT_READY"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    FAILED = "FAILED"
    FAILED_INITIAL_DELAY = "FAILED_INITIAL_DELAY"
    FAILED_PROBING = "FAILED_PROBING"
    FAILED_PROVISION = "FAILED_PROVISION"
    FAILED_CLEANUP = "FAILED_CLEANUP"
    PREEMPTED = "PREEMPTED"
    UNKNOWN = "UNKNOWN"


@dataclass(kw_only=True)
class Job:
    id: str
    status: JobStatus
    status_message: str
    cloud: Optional[Cloud]
    region: Optional[str]
    zone: Optional[str]
    instance_type: Optional[str]
    accelerators: Optional[str]
    ports: Optional[List[str]]
    disk_size: Optional[int]
    spot: Optional[bool]

    name: str
    num_nodes: int
    requested_resources: dict
    envs: dict
    file_mounts: dict
    setup: str
    run: str

    created_timestamp: int
    started_timestamp: Optional[int]
    updated_timestamp: int
    finished_timestamp: Optional[int]

    @classmethod
    def from_dict(cls, d):
        d["status"] = JobStatus(d["status"])
        if d.get("cloud", None):
            d["cloud"] = Cloud(d["cloud"])

        job = Job(**d)
        return job


@dataclass(kw_only=True)
class Machine:
    id: str
    status: MachineStatus
    status_message: str
    cloud: Optional[Cloud]
    region: Optional[str]
    zone: Optional[str]
    instance_type: Optional[str]
    accelerators: Optional[str]
    ports: Optional[List[str]]
    disk_size: Optional[int]
    spot: Optional[bool]

    name: str
    requested_resources: dict
    envs: dict
    file_mounts: dict
    setup: str
    notebook_token: Optional[str]
    notebook_url: Optional[str]

    created_timestamp: int
    started_timestamp: Optional[int]
    updated_timestamp: int
    terminated_timestamp: Optional[int]

    @classmethod
    def from_dict(cls, d):
        d["status"] = MachineStatus(d["status"])
        if d.get("cloud", None):
            d["cloud"] = Cloud(d["cloud"])

        machine = Machine(**d)
        return machine


@dataclass(kw_only=True)
class ReadinessProbeSection:
    path: str
    post_data: Optional[dict] = None
    initial_delay_seconds: int


@dataclass(kw_only=True)
class ReplicaPolicySection:
    min_replicas: int
    max_replicas: int
    target_qps_per_replica: Optional[int] = None
    upscale_delay_seconds: int
    downscale_delay_seconds: int


@dataclass(kw_only=True)
class ServiceSection:
    readiness_probe: ReadinessProbeSection
    replica_policy: ReplicaPolicySection

    @classmethod
    def from_dict(cls, d):
        d["readiness_probe"] = ReadinessProbeSection(**d["readiness_probe"])
        d["replica_policy"] = ReplicaPolicySection(**d["replica_policy"])

        service_section = ServiceSection(**d)
        return service_section


@dataclass(kw_only=True)
class Service:
    id: str
    status: ServiceStatus
    status_message: str

    name: str
    num_nodes: int
    requested_resources: dict
    envs: dict
    file_mounts: dict
    setup: str
    run: str
    service: ServiceSection

    uptime: int
    active_versions: List[int]

    created_timestamp: int
    updated_timestamp: int

    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d):
        d["status"] = ServiceStatus(d["status"])
        d["service"] = ServiceSection.from_dict(d["service"])

        service = Service(**d)
        return service


@dataclass(kw_only=True)
class ServiceReplica:
    service_id: str
    replica_id: int
    version: int
    status: Optional[ReplicaStatus]

    cloud: Optional[Cloud]
    region: Optional[str]
    zone: Optional[str]
    instance_type: Optional[str]
    accelerators: Optional[str]
    ports: Optional[List[str]]
    disk_size: Optional[int]
    spot: Optional[bool]

    created_timestamp: int
    updated_timestamp: int

    @classmethod
    def from_dict(cls, d):
        if d.get("status", None):
            d["status"] = ReplicaStatus(d["status"])
        else:
            d["status"] = None

        if d.get("cloud", None):
            d["cloud"] = Cloud(d["cloud"])

        replica = ServiceReplica(**d)
        return replica
