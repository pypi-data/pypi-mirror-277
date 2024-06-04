# distutils: language = c++
# cython: language_level = 3

from iarduino_I2C_Motor cimport iarduino_I2C_Motor
#from time import sleep

DEF_CHIP_ID_FLASH     = 0x3C
DEF_CHIP_ID_METRO     = 0xC3
DEF_MODEL_MOT         = 0x14
#Адреса регистров модуля:
REG_FLAGS_0           = 0x00
REG_BITS_0            = 0x01
REG_FLAGS_1           = 0x02
REG_BITS_1            = 0x03
REG_MODEL             = 0x04
REG_VERSION           = 0x05
REG_ADDRESS           = 0x06
REG_CHIP_ID           = 0x07
REG_MOT_FREQUENCY_L   = 0x08
REG_MOT_FREQUENCY_H   = 0x09
REG_MOT_MAX_RPM_DEV   = 0x0A
REG_MOT_FLG           = 0x10
REG_MOT_MAGNET        = 0x11
REG_MOT_REDUCER_L     = 0x12
REG_MOT_REDUCER_C     = 0x13
REG_MOT_REDUCER_H     = 0x14
REG_MOT_SET_PWM_L     = 0x15
REG_MOT_SET_PWM_H     = 0x16
REG_MOT_SET_RPM_L     = 0x17
REG_MOT_SET_RPM_H     = 0x18
REG_MOT_GET_RPM_L     = 0x19
REG_MOT_GET_RPM_H     = 0x1A
REG_MOT_GET_REV_L     = 0x1B
REG_MOT_GET_REV_C     = 0x1C
REG_MOT_GET_REV_H     = 0x1D
REG_MOT_STOP_REV_L    = 0x1E
REG_MOT_STOP_REV_C    = 0x1F
REG_MOT_STOP_REV_H    = 0x20
REG_MOT_STOP_TMR_L    = 0x21
REG_MOT_STOP_TMR_C    = 0x22
REG_MOT_STOP_TMR_H    = 0x23
REG_MOT_STOP          = 0x24
REG_BITS_2            = 0x25
REG_MOT_VOLTAGE       = 0x26
REG_MOT_NOMINAL_RPM_L = 0x27
REG_MOT_NOMINAL_RPM_H = 0x28

#Позиция битов и флагов:
MOT_FLG_RPM_EN        = 0x80
MOT_FLG_RPM_ERR       = 0x20
MOT_FLG_DRV_ERR       = 0x10
MOT_FLG_STOP          = 0x02
MOT_FLG_NEUTRAL       = 0x01
MOT_BIT_STOP          = 0x02
MOT_BIT_NEUTRAL       = 0x01
MOT_BIT_DIR_CKW       = 0x04
MOT_BIT_INV_RDR       = 0x02
MOT_BIT_INV_PIN       = 0x01

MOT_ERR_SPD           = 1
MOT_ERR_DRV           = 2
MOT_MET               = 3
MOT_SEC               = 4
MOT_M_S               = 5
MOT_REV               = 6
MOT_RPM               = 7
MOT_PWM               = 8

NO_BEGIN = 1

cdef class pyiArduinoI2Cmotor:
    cdef iarduino_I2C_Motor c_module

    def __cinit__(self, address=None, auto=None):

        if address is not None:

            self.c_module = iarduino_I2C_Motor(address)

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля,"
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

        else:

            self.c_module = iarduino_I2C_Motor()

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля, "
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

    def begin(self):
        return self.c_module.begin()

    def changeAddress(self, unsigned char newAddr):
        return self.c_module.changeAddress(newAddr)

    def reset(self):
        return self.c_module.reset()

    def getAddress(self):
        return self.c_module.getAddress()

    def getVersion(self):
        return self.c_module.getVersion()

    def getPullI2C(self):
        return self.c_module.getPullI2C()

    def setPullI2C(self, flag=None):
        if flag is not None:
            return self.c_module.setPullI2C(flag)
        else:
            return self.c_module.setPullI2C(True)

    def setFreqPWM(self, freq):
        return self.c_module.setFreqPWM(freq)

    def setMagnet(self, num):
        return self.c_module.setMagnet(num)

    def getMagnet(self):
        return self.c_module.getMagnet()

    def setReducer(self, gear):
        return self.c_module.setReducer(gear)

    def getReducer(self):
        return self.c_module.getReducer()

    def setError(self, dev):
        return self.c_module.setError(dev)

    def getError(self):
        return self.c_module.getError()

    def setSpeed(self, valSpeed, typeSpeed, valStop=None, typeStop=None):
        if valStop is not None:
            return self.c_module.setSpeed(valSpeed, typeSpeed, valStop, typeStop)
        else:
            return self.c_module.setSpeedOverloaded(valSpeed, typeSpeed)

    def getSpeed(self, typ):
        return self.c_module.getSpeed(typ)

    def setStop(self, val=None, typ=None):
        if val is not None:
            return self.c_module.setStop(val, typ)
        else:
            return self.c_module.setStopOverloaded()

    def getStop(self, typ):
        return self.c_module.getStop(typ)

    def setStopNeutral(self, f):
        return self.c_module.setStopNeutral(f)

    def getStopNeutral(self):
        return self.c_module.getStopNeutral()

    def setDirection(self, flgCKW):
        return self.c_module.setDirection(flgCKW)

    def getDirection(self):
        return self.c_module.getDirection()

    def setInvGear(self, invRDR, invPIN):
        return self.c_module.setInvGear(invRDR, invPIN)

    def getInvGear(self):
        return self.c_module.getInvGear()

    def getSum(self, typ):
        return self.c_module.getSum(typ)

    def delSum(self):
        return self.c_module.delSum()

    def setVoltage(self, volt):
        return self.c_module.setVoltage(volt)

    def getVoltage(self):
        return self.c_module.getVoltage()

    def setNominalRPM(self, val):
        return self.c_module.setNominalRPM(val)

    def getNominalRPM(self):
        return self.c_module.getNominalRPM()

    def saveManufacturer(self, code):
        return self.c_module.saveManufacturer(code)

    property radius:
        def __get__(self):
            return self.c_module.radius
        def __set__(self, float var):
            self.c_module.radius = var
