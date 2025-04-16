from enum import Enum, auto

class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4
    
    def is_completed(status):
        return status == Status.COMPLETED

for status in Status:
        print(f"{status.name} = {status.value}")


