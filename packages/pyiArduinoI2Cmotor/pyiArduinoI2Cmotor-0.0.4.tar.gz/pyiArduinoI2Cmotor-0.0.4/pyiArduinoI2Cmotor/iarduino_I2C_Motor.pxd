cdef extern from "iarduino_I2C_Motor.cpp":
    pass

cdef extern from "iarduino_I2C_Motor.h":
    cdef cppclass iarduino_I2C_Motor:
        iarduino_I2C_Motor() except +
        iarduino_I2C_Motor(unsigned char) except +
        bint begin()
        bint changeAddress(unsigned char)
        bint reset()
        unsigned char getAddress()
        unsigned char getVersion()
        bint getPullI2C()
        bint setPullI2C(bint)
        bint setFreqPWM(unsigned short)
        bint setMagnet(unsigned char)
        unsigned char getMagnet()
        bint setReducer(float)
        float getReducer()
        bint setError(unsigned char)
        unsigned char getError()
        bint setSpeed(float,unsigned char,float,unsigned char)
        bint setSpeedOverloaded "setSpeed"(float, unsigned char)
        float getSpeed(unsigned char)
        bint setStop(float, unsigned char)
        bint setStopOverloaded "setStop"()
        float getStop(unsigned char)
        bint setStopNeutral(bint)
        bint getStopNeutral()
        bint setDirection(bint)
        bint getDirection()
        bint setInvGear(bint, bint)
        unsigned char getInvGear()
        float getSum(unsigned char)
        bint  delSum()
        bint  setVoltage(float)
        float getVoltage()
        bint  setNominalRPM(unsigned short)
        unsigned short getNominalRPM()
        bint saveManufacturer(unsigned long)
        float radius
