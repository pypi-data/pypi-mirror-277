"""context module"""
import json
from pathlib import Path
from typing import Tuple
from matatika.exceptions import (
    ContextExistsError,
    ContextDoesNotExistError,
    NoDefaultContextSetError
)


FILE = 'contexts.json'

DEFAULT = 'default'
CONTEXTS = 'contexts'
TEMPLATE = {
    DEFAULT: None,
    CONTEXTS: {}
}


class MatatikaContext():
    """Class to handle read/write operations to a contexts file"""

    def __init__(self, matatika_dir):
        matatika_dir = Path(matatika_dir)
        Path.mkdir(matatika_dir, exist_ok=True)
        self.contexts_file = matatika_dir / FILE

        # create the templated file if it doesn't already exist
        if not self.contexts_file.exists():
            with open(self.contexts_file, 'x', encoding='utf8') as contexts_file:
                json.dump(TEMPLATE, contexts_file)

    def _read_json(self) -> dict:

        with open(self.contexts_file, 'r', encoding='utf8') as contexts_file:
            contexts = json.load(contexts_file)
            return contexts

    def _write_json(self, contexts: dict) -> None:

        with open(self.contexts_file, 'w', encoding='utf8') as contexts_file:
            json.dump(contexts, contexts_file)

    def get_context(self, context_name: str) -> dict:
        """Returns the context 'context_name"""

        contexts = self._read_json()
        self._check_context_exists(context_name, contexts)

        return contexts[CONTEXTS][context_name]

    def get_all_contexts(self) -> dict:
        """Returns all contexts"""

        return self._read_json()[CONTEXTS]

    def create_context(self, context_name: str, variables: dict) -> None:
        """Creates a context in the contexts file"""

        contexts = self._read_json()
        self._check_context_does_not_exist(context_name, contexts)

        contexts[CONTEXTS].update({context_name: variables})
        self._write_json(contexts)

    def delete_context(self, context_name: str) -> None:
        """Deletes the context 'context_name', if it exists"""

        contexts = self._read_json()
        self._check_context_exists(context_name, contexts)

        contexts[CONTEXTS].pop(context_name)
        self._write_json(contexts)

    def get_default_context(self) -> Tuple[str, dict]:
        """Gets the default context 'context_name', if it exists"""

        contexts = self._read_json()
        default_context_name = contexts[DEFAULT]

        if default_context_name is None:
            raise NoDefaultContextSetError

        return default_context_name, contexts[CONTEXTS][default_context_name]

    def set_default_context(self, context_name: str) -> None:
        """Sets the context 'context_name' as the default, if it exists"""

        contexts = self._read_json()

        if context_name is not None:
            self._check_context_exists(context_name, contexts)

        default_context = {"default": context_name}
        contexts.update(default_context)
        self._write_json(contexts)

    def update_default_context_variables(self, update_variables: dict) -> None:
        """Updates a context in the contexts file"""

        name, variables = self.get_default_context()
        contexts = self._read_json()
        self._check_context_exists(name, contexts)

        diff = set(update_variables.items()) - set(variables.items())
        if not diff:
            return

        contexts[CONTEXTS][name].update(diff)
        self._write_json(contexts)

    @staticmethod
    def _check_context_exists(context_name: str, contexts: dict) -> None:

        if context_name not in contexts[CONTEXTS]:
            raise ContextDoesNotExistError(context_name)

    @staticmethod
    def _check_context_does_not_exist(context_name: str, contexts: dict) -> None:

        if context_name in contexts[CONTEXTS]:
            raise ContextExistsError(context_name)
