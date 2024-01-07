import interpreter
import os

interpreter.model = f"azure/{os.environ['AZURE_API_DEPLOYMENT_ID']}"
interpreter.auto_run = True  # ユーザーの確認なしで生成されたコードを自動的に実行できるようになる
interpreter.api_base = os.environ["AZURE_API_BASE"]
interpreter.api_key = os.environ["AZURE_API_KEY"]
interpreter.api_version = os.environ["AZURE_API_VERSION"]
interpreter.debug_mode = False
interpreter.temperature = 1.0

input_dir = "input"
output_dir = "output"
file_type = "xlsx"
filename = "kinkyuuhinanbasho.xlsx"

prompt = f"""
あなたは、プログラムを実行するコンピュータです。
「あなたが実行すること」を確認し実行してください。

# あなたが実行すること
{file_type}の拡張子で記述されたファイルを読み込み、{output_dir}に保存します。
あなたが読み込むファイルは、{input_dir}/{filename}にあります。
このタスクに成功することがあなたの使命です。

# 前提条件
(1)
あなたが利用できるライブラリの一覧は以下の通りです。
それ以外のライブラリを使うとペナルティが発生します。
- pandas
- openpyxl
"""

if __name__ == "__main__":
    interpreter.chat(prompt)  # コマンドを実行
