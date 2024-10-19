# cicd/tests/conftest.py
import sys
from pathlib import Path

# pathlibを使ってappディレクトリを検索パスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / 'app'))
