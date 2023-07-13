import enum

class Status(enum.Enum):
    INIT = 1
    PUMP_ON = 2
    PUMP_OFF = 3
    STABLE = 4

class Monitoring:
    PUMP_ON_DELAY = 3000
    PUMP_OFF_DELAY = 5000
    STABLE_DELAY = 20000
    SENSING_DELAY = 500
    IDLE_DELAY = 10000
    BUTTON_STATE = []
    numButton = 6

    def __init__(self, _soft_timer, _rs485):
        self.status = Status.INIT
        self.soft_timer = _soft_timer
        self.rs485 = _rs485
        for i in range(0, self.numButton):
            self.BUTTON_STATE.append(True)
        return
    
    def MonitoringTask_Run(self):
        if self.status == Status.INIT:
            self.soft_timer.setTimer(0, self.PUMP_ON_DELAY)
            self.status = Status.PUMP_ON
            self.rs485.relayController(1, 1)
        elif self.status == Status.PUMP_ON:
            self.soft_timer.setTimer(0, self.PUMP_OFF_DELAY)
            self.status = Status.PUMP_OFF
            self.rs485.relayController(1, 0)
        elif self.status == Status.PUMP_OFF:
            self.soft_timer.setTimer(0, self.STABLE_DELAY)
            self.status = Status.STABLE
            self.rs485.relayController(1, 0)