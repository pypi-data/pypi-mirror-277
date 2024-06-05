from ....api.jobs import list_jobs
from ....client import Client
from .. import list_jobs

def sync(
        app_title: str,
        allow_preview: bool = False,
        client: Client = None
):
    """
    Get the full info of a running app given its title. If multiple apps match the title,
    the most recent one (by creation timestamp) will be returned. Note the info does not
    include the job url, use get_job_url() to retrieve it.

    Args:
        app_title: The app title to search for.
        allow_preview: Whether to include apps published in preview mode in the result set.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A dictionary containing information about the app.

    Raises:
        KeyError: If no apps with the given title are found.
    """
    all_jobs = list_jobs.sync(client=client)
    if not allow_preview:
        my_job = list(filter(lambda x: 'os-app-title' in x.labels.additional_properties and x.labels.additional_properties['os-app-title'] == app_title \
                                    and ('os-ancestor' not in x.labels.additional_properties or x.labels.additional_properties['os-ancestor'] == 'none'),
                                    all_jobs))
    else:
        my_job = list(filter(lambda x: 'os-app-title' in x.labels.additional_properties and (x.labels.additional_properties['os-app-title'] == app_title \
                                    or x.labels.additional_properties['os-app-title'] == "preview-" + app_title) \
                                    and ('os-ancestor' not in x.labels.additional_properties or x.labels.additional_properties['os-ancestor'] == 'none'),
                                    all_jobs))        
    if not my_job:
        raise KeyError("Cannot find app with given title!")
    my_job = max(my_job, key= lambda x: x.creation_timestamp)
    return my_job

async def asyncio(
        app_title: str,
        allow_preview: bool = False,
        client: Client = None
):
    """
    Get asynchronously the full info of a running app given its title. If multiple apps
    match the title, the most recent one (by creation timestamp) will be returned.

    Args:
        app_title: The app title to search for.
        allow_preview: Whether to include apps published in preview mode in the result set.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A dictionary containing information about the app.

    Raises:
        KeyError: If no apps with the given title are found.
    """
    all_jobs = list_jobs.asyncio(client=client)
    if not allow_preview:
        my_job = list(filter(lambda x: 'os-app-title' in x.labels.additional_properties and x.labels.additional_properties['os-app-title'] == app_title \
                                    and ('os-ancestor' not in x.labels.additional_properties or x.labels.additional_properties['os-ancestor'] == 'none'),
                                    all_jobs))
    else:
        my_job = list(filter(lambda x: 'os-app-title' in x.labels.additional_properties and (x.labels.additional_properties['os-app-title'] == app_title \
                                    or x.labels.additional_properties['os-app-title'] == "preview-" + app_title) \
                                    and ('os-ancestor' not in x.labels.additional_properties or x.labels.additional_properties['os-ancestor'] == 'none'),
                                    all_jobs))    
    if not my_job:
        raise KeyError("Cannot find app with given title!")
    my_job = max(my_job, key= lambda x: x.creation_timestamp)
    return my_job
