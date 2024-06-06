import os
from .util import get_file_paths
import pickle


class InstanceFiles:
    def __init__(self):
        self._file_paths = None
        self._path_by_file_name = None

    def _get_file_paths(self):
        if self._file_paths is None:
            self._file_paths = get_file_paths()
            self._path_by_file_name = {
                os.path.splitext(os.path.basename(p))[0]: p for p in self._file_paths
            }
        return self._file_paths

    def _get_file_path_by_file_name(self, file_name):
        if self._path_by_file_name is None:
            self._get_file_paths()
        return self._path_by_file_name[file_name]

    def _load_file(self, file_path):
        with open(file_path, "rb") as f:
            instance = pickle.load(f)
        return instance

    def __getitem__(self, file_name):
        file_path = self._get_file_path_by_file_name(file_name)
        return self._load_file(file_path)

    def __iter__(self):
        for file_path in self._get_file_paths():
            yield self._load_file(file_path)

    def values(self):
        return self.__iter__()

    def items(self):
        for file_path in self._get_file_paths():
            yield file_path, self._load_file(file_path)

    def keys(self):
        self._get_file_paths()
        return sorted(self._path_by_file_name.keys())
