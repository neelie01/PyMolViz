import numpy as np
import logging
from .RegularData import RegularData
from .ColorRamp import ColorRamp
from ..Displayable import Displayable
from ..util.colors import _convert_string_color


class IsoSurface(Displayable):
    def __init__(self, regular_data : RegularData, level: float, name = None, color = None, transparancy = 0, selection = None, carve = None, side = 1, in_sigma = False):
        """ 
        Computes and collects pymol commands to load in regular data and display an iso mesh at the given level.
        Note that, since this is based on volumetric data it is different from the pmv.Mesh class.

        Args:
            regular_data (pymolviz.RegularData): Regular data for which to show the isomesh.
            level (float): The level at which to display the isomesh.
            name (str, optional): The name of the mesh as displayed in PyMOL. Defaults to {regular_data.name}_{value_label}_IsoMesh_{i}.
            value_label (str, optional): The name of the value to use from the regular data. Defaults to None. Must be passed if regular_data has multiple values.
            color (str or rgb or pymolviz.ColorRamp, optional): The name of the color to use or rgb values or a pymolviz ColorRamp which will be used to color based on position. Defaults to white. 
            transparancy (float): Transparancy of the surface, defaults to 1.
            selection (str, optional): The selection to use. Defaults to None.
            carve (float, optional): The carve to use. Defaults to None.
            side (int, optional): The side of the isosurface to show. Defaults to 1 (outside/gradient facing).
            in_sigma (bool, optional): Whether the level is in sigma. Defaults to False.
        """
        
        self.side = side
        self.transparancy = transparancy
        self.regular_data = regular_data

        if in_sigma:
            self.level = level
        else:
            self.level = level / np.std(self.regular_data.values)

        color = [1, 1, 1] if color is None else color
        if isinstance(color, str):
            self.color = _convert_string_color(color)
        else:
            self.color = color

        self.selection = selection
        self.carve = carve

        if issubclass(type(self.color), ColorRamp):
            dependencies = [self.regular_data, self.color]
        else:   
            dependencies = [self.regular_data]
        super().__init__(name = name, dependencies = dependencies)

    def _script_string(self):
        """ Creates a pymol script to create an isomesh representation of the given regular data.
        
        Returns:
            str: The script.
        """

        optional_arguments = []
        if not(self.selection is None):
            optional_arguments.append(f"selection = \"{self.selection}\"")
        if self.carve is not None:
            optional_arguments.append(f"carve = {self.carve}")

        if issubclass(type(self.color), ColorRamp):
            color_string = f'cmd.color("{self.color.name}", "{self.name}")'
        else:
            color_string = f'''cmd.set_color("{self.name}_color", {self.color})
cmd.color("{self.name}_color", "{self.name}")
'''

        
        result = f"""
cmd.isosurface("{self.name}", "{self.regular_data.name}", {self.level}, {" , ".join(optional_arguments)}{"," if len(optional_arguments) > 0 else ""} side = {self.side})
{color_string}
cmd.set("transparency", {self.transparancy}, "{self.name}")
        """
        
        return result
