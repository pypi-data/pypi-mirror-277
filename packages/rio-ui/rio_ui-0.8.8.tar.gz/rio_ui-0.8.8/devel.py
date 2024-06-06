import rio
import rio.components.layout_display
import asyncio
import sys
from typing import Any
import uniserde


class RootComponent(rio.Component):
    def on_change(self, new_component_id) -> None:
        print("Changed", new_component_id)

    def build(self) -> rio.Component:
        target = rio.Row(
            rio.Text("Hey There"),
            rio.Button("Click Me"),
            spacing=3,
            margin_left=5,
            margin_top=2,
            height=10,
            # align_x=0.5,
            # align_y=0.5,
        )

        return rio.Column(
            target,
            # rio.components.layout_display.LayoutDisplay(
            #     component_id=target._id,
            #     on_component_change=self.on_change,
            #     width=60,
            #     height=40,
            #     align_x=0.5,
            #     align_y=0.5,
            # ),
        )


app = rio.App(
    build=RootComponent,
    default_attachments=[],
)
