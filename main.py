import streamlit as st

st.set_page_config(page_title="メモ入力補助ツール", layout="centered")
st.title("メモ入力補助ツール")

# 記録を保存するためのセッション（履歴の保持）
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = ""

# --- ゲーム数入力エリア ---
st.subheader("① ゲーム数設定")
game_input = st.number_input("現在のゲーム数", min_value=0, step=1, value=0)
if st.button("🔢 ゲーム数を出力"):
    st.session_state.memo_log += f"\n{game_input} "

# --- カテゴリ1：演出系 ---
st.subheader("② 演出・状態")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("バルーン"): st.session_state.memo_log += "バルーン "
with c2:
    if st.button("スイート"): st.session_state.memo_log += "スイート "
with c3:
    if st.button("ぷっちゅん"): st.session_state.memo_log += "ぷっちゅん "
with c4:
    if st.button("追憶"): st.session_state.memo_log += "追憶 "

# --- カテゴリ2：小役・対応（横並び入力） ---
st.subheader("③ 小役・対応 (横に並びます)")
c5, c6, c7, c8, c9 = st.columns(5)
with c5:
    if st.button("🔔"): st.session_state.memo_log += "🔔"
with c6:
    if st.button("非対応"): st.session_state.memo_log += "非対応 "
with c7:
    if st.button("対応"): st.session_state.memo_log += "対応 "
with c8:
    if st.button("ミッション"): st.session_state.memo_log += "ミッション "
with c9:
    if st.button("確定役"): st.session_state.memo_log += "確定役 "

# --- カテゴリ3：報酬 ---
st.subheader("④ 報酬")
c10, c11, c12 = st.columns(3)
with c10:
    if st.button("ばいん"): st.session_state.memo_log += "ばいん "
with c11:
    if st.button("ぺろぺろ"): st.session_state.memo_log += "ぺろぺろ "
with c12:
    if st.button("報酬ぷちゅ"): st.session_state.memo_log += "ぷっちゅん(報) "

# --- 出力エリア ---
st.divider()
st.subheader("出力（コピー用）")
st.text_area("生成テキスト", value=st.session_state.memo_log, height=250)

if st.button("履歴をすべてリセット"):
    st.session_state.memo_log = ""
    st.rerun()
