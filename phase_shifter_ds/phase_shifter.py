"""This is PhaseShifter device class based on the facadedevice library"""

from facadedevice import Facade, proxy_attribute, logical_attribute
from tango import AttrWriteType, DevState
from tango.server import device_property
import csv


class PhaseShifter(Facade):


    def safe_init_device(self):
        """
        Docstring for 'safe_init_device' - it is just safe initialization of the DS
        :return:
        """
        super(PhaseShifter, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")
        self.arrayVoltages = [0]
        self.arrayPhaseShifts = [0]
        with open(str(self.ConfigurationPath), 'rb') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            conversionFlagPhaseShifter = 0
            for row in reader:
                try:
                    float(row[1])
                    conversionFlagPhaseShifter = 1
                except ValueError:
                    conversionFlagPhaseShifter = 0
                if self.arrayPhaseShifts == [0.0] and conversionFlagPhaseShifter:
                    self.arrayPhaseShifts = [row[1]]
                elif conversionFlagPhaseShifter:
                    self.arrayPhaseShifts.append(row[1])

        with open(str(self.ConfigurationPath), 'rb') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            conversionFlagVoltage = 0
            for row in reader:
                try:
                    float(row[0])
                    conversionFlagVoltage = 1
                except ValueError:
                    conversionFlagVoltage = 0
                if self.arrayVoltages == [0.0] and conversionFlagVoltage:
                    self.arrayVoltages = [row[0]]
                elif conversionFlagVoltage:
                    self.arrayVoltages.append(row[0])

    # Proxy attribute

    Voltage = proxy_attribute(
        dtype=float,
        property_name="VoltageSource",
        access=AttrWriteType.READ_WRITE,
        description="This attribute specifies voltage source"
    )


    ConfigurationPath = device_property(dtype=str)

    # logical attribute

    @logical_attribute(
        dtype=float,
        bind=['Voltage'],
        description="This is an attribute which shows degrees accordingly to data in a .csv configuration")
    def degrees(self, val):
        """
        This changes voltage into degrees accordingly to data in a .csv configuration
        :param val:
        :return:
        """
        for i in range(len(self.arrayVoltages)):
            if val==self.arrayVoltages:
                return self.arrayPhaseShifts[i]



run=PhaseShifter.run_server()

if __name__ == '__main__':
   run()
