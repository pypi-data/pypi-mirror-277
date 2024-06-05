import click
from eximreservoirsimulation.explicit_and_implicit_with_UI import Simres

import sys
from streamlit.web import cli as stcli


@click.command()
@click.option(
    '-w',
    '--web',
    default='web',
    help='The mode of the simulation. They are: Standard, Sensitivity, Optimization, Uncertainty'
)
def entry_point(**kwargs):
    """ Manages CLI """
    # Defining the cli command for path
    sys.argv = ["streamlit", "run", "eximreservoirsimulation/explicit_and_implicit_with_UI.py"]
    sys.exit(stcli.main())



