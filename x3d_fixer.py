import sys
import re
import os

def main():
    if len(sys.argv) < 2:
        print("python x3d_fixer.py <ファイル名> で指定してください。")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ファイルが見つかりません。")
        sys.exit(1)

    try:
        # ファイルの読み込み
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 正規表現で置換
        fixed_content = re.sub(r'<([a-zA-Z0-9_]+)([^>]*?)\s*/>', r'<\1\2></\1>', content)

        # 出力ファイル名の生成
        output_file = f"fixed_{os.path.basename(input_file)}"

        # 変換結果の保存
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)

        print(f" 変換終了。'{output_file}' を確認してください。")

    except Exception as e:
        print(f"何かエラー: {e}")

if __name__ == "__main__":
    main()