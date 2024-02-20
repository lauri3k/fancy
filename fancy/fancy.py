from typing import Tuple
from nbgrader.preprocessors import NbGraderPreprocessor
from nbconvert.exporters.exporter import ResourcesDict
from nbformat.notebooknode import NotebookNode


class FancyPreprocessor(NbGraderPreprocessor):
    def preprocess(
        self, nb: NotebookNode, resources: ResourcesDict
    ) -> Tuple[NotebookNode, ResourcesDict]:
        """
        Do something with notebook.
        """
        return nb, resources
