from pathlib import Path


def ensureDirExist(path: str):
    """确保路径存在
    @param path:文件夹路径。 x:\\abc`
    """
    dir_path = Path(path)
    dir_path.mkdir(exist_ok=True)


# end def


def ensurePathExist(path: str):
    """确保路径存在
    @param path:文件路径。 x:\\abc\\file.txt`
    """
    # 指定文件路径
    file_path = Path(path)
    # 确保路径存在，如果不存在则创建
    file_path.parent.mkdir(parents=True, exist_ok=True)


__all__ = ["ensurePathExist", "ensureDirExist"]
