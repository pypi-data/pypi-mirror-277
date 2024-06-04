from datetime import datetime

import typing
from everai.autoscaling.action import Action, ScaleUpAction, ScaleDownAction, DecideResult
from everai.autoscaling.autoscaling_policy import AutoScalingPolicy
from everai.autoscaling.factors import Factors, QueueReason, WorkerStatus
from everai.placeholder import Placeholder


T = typing.TypeVar('T', int, float, datetime)
ArgumentType = typing.Union[T, Placeholder]


class SimpleAutoScalingPolicy(AutoScalingPolicy):
    # The minimum number of worker, even all of those are idle
    min_workers: ArgumentType
    # The maximum number of worker, even there are some request in queued_request.py
    max_workers: ArgumentType
    # The max_queue_size let scheduler know it's time to scale up
    max_queue_size: ArgumentType
    # The quantity of each scale up
    scale_up_step: ArgumentType
    # The max_idle_time in seconds let scheduler witch worker should be scale down
    max_idle_time: ArgumentType

    def __init__(self,
                 min_workers: ArgumentType[int] = 1,
                 max_workers: ArgumentType[int] = 1,
                 max_queue_size: ArgumentType[int] = 1,
                 max_idle_time: ArgumentType[int] = 120,
                 scale_up_step: ArgumentType[int] = 1):

        self.min_workers = min_workers
        self.max_workers = max_workers
        self.max_queue_size = max_queue_size
        self.max_idle_time = max_idle_time
        self.scale_up_step = scale_up_step

    def get_argument(self, name: str) -> int:
        assert hasattr(self, name)
        prop = getattr(self, name)

        if isinstance(prop, int):
            return prop
        elif callable(prop):
            return prop()
        else:
            raise TypeError(f'Invalid argument type {type(prop)} for {name}')

    def get_arguments(self):
        min_workers = int(self.get_argument('min_workers'))
        max_workers = int(self.get_argument('max_workers'))
        max_queue_size = int(self.get_argument('max_queue_size'))
        max_idle_time = int(self.get_argument('max_idle_time'))
        scale_up_step = int(self.get_argument('scale_up_step'))

        return min_workers, max_workers, max_queue_size, max_idle_time, scale_up_step

    @staticmethod
    def should_scale_up(factors: Factors, max_queue_size: int) -> bool:
        busy_count = 0

        # don't do scale up again
        in_flights = [worker for worker in factors.workers if worker.status == WorkerStatus.Inflight]
        if len(in_flights) > 0:
            return False

        for req in factors.queue.requests:
            if req.queue_reason == QueueReason.QueueDueBusy:
                busy_count += 1
        return busy_count > max_queue_size

    def decide(self, factors: Factors) -> DecideResult:
        min_workers, max_workers, max_queue_size, max_idle_time, scale_up_step = self.get_arguments()
        print(f'min_workers: {min_workers}, max_workers: {max_workers}, '
              f'max_queue_size: {max_queue_size}, max_idle_time: {max_idle_time}, scale_up_step: {scale_up_step}')

        now = int(datetime.now().timestamp())
        # scale up to min_workers
        if len(factors.workers) < min_workers:
            print(f'workers {len(factors.workers)} less than min_workers {min_workers}')
            return DecideResult(
                max_workers=max_workers,
                actions=[ScaleUpAction(count=min_workers - len(factors.workers))],
            )

        # ensure after scale down, satisfied the max_workers
        max_scale_up_count = max_workers - len(factors.workers)
        scale_up_count = 0
        if SimpleAutoScalingPolicy.should_scale_up(factors, max_queue_size):
            scale_up_count = min(max_scale_up_count, scale_up_step)

        if scale_up_count > 0:
            return DecideResult(
                max_workers=max_workers,
                actions=[ScaleUpAction(count=scale_up_count)],
            )

        # check if scale down is necessary
        scale_down_actions = []
        factors.workers.sort(key=lambda x: x.started_at, reverse=True)
        for worker in factors.workers:
            if (worker.number_of_sessions == 0 and worker.status == WorkerStatus.Free and
                    now - worker.last_service_time >= max_idle_time):
                scale_down_actions.append(ScaleDownAction(worker_id=worker.worker_id))

        running_workers = 0
        for worker in factors.workers:
            if worker.status == WorkerStatus.Free:
                running_workers += 1

        # ensure after scale down, satisfied the min_workers
        max_scale_down_count = running_workers - min_workers
        scale_down_count = min(max_scale_down_count, len(scale_down_actions))
        return DecideResult(
            max_workers=max_workers,
            actions=scale_down_actions[:scale_down_count]
        )
