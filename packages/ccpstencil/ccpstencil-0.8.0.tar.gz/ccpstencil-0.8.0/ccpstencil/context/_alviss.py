__all__ = [
    'AlvissContext',
]

from ccpstencil.structs import *
from alviss import quickloader
from ccptools.tpu import iters
from pathlib import Path
import logging
log = logging.getLogger(__file__)


class AlvissContext(IContext):
    def __init__(self, file_name: Union[str, Path], **kwargs):
        self._file_name = str(file_name)
        self._data = quickloader.autoload(file_name)
        self._update_map: Dict[Tuple[str], Any] = {}

    def update(self, key: str, value: Any):
        self._data[key] = value

    def nested_update(self, key_tuple: Union[str, Tuple[str]], value: Any):
        log.debug(f'nested_update({key_tuple=}, {value=})')
        if isinstance(key_tuple, str):
            key_tuple = key_tuple.split('.')
        if isinstance(key_tuple, List):
            key_tuple = tuple(key_tuple)
        self._data.update(**iters.nest_dict(list(key_tuple), value))  # noqa

    def as_dict(self) -> Dict:
        return self._data.as_dict(unmaksed=True)
