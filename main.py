import streamlit as st

# アプリのタイトル
st.title("メモ入力補助ツール")

# 記録を保存するためのセッション（履歴の保持）
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = []

# --- 入力エリア ---
st.subheader("入力")
game_count = st.number_input("ゲーム数入力", min_value=0, step=1, value=0)

# ボタンを配置
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔔"):
        st.session_state.memo_log.append(f"{game_count} 🔔")
    if st.button("対応 👅"):
        st.session_state.memo_log.append(f"対応 👅 {game_count}")

with col2:
    if st.button("ぷちゅ"):
        st.session_state.memo_log.append(f"{game_count} ぷちゅ")
    if st.button("非対応"):
        st.session_state.memo_log.append(f"非対応 {game_count}")

with col3:
    if st.button("子役なし"):
        st.session_state.memo_log.append("子役なし")
    if st.button("❌"):
        st.session_state.memo_log.append("❌")

# --- 出力エリア ---
st.divider()
st.subheader("出力（メモ帳用）")
final_text = "\n".join(st.session_state.memo_log)
st.text_area("生成されたテキスト", value=final_text, height=200)

if st.button("履歴をリセット"):
    st.session_state.memo_log = []
    st.rerun()
