# Generated file. Do not edit.

import os
from typing import Dict, Tuple, Optional, List, Any

from itkwasm import (
    environment_dispatch,
    Mesh,
)

def sub_mesh(
    mesh: Mesh,
    cell_identifiers: List[int] = [],
) -> Mesh:
    """Extract a subset of a mesh given by the cell identifiers.

    :param mesh: Full mesh
    :type  mesh: Mesh

    :param cell_identifiers: Cell identifiers for output mesh.
    :type  cell_identifiers: int

    :return: Sub mesh.
    :rtype:  Mesh
    """
    func = environment_dispatch("itkwasm_sub_mesh", "sub_mesh")
    output = func(mesh, cell_identifiers=cell_identifiers)
    return output
