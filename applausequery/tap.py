#
# Licensed under a 3-clause BSD style license - see LICENSE in top directory
#

# internal imports

# Standard library imports
import os.path 

# Third party modules
from astropy.table import Table
import pyvo as vo

# General settings
__tapurl__ = "https://www.plate-archive.org/tap"
# Personal authentication token (to be obtained in APPLAUSE web interface)
token = None


def query_applause(query,
                background=False,
                table_file=None,
                force_download=False):
    """
    Queries the APPLAUSE TAP service and returns result as a table object

    Parameters
    ----------
    query : str
        The ADQL query as a string   
    background : bool, optional
        Execute query in background (default: False), not yet implemented
    table_file : str, optional
        Path of VOTable file to be saved and used for caching
    force_download : bool
        Force querying APPLAUSE even if the VOTable already exists
    
    Returns
    -------
    table : astropy.table.Table
        Astropy table containing the result of the query
    """
    if not os.path.isfile(table_file) or force_download:
        tap_service = vo.dal.TAPService(__tapurl__)
        if token is not None:
            vo.utils.http.session.headers['Authorization'] = 'Token ' + token
        result = tap_service.run_async(query)
        if table_file is not None:
            result.votable.to_xml(table_file, tabledata_format="binary2")
        return result.to_table()
    else:
        return Table.read(table_file, format="votable")
