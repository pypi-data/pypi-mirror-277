from abc import ABC
from pathlib import PurePath, Path
from aiofiles import AIOFile
from ...exceptions import FileError
from ...template import getTemplateHandler, TemplateHandler


class TemplateSupport(ABC):
    """TemplateSupport.

    Adding Support for Jinja2 Template parser on Components.
    """

    use_template: bool = False

    def __init__(self, **kwargs):
        try:
            self.use_template: bool = bool(kwargs["use_template"])
            del kwargs["use_template"]
        except KeyError:
            self.use_template: bool = False
        # Template directory
        try:
            template_dir = kwargs["template_dir"]
            del kwargs["template_dir"]
        except KeyError:
            template_dir = None
        # Template Parser:
        self._templateparser: TemplateHandler = None
        if self.use_template is True:
            self._templateparser = getTemplateHandler(newdir=template_dir)

    async def open_templatefile(self, file: PurePath, **kwargs) -> str:
        if isinstance(file, str):
            file = Path(file)
        if not file.is_absolute():
            # File is relative to TaskStorage:
            directory = self._filestore.get_directory('templates')
            file = directory.joinpath(file).resolve()
        if file.exists() and file.is_file():
            content = None
            # open SQL File:
            async with AIOFile(file, "r+") as afp:
                content = await afp.read()
                # check if we need to replace masks
            if hasattr(self, "masks"):
                content = self.mask_replacement(content)
            if self.use_template is True:
                content = self._templateparser.from_string(
                    content,
                    kwargs
                )
            return content
        else:
            raise FileError(
                f"{__name__}: Missing Template File: {file}"
            )
