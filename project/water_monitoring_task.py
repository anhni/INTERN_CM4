import enum
from rs485 import *

class WMT_Status(enum.Enum):
    INIT = 1
    PUMP_ON = 2
    PUMP_OFF = 3
    STABLE = 4
    READ_DIS = 5
    IDLE = 6

class waterMonitoringTask:
    PUMP_ON_DELAY = 3000
    PUMP_OFF_DELAY = 5000
    STABLE_DELAY = 20000
    SENSING_DELAY = 500
    IDLE_DELAY = 10000

    DIS_Value = 2999
    BUTTON_STATE = True

    def __init__(self,_rs485, _soft_timer):
        print("Init monitor water")
        self.status = WMT_Status.INIT
        self.rs485 = _rs485
        self.soft_timer = _soft_timer
        return

    def setPumpOn(self):
        print("Pump is On")
        self.rs485.relayController(1, 1)

    def setPumpOff(self):
        print("Pump is Off")
        self.rs485.relayController(1, 0)

    def waterMoniteringTask_Run(self):
        print("Monitering Water is Running!!")
        if self.status == WMT_Status.INIT:
            print("Pump is On")
            self.soft_timer.set_timer(0, self.PUMP_ON_DELAY)
            self.status = WMT_Status.PUMP_ON
            self.BUTTON_STATE = True
            self.rs485.relayController(1, 1)

        elif self.status == WMT_Status.PUMP_ON:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.soft_timer.set_timer(0, self.PUMP_OFF_DELAY)
                self.status = WMT_Status.PUMP_OFF
                self.BUTTON_STATE = False
                self.rs485.relayController(1, 0)
                print("Pump is Off")

        elif self.status == WMT_Status.PUMP_OFF:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.soft_timer.set_timer(0, self.STABLE_DELAY)
                self.status = WMT_Status.STABLE
                print("Stabilizing")

        elif self.status == WMT_Status.STABLE:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.soft_timer.set_timer(0, self.SENSING_DELAY)
                self.status = WMT_Status.READ_DIS
                self.rs485.sendReadDistance(9)
                print("Reading")

        elif self.status == WMT_Status.READ_DIS:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.soft_timer.set_timer(0, self.SENSING_DELAY)
                self.status = WMT_Status.IDLE
                self.DIS_Value = self.rs485.readDistance()
                print("Idling")

        elif self.status == WMT_Status.IDLE:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.soft_timer.set_timer(0, self.IDLE_DELAY)
                self.status = WMT_Status.INIT
                print(">>>>>>")

        else:
            print("Invalid status")
        return