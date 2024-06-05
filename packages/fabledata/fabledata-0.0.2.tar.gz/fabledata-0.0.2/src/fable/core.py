from typing import List

import polars as pl
from .models import FieldConfig, FieldMetadata, TableConfig

# TODO: Find a better place for polars configs?
pl.Config.set_tbl_hide_dataframe_shape(True)
pl.Config.set_tbl_hide_column_data_types(True)


class Field:
    """ """

    def __init__(self, config: FieldConfig):
        self.name = config.name
        self.dtype = config.dtype
        self.generator = config.generator

        self.params = config.model_extra

        # TODO: Better type hint
        self.values: List[self.generator.return_type] = []
        self.table: Table = None

    def __str__(self):
        return f"{str(self.__class__)} : {str(self.__dict__)}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.name, self.generator, self.table) == (
                other.name,
                other.generator,
                other.table,
            )
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def populate(self, row_count: int):
        """Populate this field"""
        self.values = self.generator.generate(row_count, self.params)


class Table:
    """ """

    def __init__(self, config: TableConfig):
        self.name = config.name
        self.row_count = config.row_count

        self.field_map: dict[str, FieldMetadata] = {}
        self.fields: List[Field] = []
        self.data: pl.DataFrame = None

    def __str__(self):
        return f"{str(self.__class__)} : {str(self.__dict__)}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def head(self, rows: int = 10):
        if self.data is None:
            raise Exception("Table has not been populated")
        return self.data.head(rows)

    def add_field(self, field: Field):
        if field.name not in self.field_map:
            self.field_map[field.name] = FieldMetadata(
                dtype=field.dtype, position=1 + len(self.fields)
            )
            self.fields.append(field)
            field.table = self
        else:
            raise Exception(f"Duplicate field: {field.name}")

    def add_fields(self, fields: List[Field]):
        for field in fields:
            self.add_field(field)

    def remove_field(self, field_name: str):
        position = self.field_map[field_name].position
        self.fields.pop(position - 1)
        del self.field_map[field_name]
        # Field map entry position needs to update when fields are removed
        for _, value in self.field_map.items():
            if value.position > position:
                value.position -= 1

    def populate(self):
        """Populate the fields associated with this table"""
        if self.data is not None:
            raise Exception("This table has already been populated")

        for field in self.fields:
            field.populate(self.row_count)

        self.data = pl.DataFrame({field.name: field.values for field in self.fields})

    def truncate(self):
        """This method keeps the structure of the table in place, but removes the data
        from each row in the `data` instance attribute using the pl.Dataframe.clear() method

        Note that it is different than the `clear()` method of this class
        """
        self.data.clear()

    def clear(self):
        """Completely resets the table to an empty state. The `data` attribute is reset to its
        default fo None, the `fields` attribute is reset to its default of an empty list, and
        the `field_map` attribute is reset to its default of an empty dictionary.

        Note that this is different than the `clear()` method of a Polars DataFrame
        """
        self.data = None
        self.fields = []
        self.field_map = {}

    def link(self, field: Field, linking_table, linking_field: Field):
        if not isinstance(linking_table, self.__class__):
            raise ValueError(
                f"Received table of type {linking_table.__class__}. Must pass a Table to linking_table"
            )

        if linking_table == self:
            raise Exception("Link must be set between two different tables")

        if not all(isinstance(field, Field), isinstance(linking_field, Field)):
            raise Exception("Fields can only be linked with other Fields")

        # TODO: Update field_map in each table with link information.
        # Or maybe a separate `link` map on each object?

    def to_csv(self, outfile: str, **kwargs):
        """Export table as a csv file.
        Any valid pl.Dataframe.write_csv params can be passed as kwargs"""
        if self.data is not None:
            self.data.write_csv(file=outfile, **kwargs)
        else:
            raise Exception("Failed to write empty table to csv")
