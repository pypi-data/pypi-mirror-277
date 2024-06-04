from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ...fable_modules.fable_library.array_ import map as map_2
from ...fable_modules.fable_library.list import (map, FSharpList, item, of_array, singleton as singleton_1)
from ...fable_modules.fable_library.range import range_big_int
from ...fable_modules.fable_library.seq import (to_array, delay, map as map_1, to_list, append, singleton, exists, empty)
from ...fable_modules.fable_library.types import Array
from ...fable_modules.fable_library.util import IEnumerable_1
from ...fable_modules.fs_spreadsheet.Cells.fs_cell import FsCell
from ...fable_modules.fs_spreadsheet.fs_address import FsAddress__get_RowNumber
from ...fable_modules.fs_spreadsheet.fs_column import FsColumn
from ...fable_modules.fs_spreadsheet.Ranges.fs_range_address import FsRangeAddress__get_LastAddress
from ...fable_modules.fs_spreadsheet.Ranges.fs_range_base import FsRangeBase__get_RangeAddress
from ...Core.Table.composite_cell import CompositeCell
from ...Core.Table.composite_column import CompositeColumn
from ...Core.Table.composite_header import CompositeHeader
from ..AnnotationTable.composite_cell import to_fs_cells as to_fs_cells_1
from .data_map_header import (from_fs_cells, to_fs_cells)

def from_fs_columns(columns: FSharpList[FsColumn]) -> CompositeColumn:
    def mapping(c: FsColumn, columns: Any=columns) -> FsCell:
        return c.Item(1)

    pattern_input: tuple[CompositeHeader, Callable[[FSharpList[FsCell]], CompositeCell]] = from_fs_cells(map(mapping, columns))
    l: int = FsAddress__get_RowNumber(FsRangeAddress__get_LastAddress(FsRangeBase__get_RangeAddress(item(0, columns)))) or 0
    def _arrow954(__unit: None=None, columns: Any=columns) -> IEnumerable_1[CompositeCell]:
        def _arrow953(i: int) -> CompositeCell:
            def mapping_1(c_1: FsColumn) -> FsCell:
                return c_1.Item(i)

            return pattern_input[1](map(mapping_1, columns))

        return map_1(_arrow953, range_big_int(2, 1, l))

    cells_1: Array[CompositeCell] = to_array(delay(_arrow954))
    return CompositeColumn.create(pattern_input[0], cells_1)


def to_fs_columns(column: CompositeColumn) -> FSharpList[FSharpList[FsCell]]:
    is_term: bool = column.Header.IsTermColumn
    is_data: bool = column.Header.IsDataColumn
    header: FSharpList[FsCell] = to_fs_cells(column.Header)
    def mapping(cell: CompositeCell, column: Any=column) -> FSharpList[FsCell]:
        return to_fs_cells_1(is_term, False, cell)

    cells: Array[FSharpList[FsCell]] = map_2(mapping, column.Cells, None)
    if is_term:
        def _arrow960(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow959(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow958(i: int) -> FsCell:
                    return item(0, cells[i])

                return map_1(_arrow958, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(0, header)), delay(_arrow959))

        def _arrow963(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow962(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow961(i_1: int) -> FsCell:
                    return item(1, cells[i_1])

                return map_1(_arrow961, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(1, header)), delay(_arrow962))

        def _arrow966(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow965(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow964(i_2: int) -> FsCell:
                    return item(2, cells[i_2])

                return map_1(_arrow964, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(2, header)), delay(_arrow965))

        return of_array([to_list(delay(_arrow960)), to_list(delay(_arrow963)), to_list(delay(_arrow966))])

    elif is_data:
        def predicate(c: CompositeCell, column: Any=column) -> bool:
            return c.AsData.Format is not None

        has_format: bool = exists(predicate, column.Cells)
        def predicate_1(c_1: CompositeCell, column: Any=column) -> bool:
            return c_1.AsData.SelectorFormat is not None

        has_selector_format: bool = exists(predicate_1, column.Cells)
        def _arrow978(__unit: None=None, column: Any=column) -> IEnumerable_1[FSharpList[FsCell]]:
            def _arrow969(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow968(__unit: None=None) -> IEnumerable_1[FsCell]:
                    def _arrow967(i_3: int) -> FsCell:
                        return item(0, cells[i_3])

                    return map_1(_arrow967, range_big_int(0, 1, len(column.Cells) - 1))

                return append(singleton(item(0, header)), delay(_arrow968))

            def _arrow977(__unit: None=None) -> IEnumerable_1[FSharpList[FsCell]]:
                def _arrow972(__unit: None=None) -> IEnumerable_1[FsCell]:
                    def _arrow971(__unit: None=None) -> IEnumerable_1[FsCell]:
                        def _arrow970(i_4: int) -> FsCell:
                            return item(1, cells[i_4])

                        return map_1(_arrow970, range_big_int(0, 1, len(column.Cells) - 1))

                    return append(singleton(item(1, header)), delay(_arrow971))

                def _arrow976(__unit: None=None) -> IEnumerable_1[FSharpList[FsCell]]:
                    def _arrow975(__unit: None=None) -> IEnumerable_1[FsCell]:
                        def _arrow974(__unit: None=None) -> IEnumerable_1[FsCell]:
                            def _arrow973(i_5: int) -> FsCell:
                                return item(2, cells[i_5])

                            return map_1(_arrow973, range_big_int(0, 1, len(column.Cells) - 1))

                        return append(singleton(item(2, header)), delay(_arrow974))

                    return singleton(to_list(delay(_arrow975))) if has_selector_format else empty()

                return append(singleton(to_list(delay(_arrow972))) if has_format else empty(), delay(_arrow976))

            return append(singleton(to_list(delay(_arrow969))), delay(_arrow977))

        return to_list(delay(_arrow978))

    else: 
        def _arrow981(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow980(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow979(i_6: int) -> FsCell:
                    return item(0, cells[i_6])

                return map_1(_arrow979, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(0, header)), delay(_arrow980))

        return singleton_1(to_list(delay(_arrow981)))



__all__ = ["from_fs_columns", "to_fs_columns"]

