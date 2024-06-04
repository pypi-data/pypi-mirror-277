cdef extern from "iarduino_I2C_Joystick.cpp":
    pass

cdef extern from "iarduino_I2C_Joystick.h":
    cdef cppclass iarduino_I2C_Joystick:
        iarduino_I2C_Joystick() except +
        iarduino_I2C_Joystick(unsigned char) except +
        bint begin()
        bint changeAddress(unsigned char)
        bint reset()
        unsigned char getAddress()
        unsigned char getVersion()
        bint getPullI2C()
        bint setPullI2C(bint)
        unsigned short getButton(unsigned char)
        int getPosition_X()
        int getPosition_Y()
#template<typename T> bool getPosition(T &x, T &y)
        int getADC_X()
        int getADC_Y()
#template<typename T> bool getADC(T &x, T &y)
#template<typename T> bool getCalibration_X(T &l, T &c, T &r)
#template<typename T> bool getCalibration_Y(T &d, T &c, T &u)
        bint setCalibration_X(int, int, int)
        bint setCalibration_Y(int, int, int)
        bint setDeadZone(float)
        bint setAveraging(unsigned char)
        bint updateCalX()
        bint updateCalY()
        int getMinX()
        int getCenX()
        int getMaxX()
        int getMinY()
        int getCenY()
        int getMaxY()

#cdef extern from "iarduino_I2C_PI.h":
#    cdef cppclass iarduino_I2C:
#        bint readBytes(unsigned char, unsigned char, unsigned char*, unsigned char)
