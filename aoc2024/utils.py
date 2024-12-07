import importlib.resources as resources


def get_filepath(anchor: str, filename: str) -> str:
    return resources.files(anchor).joinpath(filename)
