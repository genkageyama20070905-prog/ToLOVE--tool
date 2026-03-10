import streamlit as st

st.set_page_config(page_title="メモ", layout="centered")
st.title("メモ")

# 記録を保存するためのセッション
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = ""
if 'last_action' not in st.session_state:
    st.session_state.last_action = "なし"

# --- 直前の操作を表示（追加機能） ---
st.info(f"💡 最後に押したボタン: **{st.session_state.last_action}**")

# --- ① ゲーム数入力 ---
st.subheader("① 当選ゲーム数")
game_input = st.number_input("ゲーム数", min_value=0, step=1, value=0, key="game")
if st.button("🔢 ゲーム数を出力"):
    st.session_state.memo_log += f"\n{game_input} "
    st.session_state.last_action = f"ゲーム数({game_input})"

# --- ② 演出・状態 ---
st.subheader("② 当選契機")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("バルーン"): 
        st.session_state.memo_log += "バルーン\n"
        st.session_state.last_action = "バルーン"
with c2:
    if st.button("スイート"): 
        st.session_state.memo_log += "スイート\n"
        st.session_state.last_action = "スイート"
with c3:
    if st.button("ぷっちゅん"): 
        st.session_state.memo_log += "ぷっちゅん\n"
        st.session_state.last_action = "ぷっちゅん"
with c4:
    if st.button("追憶"): 
        st.session_state.memo_log += "追憶\n"
        st.session_state.last_action = "追憶"

# --- ③ ST子役　---
st.subheader("③ 小役・対応 ")
c5, c6, c7, c8, c9, c10 = st.columns(6)
with c5:
    if st.button("🔔"): 
        st.session_state.memo_log += "🔔"
        st.session_state.last_action = "🔔"
with c6:
    if st.button("非対応"): 
        st.session_state.memo_log += "非対応 "
        st.session_state.last_action = "非対応"
with c7:
    if st.button("対応"): 
        st.session_state.memo_log += "対応 "
        st.session_state.last_action = "対応"
with c8:
    if st.button("ミッション"): 
        st.session_state.memo_log += "ミッション "
        st.session_state.last_action = "ミッション"
with c9:
    if st.button("確定役"): 
        st.session_state.memo_log += "確定役 "
        st.session_state.last_action = "確定役"
with c10:
    if st.button("⭕️"): 
        st.session_state.memo_log += " ⭕️ "
        st.session_state.last_action = "⭕️"

# --- ④ 報酬　---
st.subheader("④ 報酬　")
reward_val = st.number_input("報酬枚数", min_value=0, step=10, value=0, key="reward")
c11, c12, c13 = st.columns(3)
with c11:
    if st.button("ばいん"): 
        st.session_state.memo_log += f"ばいん {reward_val}\n"
        st.session_state.last_action = f"ばいん({reward_val})"
with c12:
    if st.button("ぺろぺろ"): 
        st.session_state.memo_log += f"ぺろぺろ {reward_val}\n"
        st.session_state.last_action = f"ぺろぺろ({reward_val})"
with c13:
    if st.button("愛すぷ"): 
        st.session_state.memo_log += f"愛すぷ {reward_val}\n"
        st.session_state.last_action = f"愛すぷ({reward_val})"

# --- 出力エリア ---
st.divider()
st.subheader("出力結果")
st.text_area("メモ帳用テキスト", value=st.session_state.memo_log, height=300)

if st.button("履歴をすべてリセット"):
    st.session_state.memo_log = ""
    st.session_state.last_action = "リセット済み"
    st.rerun()
