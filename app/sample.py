import os
import datetime
# CI/CDを体験するために適当な関数を定義

# 指定ディレクトリにあるファイルの名前を書き換える関数
# 元のファイル名の末尾に、そのファイルが作成された日時を追加する


def _get_date_created(file_path: str) -> str:
    """ファイルの作成日時を取得する

    Args:
        file_path (str): ファイルのパス

    Returns:
        float: ファイルの作成日時
    """
    timestamp = os.path.getctime(file_path)
    # float型のタイムスタンプを返されるので、datetime型に変換
    # 年月日をyyyy_mm_ddの形式で返す
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y_%m_%d")


def rename_files_in_dir(target_dir: str) -> None:
    # 指定ディレクトリにあるファイルの名前を書き換える
    files = os.listdir(target_dir)
    for file in files:
        # ファイル名の末尾に、そのファイルが作成された日時を追加
        filepath = os.path.join(target_dir, file)
        date_created = _get_date_created(filepath)
        # 新しいファイル名を作成とパス
        new_file_name = f"{file}_{date_created}"
        new_path = os.path.join(target_dir, new_file_name)
        os.rename(filepath, new_path)
