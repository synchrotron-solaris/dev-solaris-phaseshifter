"""This is SHG device class based on the facadedevice library"""

from facadedevice import Facade, proxy_attribute, proxy_command
from tango import AttrWriteType, DevState


class PhaseShifter(Facade):


    def safe_init_device(self):
        """
        Docstring for 'safe_init_device' - it is just safe initialization of the DS
        :return:
        """
        super(PhaseShifter, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running")

    # Proxy attributes
        # only-to-compare PART
    #
    # Temperature = proxy_attribute(
    #     dtype=float,
    #     property_name="TemperatureModbus",
    #     access=AttrWriteType.READ,
    #     description="This attribute specifies temperature"
    # )
    #
    #
    # @proxy_command(
    #     property_name="StopPumpTag",
    #     write_attribute=True)
    # def StopPump(self, subcommand):
    #     """
    #     This command stops the pump.
    #     :param subcommand:
    #     :return:
    #     """
    #     subcommand(1)


run=PhaseShifter.run_server()

if __name__ == '__main__':
   run()
