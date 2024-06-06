# Generated file. To retain edits, remove this comment.

from pathlib import Path, PurePosixPath
import os
from typing import Dict, Tuple, Optional, List, Any

from importlib_resources import files as file_resources

_pipeline = None

from itkwasm import (
    InterfaceTypes,
    PipelineOutput,
    PipelineInput,
    Pipeline,
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
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline(file_resources('itkwasm_sub_mesh_wasi').joinpath(Path('wasm_modules') / Path('sub-mesh.wasi.wasm')))

    pipeline_outputs: List[PipelineOutput] = [
        PipelineOutput(InterfaceTypes.Mesh),
    ]

    pipeline_inputs: List[PipelineInput] = [
        PipelineInput(InterfaceTypes.Mesh, mesh),
    ]

    args: List[str] = ['--memory-io',]
    # Inputs
    args.append('0')
    # Outputs
    sub_mesh_name = '0'
    args.append(sub_mesh_name)

    # Options
    input_count = len(pipeline_inputs)
    if len(cell_identifiers) < 1:
       raise ValueError('"cell-identifiers" kwarg must have a length > 1')
    if len(cell_identifiers) > 0:
        args.append('--cell-identifiers')
        for value in cell_identifiers:
            args.append(str(value))


    outputs = _pipeline.run(args, pipeline_outputs, pipeline_inputs)

    result = outputs[0].data
    return result

