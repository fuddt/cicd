import os
import tempfile
import datetime
from cicd.app.sample import rename_files_in_dir, _get_date_created

def test_get_date_created():
    # 一時ファイルを作成して、その作成日時を取得
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name

    try:
        # 現在のタイムスタンプを取得して、期待されるフォーマットに変換
        expected_date = datetime.datetime.now().strftime("%Y_%m_%d")
        assert _get_date_created(file_path) == expected_date
    finally:
        os.remove(file_path)  # テスト終了後、ファイルを削除

def test_rename_files_in_dir():
    # 一時ディレクトリを作成
    with tempfile.TemporaryDirectory() as tmp_dir:
        # 一時ファイルを作成
        tmp_file_path = os.path.join(tmp_dir, "testfile.txt")
        with open(tmp_file_path, "w") as f:
            f.write("dummy content")

        # 関数を実行
        rename_files_in_dir(tmp_dir)

        # ファイル名が変更されたか確認
        renamed_files = os.listdir(tmp_dir)
        assert len(renamed_files) == 1  # ファイルは1つだけのはず
        new_file_name = renamed_files[0]
        assert "testfile.txt_" in new_file_name  # ファイル名に作成日時が含まれているか確認
