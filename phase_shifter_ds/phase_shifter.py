"""This is PhaseShifter device class based on the facadedevice library"""

from facadedevice import Facade, proxy_attribute, logical_attribute
from tango import AttrWriteType, DevState
from tango.server import device_property
import csv


class PhaseShifter(Facade):
    """
    This PhaseShifter class is based on the `facadedevice` library.
    Its main purpose is to change received voltage into degrees accordingly to
    the data provided in external file. During initialization, data from this file
    is imported into two lists: one for voltage and one for degrees. In order to
    do it user has to specify `ConfigurationPath` (path to the `.csv` file).
    Conversion itself is quite simple, it is just a comparison between two lists.
    """

    def safe_init_device(self):
        """
        Method `safe_init_device` - it is just safe initialization of
        the DS as well as reading voltages and degrees from conf file
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

    #proxy attribute
    Voltage = proxy_attribute(
        dtype=float,
        property_name="VoltageSource",
        access=AttrWriteType.READ,
        description="This attribute specifies received voltage which is"
                    "meant to be changed into degrees"
    )
    #conf path as a device property
    ConfigurationPath = device_property(dtype=str)

    # logical attribute
    @logical_attribute(
        dtype=float,
        bind=['Voltage'],
        description="This is an attribute which shows degrees accordingly to "
                    "data in a .csv configuration")
    def Degrees(self, val):
        """
        This attribute changes voltage into degrees accordingly to data
        in a .csv configuration
        :param val:
        :return:
        """
        for i in range(len(self.arrayVoltages)):
            if float(self.arrayVoltages[i])==val:
                return float(self.arrayPhaseShifts[i])



run=PhaseShifter.run_server()

if __name__ == '__main__':
   run()
