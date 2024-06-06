from typing import *  # type: ignore

import rio.components.component_tree

from . import component_details


class TreePage(rio.Component):
    _selected_component_id: int | None = None

    def _on_select_component(self, component_id: int) -> None:
        self._selected_component_id = component_id

    def build(self) -> rio.Component:
        margin = 1

        column = rio.Column(
            rio.Text(
                "Component Tree",
                style="heading2",
                margin=margin,
                justify="left",
            ),
            rio.Container(
                rio.components.component_tree.ComponentTree(
                    width=10,
                    height=10,
                    margin_left=margin,
                    on_select_component=self._on_select_component,
                ),
                height="grow",
            ),
            height="grow",
        )

        if self._selected_component_id is not None:
            column.add(
                component_details.ComponentDetails(
                    component_id=self._selected_component_id,
                    margin=margin,
                )
            )

        return column
