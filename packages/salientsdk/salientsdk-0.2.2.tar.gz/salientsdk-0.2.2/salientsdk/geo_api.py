#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Interface to the Salient geo API.

Command line usage example:
```
cd ~/salientsdk
python -m salientsdk downscale -lat 42 -lon -73 --date 2020-01-01 -u username -p password --force
```

"""

import requests

from .constants import _build_urls, _collapse_comma
from .location import Location
from .login_api import download_queries

_EXCLUDE_ARGS = ["force", "session", "verify", "verbose", "destination", "loc", "kwargs"]

VARIABLES = ["elevation", "population"]
RESOLUTIONS = [1 / 4, 1 / 8, 1 / 16]


def geo(
    # API arguments -----
    loc: Location,
    variables: str | list[str] = "elevation",
    resolution: float = 0.25,
    # Non-API arguments --------
    destination: str = "-default",
    force: bool = False,
    session: requests.Session | None = None,
    apikey: str | None = None,
    verify: bool | None = None,
    verbose: bool = False,
    **kwargs,
) -> str | list[str]:
    """Get static geo-data.

    Args:
        loc (Location): The location to query.
            If using a `shapefile` or `location_file`, may input a vector of file names which
            will trigger multiple calls to `downscale`.  This is useful because `downscale` requires
            that all points in a file be from the same continent.
        variables (str): The variables to query, defaults to "elevation".
            Supports a comma separated list or list of variables.
        resolution (float): The spatial resolution of the data in degrees.
        destination (str): The destination directory for downloaded files.
        force (bool): If False (default), don't download the data if it already exists
        session (requests.Session): The session object to use for the request
        apikey (str | None): The API key to use for the request.
            In most cases, this is not needed if a `session` is provided.
        verify (bool): If True (default), verify the SSL certificate
        verbose (bool): If True (default False) print status messages
        **kwargs: Additional arguments to pass to the API

    Returns:
        str | pd.DataFrame : If only one file was downloaded, return the name of the file.
            If multiple files were downloaded, return a table with column `file_name` and
            additional columns documenting the vectorized input arguments such as
            `location_file`.
    """
    assert resolution in RESOLUTIONS, f"Resolution must be one of {RESOLUTIONS}"
    variables = _collapse_comma(variables, VARIABLES)

    args = {k: v for k, v in {**locals(), **kwargs}.items() if k not in _EXCLUDE_ARGS}
    queries = _build_urls(endpoint="geo", args=loc.asdict(**args), destination=destination)

    # geo currently takes no "format" argument, so we need to set the file name post hoc
    # instead of just counting on _build_urls to do it for us:
    format = "nc"
    queries["file_name"] = queries["file_name"] + f".{format}"

    download_queries(
        query=queries["query"].values,
        file_name=queries["file_name"].values,
        force=force,
        session=session,
        verify=verify,
        verbose=verbose,
        format=format,
        max_workers=5,  # downscale @limiter.limit("5 per second")
    )

    if len(queries) == 1:
        return queries["file_name"].values[0]
    else:
        queries = queries.drop(columns="query")
        return queries
