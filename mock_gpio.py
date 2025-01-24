class MockGPIO:
    BOARD = "BOARD"
    OUT = "OUT"
    IN = "IN"
    PUD_UP = "PUD_UP"
    LOW = 0
    HIGH = 1
    warnings_disabled = False

    @staticmethod
    def setwarnings(flag):
        MockGPIO.warnings_disabled = flag

    @staticmethod
    def setmode(mode):
        print(f"GPIO mode set to {mode}")

    @staticmethod
    def setup(pin, mode, pull_up_down=None):
        print(f"Pin {pin} set to mode {mode} with pull_up_down={pull_up_down}")

    @staticmethod
    def output(pin, state):
        print(f"Output {state} to pin {pin}")

    @staticmethod
    def input(pin):
        print(f"Reading from pin {pin}")
        # 返回模拟的输入值，可以根据你的需求返回 0 或 1
        return 0

    @staticmethod
    def cleanup():
        print("Cleaning up GPIO")
