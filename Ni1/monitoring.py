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
<<<<<<< HEAD
    RELAY_IN = 12
    RELAY_OUT = 13
=======
    SENSOR1 = 10
    SENSOR2 = 11
>>>>>>> e6e7d1ba0d6f8f831e18aad66e69a66e4e67800e

class Monitoring:
    PUMP_ON_DELAY = [3000, 4000, 5000, 0, 1000, 0]
    PUMP_OFF_DELAY = [5000, 5000, 5000]
    STABLE_DELAY = 5000
    SENSING_DELAY = 500
    IDLE_DELAY = 10000
    BUTTON_STATE = []
    numButton = 8
    count = 0

    distance1_value = 1
    distance2_value = 2


    def __init__(self, _soft_timer, _rs485):
        self.status = Status.INIT
        self.distanceStatus = Status.INIT
        self.soft_timer = _soft_timer
        self.rs485 = _rs485
        for i in range(0, self.numButton):
            self.BUTTON_STATE.append(True)
        return
    
    def relayController(self, number, state):
        self.rs485.relayController(number, state)

    def distanceController(self, number):
        self.rs485.distanceController(number)

    def getDistance(self):
        if self.distanceStatus == Status.INIT:
            self.soft_timer.setTimer(5, self.SENSING_DELAY)
            self.distanceStatus == Status.SENSOR1
            self.distanceController(9)
        elif self.distanceStatus == Status.SENSOR1:
            self.distance1_value = self.rs485.serial_read_data()
            self.soft_timer.setTimer(5, self.SENSING_DELAY)
            self.distanceStatus == Status.SENSOR2
            self.distanceController(12)
        elif self.distanceStatus == Status.SENSOR2:
            self.distance2_value = self.rs485.serial_read_data()
            self.distanceStatus = Status.INIT
        else:
            self.distanceStatus = Status.INIT


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

    def MonitoringTask_Run1(self):
        if self.status == Status.INIT:
            print("Init")
            self.status = Status.RELAY_IN
            self.soft_timer.setTimer(0, self.PUMP_ON_DELAY[0])
            self.soft_timer.setTimer(1, self.PUMP_ON_DELAY[1])
            self.soft_timer.setTimer(2, self.PUMP_ON_DELAY[2])
            if self.PUMP_ON_DELAY[0]:
                print("1: On")
                self.BUTTON_STATE[0] = True
            else:
                self.count += 1
            if self.PUMP_ON_DELAY[1]:
                print("2: On")
                self.BUTTON_STATE[1] = True
            else:
                self.count += 1
            if self.PUMP_ON_DELAY[2]:
                print("3: On")
                self.BUTTON_STATE[2] = True
            else:
                self.count += 1

        if self.status == Status.RELAY_IN:
            if self.soft_timer.isExpire(0) == 1:
                print("1: Off")
                self.count += 1
                self.soft_timer.setTimer(0, 0)
            if self.soft_timer.isExpire(1) == 1:
                print("2: Off")
                self.count += 1
                self.soft_timer.setTimer(1, 0)
            if self.soft_timer.isExpire(2) == 1:
                print("3: Off")
                self.count += 1
                self.soft_timer.setTimer(2, 0)

            if self.count == 3:
                self.count = 0
                self.status = Status.STABLE
                self.soft_timer.setTimer(0, self.STABLE_DELAY)

        if self.status == Status.STABLE:
            if self.soft_timer.isExpire(0) == 1:
                self.status = Status.RELAY_OUT
                self.soft_timer.setTimer(3, self.PUMP_ON_DELAY[3])
                self.soft_timer.setTimer(4, self.PUMP_ON_DELAY[4])
                self.soft_timer.setTimer(5, self.PUMP_ON_DELAY[5])
                if self.PUMP_ON_DELAY[3]:
                    print("4: On")
                    self.BUTTON_STATE[3] = True
                else:
                    self.count += 1
                if self.PUMP_ON_DELAY[4]:
                    print("5: On")
                    self.BUTTON_STATE[4] = True
                else:
                    self.count += 1
                if self.PUMP_ON_DELAY[5]:
                    print("6: On")
                    self.BUTTON_STATE[5] = True
                else:
                    self.count += 1

        if self.status == Status.RELAY_OUT:
            if self.soft_timer.isExpire(3) == 1:
                print("4: Off")
                self.count += 1
                self.soft_timer.setTimer(3, 0)
            if self.soft_timer.isExpire(4) == 1:
                print("5: Off")
                self.count += 1
                self.soft_timer.setTimer(4, 0)
            if self.soft_timer.isExpire(5) == 1:
                print("6: Off")
                self.count += 1
                self.soft_timer.setTimer(5, 0)

            if self.count == 3:
                self.count = 0
                print("End")



