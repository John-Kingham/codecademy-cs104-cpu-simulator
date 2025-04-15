"""
Codecademy Computer Science Career Path
CPU Simulator Project
"""


class CPUSimulator:
    """
    The top-level object in the CPU Simulator system.
    The controller in the model-view-controller architecture.
    """

    def __init__(self) -> None:
        """
        Requires:
            Nothing.
        Guarantees:
            The system start up objects have been created.
            The simulation has not started.
        """
        self.cpu: CentralProcessingUnit

        print("Constructing CPUSimulator")
        self.cpu = CentralProcessingUnit()

    def run(self) -> None:
        """
        Requires:
            That the external instruction and data files exist.
        Guarantees:
            That the CPU simulation has run and ended.
        """
        self.cpu.run()


class CentralProcessingUnit:
    """
    This class is a simplified model of the physical structure of a CPU.
    It contains an arithmetic logic unit, a control unit and a connection to
    the memory bus.
    """

    def __init__(self) -> None:
        """
        Requires:
            That the instruction and data files exist.
        Guarantees:
            That the CPU has been created and is ready to start the machine
            cycle.
        """
        self.alu: ArithmeticLogicUnit
        self.memory_bus: MemoryBus
        self.control_unit: ControlUnit

        print("Constructing CPU")
        self.alu = ArithmeticLogicUnit()
        self.memory_bus = MemoryBus()
        self.control_unit = ControlUnit(self.alu, self.memory_bus)

    def run(self) -> None:
        """
        Requires:
            The external instruction and data files exist.
        Guarantees:
            The machine cycle was started, executed instructions and ended.
        """
        self.control_unit.run_machine_cycle()


class ArithmeticLogicUnit:
    """
    The ALU carries out arithmetic and logical operations for the control unit.
    These are bitwise operations that work at the level of individual bits.
    """

    def __init__(self) -> None:
        print("Constructing ALU")


class MemoryBus:
    """
    The memory bus gives the CPU access to data and instructions
    stored outside the CPU.
    """

    def __init__(self) -> None:
        """
        Requires:
            The instruction and data files exist.
        Guarantees:
            The memory bus has been created in an empty state.
        """
        print("Constructing Memory Bus")
        self.instruction_file_name: str
        self.data_file_name: str
        self.memory_cells: list[str]

        self.instruction_file_name = "instructions.txt"
        self.data_file_name = "data.txt"
        self.memory_cells = ["BOOT"] + ([""] * 31)

    def load(self, address: int) -> str:
        """
        Requires:
            A valid memory cell address.
        Returns:
            The contents of the memory cell at the address.
        """
        # TODO - To be implemented
        return ""


class ControlUnit:
    """
    This is the core of the CPU. It runs the machine cycle, which
    fetches, decodes and executes machine instructions in a recurring loop.
    """

    def __init__(self, alu: ArithmeticLogicUnit, memory_bus: MemoryBus) -> None:
        """
        Requires:
            The CPU's ALU and memory bus.
        Guarantees:
            The control unit is ready to begin the machine cycle.
        """
        print("Constructing control unit")
        # The program counter contains the memory cell address of the
        # next instruction to be fetched.
        self.program_counter: int
        # The instruction register contains the instruction to be / being
        # executed.
        self.instruction_reg: str
        # General registers are memory cells within the CPU, giving it rapid
        # access to small amounts of data required to execute an instruction.
        self.general_regs: list[str]
        # The cycle register is a one-bit register. If it is set to 1,
        # the machine cycle will run; if it's 0, the machine cycle will stop.
        self.cycle_register: bool
        self.alu: ArithmeticLogicUnit
        self.memory: MemoryBus

        self.program_counter = 0
        self.instruction_reg = ""
        self.general_regs = [""] * 8
        self.cycle_register = True
        self.alu = alu
        self.memory = memory_bus

    def run_machine_cycle(self) -> None:
        """
        Starts the machine cycle. The machine cycle continues until
        a HALT instruction or an invalid instruction is found.
        Requires:
            The cycle register is set to 1.
            The instruction and data files exist.
        Guarantees:
            The machine cycle was started, executed instructions and ended.
        """
        while self.cycle_register is True:
            self.instruction_reg = self.memory.load(self.program_counter)
            # TODO - under construction


def main() -> None:
    choice: str
    simulator: CPUSimulator

    # greet the user and ask if they'd like to run the cpu simulation
    print("Welcome to the CPU Simulator.")
    while True:
        choice = input("Do you want to run the simulator (y/n)? ").lower()
        if choice == "y":
            break
        elif choice == "n":
            return
        else:
            print("Invalid choice.")
    simulator = CPUSimulator()


if __name__ == "__main__":
    main()
