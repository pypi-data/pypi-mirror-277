import os

def sync(key: str) -> str:
    """
    Reads an application secret value, given its key.

    Args:
        key: The key for the application secret.
    Returns:
        A list of WatcherIntent objects which failed to execute.

    Raises:
        ValueError: If the key is not valid.
        RuntimeError: If the secrets file could not be read.
    """
    if not key or not isinstance(key, str):
        raise ValueError("key must be a non-empty string")
    if not key.strip():
        raise ValueError("key must be non-empty")

    sanitized_key = key.replace('/', '_').replace('.', '_').replace('-', '_').replace(' ', '_')
    path = '/etc/secrets/' + sanitized_key

    if not os.path.isfile(path):
        raise RuntimeError(f"Secret file not found at {path}")

    try:
        with open(path, 'r') as file:
            line = file.readline()
            if not line:
                raise ValueError(f"Secret file {path} is empty")
            return line.strip()
    except Exception as e:
        print(f"Error reading secret file {path}: {e}")
        raise RuntimeError(f"Error reading secret file {path}: {e}")
    
async def asyncio(key: str) -> str:
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()
