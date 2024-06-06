# IT Jim Polishing Robot
API for communicating devices with the main PC
## Description
The [ModulConnector](https://gitlab.ektos.net/dne/jimpolishing/-/blob/main/ModulConnector.py?ref_type=heads) module provides an interface for communication with Modbus expansions. It offers functions for writing to and reading from output nodes, as well as reading from digital inputs. The module can operate on single bits, groups of bits, or all bits of an expansion. Each expansion is initialized by a corresponding class. 

## Features
Connect and disconnect from Modbus expansions.
Read individual bits, groups of bits, or all bits from input expansions.
Write individual bits, groups of bits, or all bits to output expansions.
Execute commands based on prompts through the PromptReader class.

## Installation
To use this module, you need to have Python installed on your system. Additionally, you need to install the required dependencies.

1. Clone the repository:

> `git clone https://github.com/yourusername/ModulConnector.git
> cd ModulConnector`


2. Install the dependencies:


> `pip install -r requirements.txt`


## Configuration
The module uses a configuration file (config.yaml) to define devices and expansions. Below is a schematic representation of the configuration file:

```
DEVICES:
  "DEVICE_IDENTIFIER_1":
    # Expansion this device is connected to (I1, I2, Q1, Q2)
    EXP: EXPANSION_NAME
    # Pin number on the expansion
    PIN: PIN_NUMBER
    
  "DEVICE_IDENTIFIER_2":
    EXP: EXPANSION_NAME
    PIN: PIN_NUMBER
    
  # Continue for all devices
  ...

EXPANSIONS:
  # Expansion identifier (string)
  EXPANSION_NAME:
    # Type of expansion: 'input' or 'output'
    type: EXPANSION_TYPE
    # IP address of the expansion module
    IP: EXPANSION_IP

  # Continue for all expansions
  ...
```
## Usage
Here's an [example script](https://gitlab.ektos.net/dne/jimpolishing/-/blob/main/Example_Devices.py?ref_type=heads) demonstrating how to use the ModulConnector module:

```
from ModulConnector import InputExpansion, OutputExpansion, PromptReader
import time
from utils import load_config

if __name__ == '__main__':
    start = time.time()
    config = load_config()

    I1 = InputExpansion(config['EXPANSIONS']['INPUT_01']['IP'], 502)
    O1 = OutputExpansion(config['EXPANSIONS']['OUTPUT_01']['IP'], 502)

    I1.connect()
    O1.connect()

    prompter = PromptReader(I1=I1, Q1=O1)
    while True:
        prompt = input('Your Prompt ')
        print(prompter.read_prompt(prompt))
      
    I1.disconnect()
    O1.disconnect()
```


Example prompts you can use with the script:

COMMAND DEVICE TIME(OPTIONAL, FOR WRITE)

```
READ 1_CHK_JIG_SPINDLE_01
WRITE MICRO_PUMP 50 
WRITE POLE_GRIPPER ON
READ POLE_GRIPPER
```

## Classes end Methods

![_](https://gitlab.ektos.net/dne/jimpolishing/-/blob/main/ModulConnector.png)
### Expansion Class

A parent class incorporating basic attributes and methods common to all expansions.

- connect(): Connects to the expansion.
- disconnect(): Disconnects from the expansion.

### InputExpansion Class

Inherits from Expansion and specializes in input operations.

- get_bit(address): Reads a specific bit.
- get_all_bits(): Reads all bits.

### OutputExpansion Class

Inherits from Expansion and specializes in output operations.

- get_bit(address): Reads a specific bit.
- get_all_bits(): Reads all bits.
- set_bit(address, bit): Writes to a specific bit.
- set_all_bits(bit): Writes to all bits.

### PromptReader Class

Interprets and executes commands based on prompts.

- read_prompt(prompt): Parses and executes a read or write operation based on the prompt.
- writer(time): Continuously writes to expansions for a specified duration.
- reader(): Reads values from expansions and stores the results.


## Authors and acknowledgment
Based on pymodbus library for Modbus communication.
Utilizes typing_extensions for enhanced type hinting.


## Project status
The project is currently in Phase 2, which focuses on developing an API for communicating with devices from the main PC. This phase builds upon the foundation laid in Phase 1, where a dummy API for I/O devices and the main PC was established.
