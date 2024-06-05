# Copyright 2024 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import json
import time
import signal
import argparse

from rich.console import Console
from rich.markdown import Markdown
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    MofNCompleteColumn,
    TimeElapsedColumn,
    TaskID,
)

from .__version__ import __version__
from .common.simulation_manager import SimulationManager


def cli():
    """
    Read a text file in CACE (ASCII) format 4.0, run
    simulations and analysis on electrical and physical
    parameters, as appropriate, and write out a modified
    file with simulation and analysis results.
    """

    parser = argparse.ArgumentParser(
        prog='cace',
        description="""This program parses the CACE characterization 
        file, runs simulations, and can output a modified file annotated with 
        characterization results.""",
        epilog='Online documentation at: https://cace.readthedocs.io/',
    )

    # version number
    parser.add_argument(
        '--version', action='version', version=f'%(prog)s {__version__}'
    )

    # positional argument, optional
    parser.add_argument(
        'datasheet', nargs='?', help='input specification datasheet (YAML)'
    )

    # positional argument, optional
    parser.add_argument(
        'output',
        nargs='?',
        help='output specification datasheet (YAML)',
    )

    parser.add_argument(
        '-s',
        '--source',
        type=str,
        choices=['schematic', 'layout', 'rcx', 'all', 'best'],
        default='best',
        help="""restricts characterization to the
        specific netlist source, which is either schematic capture
        layout extracted, or full R-C parasitic extracted.  If not
        specified, then characterization is run on the full R-C
        parasitic extracted layout netlist if available, and the
        schematic captured netlist if not (option "best")""",
    )
    parser.add_argument(
        '-p',
        '--parameter',
        nargs='+',
        default=None,
        help='runs simulations on only the named electrical or physical parameters, by default it runs all parameters',
    )
    parser.add_argument(
        '--parallel_parameters',
        type=int,
        default=4,
        help='the number of parameters running in parallel',
    )
    parser.add_argument(
        '-f',
        '--force',
        action='store_true',
        help='forces new regeneration of all netlists',
    )
    parser.add_argument(
        '-k',
        '--keep',
        action='store_true',
        help='retains files generated for characterization',
    )
    parser.add_argument(
        '--no-plot', action='store_true', help='do not generate any graphs'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='generates additional diagnostic output',
    )
    parser.add_argument(
        '--sequential',
        action='store_true',
        help='runs simulations sequentially',
    )
    parser.add_argument(
        '--no-simulation',
        action='store_true',
        help="""does not re-run simulations if the output file exists.
    (Warning: Does not check if simulations are out of date)""",
    )
    parser.add_argument(
        '--no-progress',
        action='store_true',
        help='do not display the progress bar',
    )
    parser.add_argument(
        '--summary',
        help='output path for the summary e.g. final/summary.md',
    )

    # Parse arguments
    args = parser.parse_args()

    # Create the SimulationManager
    simulation_manager = SimulationManager()

    # Load the datasheet
    if args.datasheet:
        if simulation_manager.load_datasheet(args.datasheet, args.debug):
            sys.exit(0)
    # Else search for it starting from the cwd
    else:
        if simulation_manager.find_datasheet(os.getcwd(), args.debug):
            sys.exit(0)

    # Set runtime options
    simulation_manager.set_runtime_options('debug', args.debug)
    simulation_manager.set_runtime_options('force', args.force)
    simulation_manager.set_runtime_options('keep', args.keep)
    simulation_manager.set_runtime_options('noplot', args.no_plot)
    simulation_manager.set_runtime_options('nosim', args.no_simulation)
    simulation_manager.set_runtime_options('sequential', args.sequential)
    simulation_manager.set_runtime_options('netlist_source', args.source)
    simulation_manager.set_runtime_options(
        'parallel_parameters', args.parallel_parameters
    )

    # Rich console
    console = Console()

    # Create the progress bar
    progress = Progress(
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
        disable=args.no_progress,
    )

    # Add a single task for all parameters
    progress.start()
    task_id = progress.add_task(
        'Running parameters',
    )

    # Queue specified parameters
    if args.parameter:
        if args.debug:
            print(f'Running simulation for: {args.parameter}')
        for pname in args.parameter:
            simulation_manager.queue_parameter(
                pname,
                cb=lambda pname, canceled=False: progress.update(
                    task_id, advance=1
                ),
            )
    # Queue all parameters
    else:
        pnames = simulation_manager.get_all_pnames()
        if args.debug:
            print(f'Running simulation for: {pnames}')
        for pname in pnames:
            simulation_manager.queue_parameter(
                pname,
                cb=lambda pname, canceled=False: progress.update(
                    task_id, advance=1
                ),
            )

    # Set the total number of parameters in the progress bar
    progress.update(task_id, total=simulation_manager.num_queued_parameters())

    # Run the simulations
    simulation_manager.run_parameters_async()

    # Wait for completion
    simulation_manager.join_parameters()

    # Stop the progress bar
    progress.stop()

    if args.debug:
        print('Done with CACE simulations and evaluations.')

    if args.output:
        simulation_manager.save_datasheet(args.output)

    # Print the summary to the console
    summary = simulation_manager.summarize_datasheet()
    console.print(Markdown(summary))

    # Write the summary to a file
    if args.summary:
        dirname = os.path.dirname(args.summary) or os.getcwd()
        filename = os.path.basename(args.summary)

        # Check whether path to file exists
        if os.path.isdir(dirname):
            with open(os.path.join(dirname, filename), 'w') as ofile:
                ofile.write(summary)
        else:
            print(
                f"Couldn't write summary, invalid path: {os.path.dirname(args.summary)}"
            )


if __name__ == '__main__':
    cli()
