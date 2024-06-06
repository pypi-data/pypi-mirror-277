from aenum import Enum

from atscale.errors import atscale_errors


class TimeSteps(Enum):
    """Translates the time levels into usable step sizes."""

    def __new__(
        cls,
        value,
        steps,
    ):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.steps = steps
        return obj

    Regular = 0, [0]
    TimeYears = 20, [1, 2]
    TimeHalfYears = 36, [1, 2]
    TimeTrimester = 4722, [1, 3]
    TimeQuarters = 68, [1, 4]
    TimeMonths = 132, [1, 3, 6, 12]
    TimeWeeks = 260, [1, 4]
    TimeDays = 516, [1, 7, 28]
    TimeHours = 772, [1, 12, 24]
    TimeMinutes = 1028, [1, 60]
    TimeSeconds = 2052, [1, 60]
    TimeUndefined = 4100, [0]

    def get_steps(self):
        if self.name == "Regular" or self.name == "TimeUndefined":
            return None
        else:
            return self.steps


class Aggs(Enum):
    """Holds constant string representations for the supported aggregation methods of numerical aggregate features
    SUM: Addition
    AVG: Average
    MAX: Maximum
    MIN: Mininum
    DISTINCT_COUNT: Distinct-Count (count of unique values)
    DISTINCT_COUNT_ESTIMATE: An estimate of the distinct count to save compute
    NON_DISTINCT_COUNT: Count of all values
    STDDEV_SAMP: standard deviation of the sample
    STDDEV_POP: population standard deviation
    VAR_SAMP: sample variance
    VAR_POP: population variance
    """

    def __new__(cls, key_name, visual_rep):
        obj = object.__new__(cls)
        obj._value_ = key_name
        obj._customer_representation = visual_rep
        return obj

    SUM = "SUM", "Sum"
    AVG = "AVG", "Average"
    MAX = "MAX", "Max"
    MIN = "MIN", "Min"
    DISTINCT_COUNT = "DC", "Distinct Count"
    DISTINCT_COUNT_ESTIMATE = "DCE", "Distinct Count Estimate"
    NON_DISTINCT_COUNT = "NDC", "Non Distinct Count"
    STDDEV_SAMP = "STDDEV_SAMP", "Sample Standard Deviation"
    STDDEV_POP = "STDDEV_POP", "Population Standard Deviation"
    VAR_SAMP = "VAR_SAMP", "Sample Variance"
    VAR_POP = "VAR_POP", "Population Variance"

    @property
    def visual_rep(self):
        return self._customer_representation

    # UNUSED UNTIL THE DMV BUG IS SORTED
    # @classmethod
    # def from_properties(cls, property_dict):
    #     if property_dict is None:
    #         return ""
    #     type_section = property_dict.get("type", {})
    #     if "measure" in type_section:
    #         return cls[type_section["measure"]["default-aggregation"]]
    #     elif "count-distinct" in type_section:
    #         if type_section["count-distinct"]["approximate"]:
    #             return cls.DISTINCT_COUNT_ESTIMATE
    #         else:
    #             return cls.DISTINCT_COUNT
    #     elif "count-nonnull":
    #         return cls.NON_DISTINCT_COUNT

    @classmethod
    def from_dmv_number(cls, number):
        num_to_value = {
            1: cls.SUM,
            5: cls.AVG,
            4: cls.MAX,
            3: cls.MIN,
            8: cls.DISTINCT_COUNT,
            1000: cls.DISTINCT_COUNT_ESTIMATE,  # dmv bug, comes back as 8
            2: cls.NON_DISTINCT_COUNT,
            7: cls.STDDEV_SAMP,
            333: cls.STDDEV_POP,  # dmv bug, comes back as 0
            0: cls.VAR_POP,
            6: cls.VAR_SAMP,
        }
        obj = num_to_value[number]
        return obj

    def requires_key_ref(self):
        return self in [
            self.__class__.DISTINCT_COUNT,
            self.__class__.DISTINCT_COUNT_ESTIMATE,
            self.__class__.NON_DISTINCT_COUNT,
        ]

    def get_dict_expression(
        self,
        key_ref,
    ):
        if self.requires_key_ref() and key_ref is None:
            raise atscale_errors.ModelingError(
                f"A key-ref id must be made and passed into this function in order to make a valid "
                f"{self.name} measure dict."
            )
        if self.name == "DISTINCT_COUNT":
            return {"count-distinct": {"key-ref": {"id": key_ref}, "approximate": False}}
        elif self.name == "DISTINCT_COUNT_ESTIMATE":
            return {"count-distinct": {"key-ref": {"id": key_ref}, "approximate": True}}
        elif self.name == "NON_DISTINCT_COUNT":
            return {"count-nonnull": {"key-ref": {"id": key_ref}, "approximate": False}}
        else:
            return {"measure": {"default-aggregation": self.value}}


class MDXAggs(Enum):
    """Holds constant string representations for the supported MDX aggregation methods
    SUM: Addition
    STANDARD_DEVIATION: standard deviation of the sample
    MEAN: Average
    MAX: Maximum
    MIN: Mininum
    """

    SUM = "Sum"
    STANDARD_DEVIATION = "Stdev"
    MEAN = "Avg"
    MAX = "Max"
    MIN = "Min"


class TableExistsAction(Enum):
    """Potential actions to take if a table already exists when trying to write a dataframe to that database table.
    APPEND: Append content of the dataframe to existing data or table
    OVERWRITE: Overwrite existing data with the content of dataframe
    IGNORE: Ignore current write operation if data/ table already exists without any error. This is not valid for pandas dataframes
    ERROR: Throw an exception if data or table already exists
    """

    def __new__(cls, value, pandas_value):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.pandas_value = pandas_value
        return obj

    APPEND = "append", "append"
    OVERWRITE = "overwrite", "replace"
    IGNORE = "ignore", None
    ERROR = "error", "fail"


class FeatureFormattingType(Enum):
    """How the value of a feature gets formatted before output"""

    GENERAL_NUMBER = "General Number"
    STANDARD = "Standard"
    SCIENTIFIC = "Scientific"
    FIXED = "Fixed"
    PERCENT = "Percent"


class FeatureType(Enum):
    """Used for specifying all features or only numerics or only categorical"""

    def __new__(
        cls,
        value,
        name_val,
    ):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.name_val = name_val
        return obj

    ALL = (0, "All")
    NUMERIC = (1, "Numeric")
    CATEGORICAL = (2, "Categorical")


class MappedColumnFieldTerminator(Enum):
    """Used for specifying mapped column field delimiters"""

    comma = ","
    semicolon = ";"
    pipe = "|"


class MappedColumnKeyTerminator(Enum):
    """Used for specifying mapped column key delimiters"""

    equals = "="
    colon = ":"
    caret = "^"


class MappedColumnDataTypes(Enum):
    """Used for specifying data type of mapped column"""

    Int = "Int"
    Long = "Long"
    Boolean = "Boolean"
    String = "String"
    Float = "Float"
    Double = "Double"
    Decimal = "Decimal"
    Datetime = "DateTime"
    Date = "Date"
