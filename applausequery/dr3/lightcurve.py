#
# Licensed under a 3-clause BSD style license - see LICENSE in top directory
#

# internal imports
from .. import tap

# Standard library imports

# Third party modules


def query_basic_lc_by_ucac4_id(ucac4_id, force_download=False):
    query = "SELECT jd_mid,bmag,bmagerr,vmag,vmagerr \
        FROM applause_dr3.lightcurve \
        WHERE bmag IS NOT NULL \
        AND bmagerr IS NOT NULL \
        AND vmag IS NOT NULL \
        AND vmagerr IS NOT NULL \
        AND ucac4_id=\'%s\' \
        ORDER BY jd_mid" %(ucac4_id)
    lc = tap.query_applause(query,force_download,table_file="applausedr3_lightcurve_ucac4_"+ucac4_id+".xml")
    return lc
