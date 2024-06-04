from aligo import Aligo, CreateFileResponse
from aligo.types.Enum import CheckNameMode


def create_folder(alipan_api: Aligo, name: str,
                  parent_file_id: str = 'root', drive_id: str = None,
                  check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
    """
    创建文件夹
    :param alipan_api: Aligo
    :param name: [str] 文件夹名
    :param parent_file_id: Optional[str] 父文件夹id, 默认为 'root'
    :param drive_id: Optional[str] 指定网盘id, 默认为 None
    :param check_name_mode: Optional[CheckNameMode] 检查文件名模式, 默认为 'auto_rename'
    :return: [CreateFileResponse]
    """
    return alipan_api.create_folder(name=name,
                                    parent_file_id=parent_file_id,
                                    drive_id=drive_id,
                                    check_name_mode=check_name_mode)


