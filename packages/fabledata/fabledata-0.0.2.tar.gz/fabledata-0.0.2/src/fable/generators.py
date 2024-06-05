from abc import ABC, abstractmethod
import logging
import random
from typing import List

import faker


class AbstractBaseGenerator(ABC):
    @property
    @abstractmethod
    def required_params():
        """This should be a dictionary defining the param name and expected data type

        Example: {"name": str, "age": int}

        Validation methods can parse this and compare the input params and their types
        to ensure whatever values have been passed to the `generate()` method can
        actually be used to generate values
        """

    @classmethod
    @abstractmethod
    def generate():
        pass

    @classmethod
    @abstractmethod
    def _generate_value():
        pass


class NumericGenerator(AbstractBaseGenerator):
    required_params = {"lower_bound": int, "upper_bound": int}

    @classmethod
    def generate(cls, row_count: int, params) -> List[int]:
        cls._validate_params(params)
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value(params))
        return values

    @classmethod
    def _generate_value(cls, params) -> int:
        if isinstance(params.get("distribution"), str):
            distribution = params.get("distribution").lower()
            if distribution == "normal":
                return round(random.normalvariate(5000, 1))
        return random.randint(params["lower_bound"], params["upper_bound"])

    @classmethod
    def _validate_params(cls, params) -> bool:
        """Parameter validation for this generator is based on the existence and value of the `distribution` parameter."""
        # TODO: Update validation to look at `distribution` param.
        # If it doesn't exist, default to uniform distribution. Require `lower_bound` and `upper_bound`
        # If it does exist, require params based on distribution type
        # These params get passed in to the FieldConfig when defining a new field
        for k, v in params.items():
            if k not in cls.required_params:
                logging.warning(
                    f"Found '{k}' in params, but it is not expected for this generator"
                )
                continue
            if not isinstance(v, cls.required_params[k]):
                # TODO: Can we attempt to coerce params to the expected datatype?
                raise TypeError(
                    f"Expected '{k}' to be of type {cls.required_params[k]}, but got {v.__class__}"
                )


class StringGenerator(AbstractBaseGenerator):
    @classmethod
    def generate(cls, row_count: int, params) -> List[str]:
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value())
        return values

    @classmethod
    def _generate_value(cls):
        return faker.Faker(use_weighting=False).name()

    @classmethod
    def _validate_params(cls):
        pass


class DateGenerator(AbstractBaseGenerator):
    @classmethod
    def generate(cls, row_count: int, params) -> List[str]:
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value())
        return values

    @classmethod
    def _generate_value(cls):
        return faker.Faker(use_weighting=False).date()

    @classmethod
    def _validate_params(cls):
        pass
