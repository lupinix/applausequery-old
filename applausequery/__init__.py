#
# Licensed under a 3-clause BSD style license - see LICENSE in top directory
#

# internal imports
from . import tap

# Standard library imports

# Third party modules

def auth_token(token):
    """
    Allows to set the APPLAUSE API token for authorization

    Parameters
    ----------
    token : str
        API token as obtained from APPLAUSE web interface, set to None to unset token.
    """
    tap.token = token