import datetime
import os
from collections import OrderedDict
from typing import Optional, Callable, List
import csv

from tkinter import ttk
import tkinter as tk
import tkinter.filedialog

from RoboControl.Com.PacketLogger.LoggedDataPacket import DisplayDataWidth_e, DisplayFormat_e, LoggedDataPacket
from RoboControl.Com.PacketLogger.utils.ratelimit import dropping_ratelimit
from RoboControl.Robot.AbstractRobot.AbstractListener import PacketLoggerListener, ChangeListener
from RoboView.Robot.Ui.utils.colors import Color

Renderer = Callable[[object], str]


class Column:
    EMPTY_VALUE = ""

    def __init__(self, name):
        self.name = name
        self.index = 0

    def render(self, value: object) -> str:
        if value is None:
            return self.EMPTY_VALUE
        return str(value)

    def parse(self, raw_value: object) -> object:
        return raw_value

    def with_index(self, index: int) -> "Column":
        self.index = index
        return self


class NumberColumn(Column):
    def parse(self, raw_value: str) -> int:
        return int(raw_value)


class TimestampColumn(Column):
    def render(self, value: datetime.datetime) -> str:
        if value is None:
            return self.EMPTY_VALUE
        return value.isoformat(sep=' ', timespec='milliseconds')


class PacketColumn(Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data_width = DisplayDataWidth_e.WIDTH_8
        self._data_format = DisplayFormat_e.DECIMAL

    def render(self, data_packet: LoggedDataPacket) -> str:
        if data_packet is None:
            return self.EMPTY_VALUE
        if self._data_format == DisplayFormat_e.DECIMAL:
            return data_packet.get_data_as_string(self._data_width, False)
        elif self._data_format == DisplayFormat_e.DECIMAL:
            return data_packet.get_data_as_string(self._data_width, False)
        elif self._data_format == DisplayFormat_e.HEXADECIMAL:
            return data_packet.get_data_as_string(self._data_width, True)
        elif self._data_format == DisplayFormat_e.NATIVE:
            return data_packet.get_parameters_as_string(False)
        elif self._data_format == DisplayFormat_e.NATIVE_WITH_DESCRIPTION:
            return data_packet.get_parameters_as_string(True)
        return data_packet.get_data_as_string(self._data_width, False)

    def set_data_width(self, data_width: DisplayDataWidth_e) -> None:
        self._data_width = data_width

    def set_data_format(self, data_format: DisplayFormat_e) -> None:
        self._data_format = data_format

    def get_as_raw(self, raw_value: LoggedDataPacket):
        return raw_value.get_data_as_string(self._data_width, False)


class Row:
    ID_COLUMN = "nr"

    def __init__(self, columns: List[Column], values: List[object], tags=None):
        if len(values) != len(columns):
            raise ValueError(f"Column size {len(columns)} doesn't match values size {len(values)}")
        self.cells = OrderedDict()
        for index, value in enumerate(values):
            column = columns[index]
            self.cells[column.name] = Cell(column, value)
        self._columns = None
        self.tags = tags

    def get_cell(self, index: int = None, column_name: str = None) -> Optional["Cell"]:
        if index is None and column_name is None:
            return None
        if index is not None:
            return list(self.cells.values())[index]
        return self.cells.get(column_name)

    def __repr__(self):
        return f"Row({[repr(cell) for cell in self.cells.values()]})"

    def __str__(self):
        return str([str(cell.value) for cell in self.cells.values()])

    def get_id(self) -> str:
        return str(self.get_cell(column_name=self.ID_COLUMN))


class Cell:
    def __init__(self, column, raw_value):
        self.raw_value = raw_value
        self.value = column.parse(self.raw_value)
        self.column = column

    def __repr__(self):
        return f"Cell({self.column.name}={self.value})"

    def __str__(self):
        return self.column.render(self.value)


class TableModel(ChangeListener):
    _max_size = None

    def __init__(self):
        self._columns: List[Column] = []
        self._rows: List[Row] = []

        self.is_recording = False
        self._listeners: list[PacketLoggerListener] = []

    @property
    def column_names(self) -> List[str]:
        return [c.name for c in self._columns]

    @property
    def columns_size(self) -> int:
        return len(self._columns)

    @property
    def rows_size(self) -> int:
        return len(self._rows)

    @property
    def max_size(self) -> int:
        return self._max_size

    @max_size.setter
    def max_size(self, new_max_size: int) -> None:
        self._max_size = 1 if new_max_size < 1 else new_max_size
        while len(self._rows) > self._max_size:
            self._rows.pop(0)
        self.on_change()

    def add_column(self, column: Column) -> "TableModel":
        if self.max_size is not None:
            self._rows.pop(0)
        new_index = self.columns_size
        self._columns.append(column.with_index(new_index))
        return self

    def get_column(self, index: int = None, name: str = None) -> Optional[Column]:
        if index is not None:
            return self._columns[index]
        elif name is not None:
            for column in self._columns:
                if column.name == name:
                    return column
        return None

    def get_row(self, index: int) -> Optional[Row]:
        if index is None:
            return None
        if index < self.rows_size:
            return self._rows[index]
        return None

    def get_cell(self, row_index: int = None, column_index: int = None) -> Optional[Cell]:
        row = self.get_row(index=row_index)
        if row is None:
            return None
        return row.get_cell(index=column_index)

    def add_row(self, values: List[object], tags=None) -> Optional[Row]:
        if not self.is_recording:
            return None
        if self.rows_size >= self.max_size:
            self._rows.pop(0)
        row = Row(self._columns, values)
        if tags:
            row.tags = tags
        self._rows.append(row)
        self.on_change()
        return row

    def clear(self) -> None:
        self._rows = []
        self.on_change()

    def as_treeview(self, master) -> ttk.Treeview:
        table = ttk.Treeview(master=master, columns=self.column_names,
                             selectmode="extended", show="headings", padding=5)

        for column in self.column_names:
            table.column(column, anchor="c", minwidth=100, width=100, stretch=False)
            table.heading(column, text=column)
        table.tag_configure('green', background=Color.LIMEGREEN)
        table.tag_configure('red', background=Color.RED)
        return table

    def save_as(self) -> None:
        file = tk.filedialog.asksaveasfile(
            filetypes=[("CSV files", "*.csv")], defaultextension=".csv",
            initialdir=os.getcwd()
        )
        if file:
            file.close()
            self.dump_csv(file.name)

    def dump_csv(self, filepath: str) -> None:
        with open(filepath, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column_names, delimiter=';')
            writer.writeheader()
            for input_row in self._rows:
                output_row = {}
                for cell in input_row.cells.values():
                    output_row[cell.column.name] = str(cell)
                writer.writerow(output_row)

    def add_listener(self, listener) -> None:
        self._listeners.append(listener)

    def on_change(self) -> None:
        for listener in self._listeners:
            listener.on_change()

    @dropping_ratelimit(seconds=1)
    def paint_on_table(self, table: ttk.Treeview) -> None:
        old_ids = table.get_children()
        new_ids = [row.get_id() for row in self._rows]

        trash = [i for i in old_ids if i not in new_ids]
        table.delete(*trash)

        for row in self._rows:
            row_id = row.get_id()
            if row_id in old_ids:
                continue
            table_row = []
            for column_index in range(self.columns_size):
                cell = row.get_cell(column_index)
                table_row.append(str(cell))
            item = table.insert('', tk.END, row_id, values=table_row, tags=row.tags or "")
            table.see(item)
            # yield
