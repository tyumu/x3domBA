import bpy

# x3d用に<coordinateinterpolatorを書き出すスクリプト
#bledner上で実行する
def export_x3d_interpolator():
    # アクティブなオブジェクトを取得
    obj = bpy.context.active_object
    if obj is None or obj.type != 'MESH':
        print("メッシュオブジェクトを選択してから実行してください。")
        return

    scene = bpy.context.scene
    
    #アニメーションタブで開始フレームと終了フレームを調節すること(面倒ならハードコードでもいい)
    #初期設定は開始1 終了250
    start_frame = scene.frame_start
    end_frame = scene.frame_end
    
    total_frames = end_frame - start_frame + 1

    # .blendファイルと同じ場所に「x3d_yukari_export.txt」として保存
    output_path = bpy.path.abspath("//x3d_yukari_export.txt")

    keys = []
    key_values = []

    # モディファイアやアーマチュアの変形を計算するための依存関係グラフを取得
    depsgraph = bpy.context.evaluated_depsgraph_get()

    print(f"--- ベイクを開始します。総フレーム数: {total_frames} ---")

    for f in range(start_frame, end_frame + 1):
        scene.frame_set(f)
        
        # 現在のフレームでの変形結果が適用されたメッシュを取得します
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()

        frame_coords = []
        for v in mesh.vertices:
            # 小数点以下4桁に丸めてファイル容量を節約
            frame_coords.append(f"{v.co.x:.4f} {v.co.z:.4f} {-v.co.y:.4f}")
        
        # 1フレーム分の全頂点座標をスペース区切りで結合
        key_values.append(" ".join(frame_coords))
        
        # 0.0 ~ 1.0 の key (アニメーションの進行度) を計算
        fraction = (f - start_frame) / max(1, (total_frames - 1))
        keys.append(f"{fraction:.4f}")

        # メモリを無駄遣いしないようにクリア
        eval_obj.to_mesh_clear()

    # ファイルに書き出し
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n")
        file.write("<coordinateinterpolator DEF='ci' ")
        file.write(f"key='{' '.join(keys)}' ")
        file.write(f"keyValue='{' '.join(key_values)}' ")
        file.write("></coordinateinterpolator>\n")

    print(f"完了しました {output_path} を確認")

# 実行
export_x3d_interpolator()