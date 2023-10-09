from typing import Optional

from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class AbstractComponentList(list[AbstractComponent]):
    def get_component_on_name(self, name: str) -> Optional[AbstractComponent]:
        """ "search for a component in device with given name" """
        for component in self:
            if component.get_component_name() == name:
                return component
        return None

    def get_component_on_global_id(self, id: int) -> Optional[AbstractComponent]:
        """ "search for a component in device with given globalId" """
        for component in self:
            if component.get_global_id() == id:
                return component
        return None

    def get_data_values(self) -> list[ComponentValue]:
        values = []
        for component in self:
            values += component.get_data_values()
        return values

    def get_control_values(self) -> list[ComponentValue]:
        values = []
        for component in self:
            values += component.get_control_values()
        return values
