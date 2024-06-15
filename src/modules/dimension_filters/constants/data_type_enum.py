from enum import Enum


class DataType(Enum):
    STRING = "String"
    NUMERIC = "Numeric"
    DATE = "Date"
    DATETIME = "DateTime"

    @staticmethod
    def valueOf(data_type_str):
        if data_type_str in ["String", "Boolean"]:
            return DataType.STRING
        elif data_type_str in ["Integer", "Float"]:
            return DataType.NUMERIC
        elif data_type_str == "Date":
            return DataType.DATE
        elif data_type_str == "DateTime":
            return DataType.DATETIME
        else:
            raise ValueError(f"Unknown data type: {data_type_str}")
