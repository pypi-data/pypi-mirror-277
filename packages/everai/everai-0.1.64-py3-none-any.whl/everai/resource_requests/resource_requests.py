import typing


class ResourceRequests:
    cpu_num: int
    gpu_num: int
    memory_mb: int

    region_constraints: typing.List[str]
    cpu_constraints: typing.List[str]
    gpu_constraints: typing.List[str]

    driver_version_constraints: str
    cuda_version_constraints: str

    def __init__(self, cpu_num: int = 1, gpu_num: int = 0, memory_mb: int = 1024,
                 region_constraints: typing.List[str] = None,
                 cpu_constraints: typing.List[str] = None,
                 gpu_constraints: typing.List[str] = None,
                 driver_version_constraints: str = None,
                 cuda_version_constraints: str = None,
                 ):
        """
        :param cpu_num: Number of CPU, default is 1
        :param gpu_num: Number of GPU, default is 0
        :param memory_mb: Memory size in MB, default is 1024
        :param region_constraints: Region constraints, default is any region
        :param cpu_constraints: Cpu constraints, default is any cpu type
        :param gpu_constraints: Gpu constraints, default is any gpu type
        :param driver_version_constraints: Driver version constraints, default is any version， e.g. >=535.154.05
        :param cuda_version_constraints: Cuda version constraints, default is any version, e.g. >=12.2
        """
        assert cpu_num > 0, "cpu_num must be positive"
        assert gpu_num >= 0
        assert memory_mb > 0, "memory_mb must be positive"

        self.cpu_num = cpu_num
        self.gpu_num = gpu_num
        self.memory_mb = memory_mb

        self.region_constraints = region_constraints
        self.cpu_constraints = cpu_constraints
        self.gpu_constraints = gpu_constraints
        self.driver_version_constraints = driver_version_constraints
        self.cuda_version_constraints = cuda_version_constraints
