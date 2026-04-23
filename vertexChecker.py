import re

# ここに確認したいX3Dのテキストを貼り付け
x3d_text = """
						<IndexedFaceSet solid="false"
						                normalPerVertex="true"
						                texCoordIndex="0 1 2 -1 3 4 5 -1 6 7 8 -1 9 10 11 -1 12 13 14 -1 15 16 17 -1 18 19 20 -1 21 22 23 -1 24 25 26 -1 27 28 29 -1 30 31 32 -1 33 34 35 -1 "
						                coordIndex="10 8 9 -1 20 18 19 -1 7 15 6 -1 17 22 23 -1 14 0 2 -1 3 5 13 -1 10 12 8 -1 20 21 18 -1 7 16 15 -1 17 11 22 -1 14 4 0 -1 3 1 5 -1 "
						                >
"""

def check_indices(text):
    # 正規表現で属性の中身を抽出
    coord_match = re.search(r'coordIndex="([^"]+)"', text)
    tex_match = re.search(r'texCoordIndex="([^"]+)"', text)

    if not coord_match or not tex_match:
        print("テキストの中から coordIndex または texCoordIndex が見つかりませんでした。")
        return

    # スペースで分割してリスト化
    coord_list = coord_match.group(1).split()
    tex_list = tex_match.group(1).split()

    coord_count = len(coord_list)
    tex_count = len(tex_list)

    print(f"coordIndexの要素数（-1含む）: {coord_count}個")
    print(f"texCoordIndexの要素数（-1含む）: {tex_count}個")
    print("-" * 30)

    if coord_count == tex_count:
        print("要素数は一致しています")
    else:
        print(f"要素数が {abs(coord_count - tex_count)} 個ずれています")

check_indices(x3d_text)