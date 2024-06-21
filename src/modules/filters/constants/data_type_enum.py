from enum import Enum


class DataType(Enum):
    STRING = 0
    NUMERIC = 1

    @staticmethod
    def valueOf(data_type_str):
        if data_type_str in ["String", "Boolean"]:
            return DataType.STRING
        elif data_type_str in ["Integer", "Datetime", "Date"]:
            return DataType.NUMERIC
        else:
            raise ValueError(f"Unknown data type: {data_type_str}")
