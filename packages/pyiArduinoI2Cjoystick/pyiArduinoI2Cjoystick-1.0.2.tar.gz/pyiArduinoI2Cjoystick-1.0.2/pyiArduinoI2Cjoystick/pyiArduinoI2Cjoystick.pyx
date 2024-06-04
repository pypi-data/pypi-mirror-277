# distutils: language = c++
# cython: language_level = 3

from iarduino_I2C_Joystick cimport iarduino_I2C_Joystick
#from time import sleep

DEF_CHIP_ID_FLASH =  0x3C
DEF_CHIP_ID_METRO =  0xC3

# Адреса регистров модуля:
REG_FLAGS_0                  =  0x00
REG_BITS_0                   =  0x01
REG_FLAGS_1                  =  0x02
REG_BITS_1                   =  0x03
REG_MODEL                    =  0x04
REG_VERSION                  =  0x05
REG_ADDRESS                  =  0x06
REG_CHIP_ID                  =  0x07
REG_JOY_AVERAGING            =  0x08
REG_JOY_DEAD_ZONE            =  0x09
REG_JOY_KEY                  =  0x10
REG_JOY_KEY_TIM              =  0x11
REG_JOY_AXIS_X               =  0x12
REG_JOY_AXIS_Y               =  0x13
REG_JOY_X_ADC_L              =  0x14
REG_JOY_Y_ADC_L              =  0x16
REG_JOY_X_RIGHT_L            =  0x18
REG_JOY_X_CEN_L              =  0x1A
REG_JOY_X_LEFT_L             =  0x1C
REG_JOY_Y_UP_L               =  0x1E
REG_JOY_Y_CEN_L              =  0x20
REG_JOY_Y_DOWN_L             =  0x22
# Позиция битов и флагов:
JOY_KEY_PUSHED               =  0x80
JOY_KEY_RELEASED             =  0x40
JOY_KEY_PRESSED              =  0x20
JOY_KEY_TRIGGER              =  0x10
JOY_KEY_HOLD_05              =  0x08
JOY_KEY_HOLD_10              =  0x04
JOY_KEY_HOLD_20              =  0x02
JOY_KEY_CHANGED              =  0x01

KEY_PUSHED                   =  1
KEY_RELEASED                 =  2
KEY_PRESSED                  =  3
KEY_TRIGGER                  =  4
KEY_HOLD_05                  =  5
KEY_HOLD_10                  =  6
KEY_HOLD_20                  =  7
KEY_CHANGED                  =  8
KEY_TIME_PRESSED             =  9

NO_BEGIN = 1


cdef class pyiArduinoI2Cjoystick():
    cdef iarduino_I2C_Joystick c_module

    def __cinit__(self, address=None, auto=None):

        if address is not None:

            self.c_module = iarduino_I2C_Joystick(address)

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

            self.c_module = iarduino_I2C_Joystick()

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

    def setPullI2C(self, f = True):
        return self.c_module.setPullI2C(f)

    def getButton(self, t):
        return self.c_module.getButton(t)

    def getPosition_X(self):
        return self.c_module.getPosition_X()

    def getPosition_Y(self):
        return self.c_module.getPosition_Y()

    def getADC_X(self):
        return self.c_module.getADC_X()

    def getADC_Y(self):
        return self.c_module.getADC_Y()

    def setCalibration_X(self, x_min, x_cen, x_max):
        return self.c_module.setCalibration_X(x_min, x_cen, x_max)

    def setCalibration_Y(self, y_min, y_cen, y_max):
        return self.c_module.setCalibration_Y(y_min, y_cen, y_max)

    def setDeadZone(self, zone):
        return self.c_module.setDeadZone(zone)

    def setAveraging(self, a):
        return self.c_module.setAveraging(a)

# now the fun part...

    def getPosition(self):
        nx = self.getPosition_X()
        ny = self.getPosition_Y()
        return nx, ny

    def getADC(self):
        nx = self.getADC_X()
        ny = self.getADC_Y()
        return nx, ny

    def getCalibration_X(self):
        self.c_module.updateCalX()
        l = self.c_module.getMinX()
        c = self.c_module.getCenX()
        r = self.c_module.getMaxX()
        return l, c, r

    def getCalibration_Y(self):
        self.c_module.updateCalY()
        d = self.c_module.getMinY()
        c = self.c_module.getCenY()
        u = self.c_module.getMaxY()
        return d, c, u

    def __getattr__(self, item):

        if item == 'x' or item == 'X':
            return self.c_module.getPosition_X()

        if item == 'y' or item == 'Y':
            return self.c_module.getPosition_Y()

        if item == 'ax' or item == 'AX':
            return self.c_module.getADC_X()

        if item == 'ay' or item == 'AY':
            return self.c_module.getADC_Y()
