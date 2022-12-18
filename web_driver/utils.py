class Utils:
    @classmethod
    def extract_number(self, input_str: str) -> float:
        return float(
            "".join(char for char in input_str if char.isdigit() or char == ".")
        )
