import pathlib
import tempfile
import zipfile


def calltracker(func):
    """Decorator to track how many times a function is called"""

    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return func(*args, **kwargs)

    wrapped.calls = 0
    return wrapped


def find_data(path):
    """Find .avi and .rtdc data files in a directory"""
    path = pathlib.Path(path)
    avifiles = [r for r in path.rglob("*.avi") if r.is_file()]
    rtdcfiles = [r for r in path.rglob("*.rtdc") if r.is_file()]
    files = [pathlib.Path(ff) for ff in rtdcfiles + avifiles]
    return files


def retrieve_data(zip_file):
    """Extract contents of data zip file and return data files
    """
    zpath = pathlib.Path(__file__).resolve().parent / "data" / zip_file
    # unpack
    arc = zipfile.ZipFile(str(zpath))

    # extract all files to a temporary directory
    edest = tempfile.mkdtemp(prefix=zpath.name)
    arc.extractall(edest)

    # Load RT-DC dataset
    # find tdms files
    datafiles = find_data(edest)

    if len(datafiles) == 1:
        datafiles = datafiles[0]

    return datafiles


def find_model(path):
    """Find .ckp files in a directory"""
    path = pathlib.Path(path)
    jit_files = [r for r in path.rglob("*.ckp") if r.is_file()]
    files = [pathlib.Path(ff) for ff in jit_files]
    return files


def retrieve_model(zip_file):
    """Extract contents of model zip file and return model ckeckpoint paths
    """
    zpath = pathlib.Path(__file__).resolve().parent / "data" / zip_file
    # unpack
    arc = zipfile.ZipFile(str(zpath))

    # extract all files to a temporary directory
    edest = tempfile.mkdtemp(prefix=zpath.name)
    arc.extractall(edest)

    # find model checkpoint paths
    modelpaths = find_model(edest)

    if len(modelpaths) == 1:
        modelpaths = modelpaths[0]

    return modelpaths
