import enum

class Status(enum.Enum):
    INIT = 1
    PUMP_ON1 = 2
    PUMP_OFF1 = 3
    PUMP_ON2 = 4
    PUMP_OFF2 = 5
    PUMP_ON3 = 6
    PUMP_OFF3 = 7
    STABLE = 8
    IDLE = 9

class Monitoring:
    PUMP_ON_DELAY = [3000, 0, 3000]
    PUMP_OFF_DELAY = [5000, 5000, 5000]
    STABLE_DELAY = 20000
    SENSING_DELAY = 500
    IDLE_DELAY = 10000
    BUTTON_STATE = []
    numButton = 8

    distance1_value = 1
    distance2_value = 2


    def __init__(self, _soft_timer, _rs485):
        self.status = Status.INIT
        self.soft_timer = _soft_timer
        self.rs485 = _rs485
        for i in range(0, self.numButton):
            self.BUTTON_STATE.append(True)
        return
    
    def relayController(self, number, state):
        self.rs485.relayController(number, state)

    def MonitoringTask_Run(self):
        if self.status == Status.INIT:
            print("Init")
            if self.PUMP_ON_DELAY[0] == 0:
                self.status = Status.PUMP_ON2
            else:
                self.soft_timer.setTimer(0, self.PUMP_ON_DELAY[0])
                self.status = Status.PUMP_ON1
                self.BUTTON_STATE[0] = True
                #self.rs485.relayController(1, 1)

        elif self.status == Status.PUMP_ON1:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_on1")
                self.soft_timer.setTimer(0, self.PUMP_OFF_DELAY[0])
                self.status = Status.PUMP_OFF1
                self.BUTTON_STATE[0] = False
                #self.rs485.relayController(1, 0)

        elif self.status == Status.PUMP_OFF1:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_off1")
                if self.PUMP_ON_DELAY[1] == 0:
                    self.status = Status.PUMP_ON3
                else:
                    self.soft_timer.setTimer(0, self.PUMP_ON_DELAY[1])
                    self.status = Status.PUMP_ON2
                    self.BUTTON_STATE[1] = True
                    #self.rs485.relayController(2, 1)

        elif self.status == Status.PUMP_ON2:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_on2")
                self.soft_timer.setTimer(0, self.PUMP_OFF_DELAY[1])
                self.status = Status.PUMP_OFF2
                self.BUTTON_STATE[1] = False
                #self.rs485.relayController(2, 0)

        elif self.status == Status.PUMP_OFF2:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_off2")
                if self.PUMP_ON_DELAY[2] == 0:
                    self.status = Status.STABLE
                    self.soft_timer.setTimer(0, self.STABLE_DELAY)
                else:
                    self.soft_timer.setTimer(0, self.PUMP_ON_DELAY[2])
                    self.status = Status.PUMP_ON3
                    self.BUTTON_STATE[2] = True
                    #self.rs485.relayController(3, 1)

        elif self.status == Status.PUMP_ON3:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_on3")
                self.soft_timer.setTimer(0, self.PUMP_OFF_DELAY[2])
                self.status = Status.PUMP_OFF3
                self.BUTTON_STATE[2] = False
                #self.rs485.relayController(3, 0)

        elif self.status == Status.PUMP_OFF3:
            if self.soft_timer.isExpire(0) == 1:
                print("pump_off3")
                self.status = Status.STABLE
                self.soft_timer.setTimer(0, self.STABLE_DELAY)

        elif self.status == Status.STABLE:
            if self.soft_timer.isExpire(0) == 1:
                print("End")

        else:
            print("Invalid status")
        return