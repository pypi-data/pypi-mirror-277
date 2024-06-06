from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregate_row import AggregateRow
    from ..models.sql_column import SqlColumn


T = TypeVar("T", bound="SqlResult")


@attr.s(auto_attribs=True)
class SqlResult:
    """
    Attributes:
        rows (List[Any]):
        columns (List['SqlColumn']):
        row_count (float):
        sql_text (str):
        aggregates (Union[Unset, List['AggregateRow']]):
        aggregate_sql_text (Union[Unset, str]):
        unit (Union[Unset, str]):
    """

    rows: List[Any]
    columns: List["SqlColumn"]
    row_count: float
    sql_text: str
    aggregates: Union[Unset, List["AggregateRow"]] = UNSET
    aggregate_sql_text: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = self.rows

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        row_count = self.row_count
        sql_text = self.sql_text
        aggregates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aggregates, Unset):
            aggregates = []
            for aggregates_item_data in self.aggregates:
                aggregates_item = aggregates_item_data.to_dict()

                aggregates.append(aggregates_item)

        aggregate_sql_text = self.aggregate_sql_text
        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "columns": columns,
                "rowCount": row_count,
                "sqlText": sql_text,
            }
        )
        if aggregates is not UNSET:
            field_dict["aggregates"] = aggregates
        if aggregate_sql_text is not UNSET:
            field_dict["aggregateSqlText"] = aggregate_sql_text
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregate_row import AggregateRow
        from ..models.sql_column import SqlColumn

        d = src_dict.copy()
        rows = cast(List[Any], d.pop("rows"))

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = SqlColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        row_count = d.pop("rowCount")

        sql_text = d.pop("sqlText")

        aggregates = []
        _aggregates = d.pop("aggregates", UNSET)
        for aggregates_item_data in _aggregates or []:
            aggregates_item = AggregateRow.from_dict(aggregates_item_data)

            aggregates.append(aggregates_item)

        aggregate_sql_text = d.pop("aggregateSqlText", UNSET)

        unit = d.pop("unit", UNSET)

        sql_result = cls(
            rows=rows,
            columns=columns,
            row_count=row_count,
            sql_text=sql_text,
            aggregates=aggregates,
            aggregate_sql_text=aggregate_sql_text,
            unit=unit,
        )

        sql_result.additional_properties = d
        return sql_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
