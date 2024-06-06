from utils import logger, load_config,  get_from_dict
from pymodbus.client import ModbusTcpClient
from typing_extensions import Self
import time
from typing import Union, List, Dict, Callable



'''
The module is intended to provide an interface during communication with modbus Expansions. 
The module provides writing/reading functions for output nodes and reading for digital inputs. 
It operates for single bit, group or all bits of a Expansion. Each Expansion is initialised by an according class. 
'''
class Expansion:
    '''
    A parent class that incorporates basic attributes and methods common to all types of Expansions.
    This serves as the base class encapsulating common functionality for both input and output Expansions.
    '''

    def __init__(self,  IP, port=502):
        self.IP = IP
        self.port = port
        self.client = ModbusTcpClient(IP)
        self.type = 'generic'
    def _catcher(errors=(Exception,), value=''):
        ''''
        Decorator function to catch exceptions and log them.

        :param errors: Tuple of exceptions to catch.
        :param value: Value to return upon catching exceptions.
        :return: Wrapper function.
        '''

        def catcher(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except errors as e:
                    logger.error(f'Error in {func.__name__} with args {args}, {kwargs}: {e}')
                    return value

            return wrapper

        return catcher

    @_catcher
    def connect(self) -> bool:
        '''
        Establishes a connection with the Expansion.
        :return: None
        '''
        self.client.connect()
        if self.client.is_socket_open():
            logger.info(f'{self.type.upper()} Expansion at IP {self.IP} and port {self.port} is connected')
            return True
        else:
            logger.error(f'Failed to connect to {self.type.upper()} Expansion at IP {self.IP} and port {self.port}')
            return False


    @_catcher
    def disconnect(self) -> Self:
        '''
        Closes the established connection with the Expansion.
        :return: True if disconnection is successful, False otherwise.
        '''
        self.client.close()
        if not self.client.is_socket_open():
            logger.info(f'{self.type.upper()} Expansion at IP {self.IP} and port {self.port} has disconnected')
            return True
        else:
            logger.error(f'Failed to disconnect {self.type.upper()} Expansion at IP {self.IP} and port {self.port}')
            return False

    _catcher = staticmethod(_catcher(value='default'))

class InputExpansion(Expansion):
    '''
    This subclass inherits from the Expansion class and specializes in operations applied to input Expansions.
    The class methods enable reading of relays individually, in groups, or all together.
    During initialization of the class object, IP and port parameters have to be passed.
    '''

    def __init__(self, *args, **kwargs):
        super(InputExpansion, self).__init__(*args, **kwargs)
        self.type = 'input'
        logger.info(f'INPUT Expansion with IP {self.IP}')

    @Expansion._catcher
    def get_bit(self, address:int) -> Union[bool, None]:
        '''
         Reads information from a specific bit of the Expansion.
        :param address: index of preferable bit (from 0 to 31)
        :return: Value of the bit (True/False) or None if error occurs.
        :return: None
        '''
        coil = self.client.read_discrete_inputs(address, 1, slave=1)
        if coil.isError():
            logger.error(f'Error reading bit at address {address}: {coil}')
            return None
        return coil.bits[0]

    @Expansion._catcher
    def get_all_bits(self) -> Union[List[bool], None]:
        '''
        Reads information from all the Expansion.
        :return: List of all bits' values or None if error occurs.
        '''
        coils = self.client.read_discrete_inputs(0, count=32, slave=1)
        if coils.isError():
            logger.error(f'Error reading all bits: {coils}')
            return None
        return coils.bits

class OutputExpansion(Expansion):
    '''
    This subclass inherits from the Expansion class and specializes in operations applied to output Expansions.
    The class methods enable reading and writing to relays individually, in groups, or all together.
    '''

    @Expansion._catcher
    def __init__(self, *args, **kwargs):
        super(OutputExpansion, self).__init__(*args, **kwargs)
        self.type = 'output'
        logger.info(f'OUTPUT Expansion with IP {self.IP}')

    @Expansion._catcher
    def get_bit(self, address: int) -> Union[bool, None]:
        '''
        Reads information from a specific bit of the Expansion.
        :param address: index of preferable bit (from 0 to 31)
        :return: Value of the bit (True/False) or None if error occurs.
        '''
        coil = self.client.read_coils(address, 1, slave=1)
        if coil.isError():
            logger.error(f'Error reading bit at address {address}: {coil}')
            return None
        return coil.bits[0]

    @Expansion._catcher
    def get_all_bits(self) -> Union[list[bool], None]:
        '''
        Reads information from all the Expansion.
        :return: List of all bits' values or None if error occurs.
        '''
        coils = self.client.read_coils(0, count=32, slave=1)
        if coils.isError():
            logger.error(f'Error reading all bits: {coils}')
            return None
        return coils.bits

    @Expansion._catcher
    def set_bit(self, address: int, bit: bool) -> bool:
        '''
        Writes information to a specific bit of the Expansion.
        :param address: index of preferable bit (from 0 to 31)
        :param bit: The status to assign
        :return: True if write is successful, False otherwise.
        '''
        coil = self.client.write_coil(address, bit, slave=1)
        if coil.isError():
            logger.error(f'Error setting bit at address {address} to {bit}: {coil}')
            return False
        return True

    @Expansion._catcher
    def set_all_bits(self, bit: bool) -> bool:
        '''
        Sets all bits of the Expansion to the specified value.
        :param bit: the state to assign
        :return: True if write is successful, False otherwise.
        '''
        results = [self.client.write_coil(ad, bit, slave=1) for ad in range(0, 32)]
        if any(result.isError() for result in results):
            logger.error(f'Error setting all bits to {bit}')
            return False
        return True

class PromptReader:
    '''
    The PromptReader class is responsible for interpreting and executing commands
    (read/write) based on provided prompts. It interacts with different Expansion
    objects (input and output) to perform the specified operations.
    '''

    def __init__(self, **kwargs):
        self.expansions = kwargs #KAYWORDS HAVE TO BE THE SAME AS IN the CONFIG
        self.config = load_config()
        self.result = []

    @Expansion._catcher
    def __get_expansion(self,name: str) -> Expansion:
        '''
        Retrieves the Expansion object by name.
        :param name: Name of the Expansion object.
        :return: Expansion object.
        '''
        return self.expansions[name]

    @Expansion._catcher
    def __unfolder(self, function: Callable[[str, int], None]) -> None:
        '''
        Recursively processes a nested dictionary structure to execute a given function.
        :param function: The function to be executed on each relevant key-value pair.
        '''

        def iterator(chunk: dict):
            for k, v in chunk.items():
                # folder self.to_process
                if k in ['EXP', 'PIN']:
                    function(chunk.EXP, chunk.PIN)
                    return self
                else:
                    iterator(chunk[k])
        iterator(self.to_process)

    @Expansion._catcher
    def __empty_writer(self, exp: str, pin: int) -> None:
        '''
        Writes a True value to a specified bit of an Expansion.

        :param exp: The name of the Expansion.
        :param pin: The pin number to write to.
        '''
        self.__get_expansion(exp).set_bit(pin, True)

    @Expansion._catcher
    def __empty_reader(self, exp: str, pin: int) -> None:
        '''
        Reads the value of a specified bit of an Expansion and stores it in the result list.

        :param exp: The name of the Expansion.
        :param pin: The pin number to read from.
        '''
        self.result.append(self.__get_expansion(exp).get_bit(pin))
    @Expansion._catcher
    def writer(self, time_: int) -> None:
        '''
        Continuously writes to Expansions for a specified duration given in prompt.

        :param time_: The duration for which writing operations should be performed.
        '''
        start_p = time.time()
        end_p = time.time()
        while (end_p - start_p) < time_:
            self.__unfolder(self.__empty_writer)
            end_p = time.time()

    @Expansion._catcher
    def reader(self) -> List[bool]:
        '''
        Reads values from Expansions and stores the results.

        :return: A list of boolean values read from the Expansions.
        '''
        self.result = []
        self.__unfolder(self.__empty_reader)
        return self.result


    @Expansion._catcher
    def read_prompt(self, prompt: str):
        '''
        Parses a prompt string and executes the corresponding read or write operation.

        :param prompt: The command string specifying the action and parameters.
        :return: The result of the read operation or None for write operations.
        '''
        logger.debug('Prompt {}'.format(prompt))
        split = prompt.split()
        action = split[0]
        t = split[-1]
        k = lambda s: s[2:] if not s[1]==s[-1] else None
        if t.isdigit():
            t = int(t)
            split = split[:-1]
        else:
            t = 1
        self.device = split[1:]
        self.to_process = get_from_dict(self.config.DEVICES, self.device)
        if action.lower() == 'read':
            result = self.reader()
            logger.info(f'Read result: {result}')
            return result
        else:
            self.writer(t)
            logger.info('Writing done')
            return None













