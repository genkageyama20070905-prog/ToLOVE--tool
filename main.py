import streamlit as st

st.set_page_config(page_title="メモ入力補助ツール", layout="centered")

# カスタムCSS（ボタンを画面幅いっぱいに広げる）
st.markdown("<style>.stButton>button { width: 100%; }</style>", unsafe_allow_index=True)

st.title("メモ入力補助ツール")

# 記録を保存するためのセッション
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = ""
if 'last' not in st.session_state:
    st.session_state.last = ""

# ボタンのラベルに印をつける関数
def label(name):
    return f"{name} 👈" if st.session_state.last == name else name

# --- ① ゲーム数入力 ---
st.subheader("① ゲーム数設定")
game_input = st.number_input("ゲーム数", min_value=0, step=1, value=0, key="game")
if st.button(label("🔢 ゲーム数を出力")):
    st.session_state.memo_log += f"\n{game_input} "
    st.session_state.last = "🔢 ゲーム数を出力"

# --- ② 演出・状態 ---
st.subheader("② 演出・状態")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button(label("バルーン")): 
        st.session_state.memo_log += "バルーン\n"; st.session_state.last = "バルーン"
with c2:
    if st.button(label("スイート")): 
        st.session_state.memo_log += "スイート\n"; st.session_state.last = "スイート"
with c3:
    if st.button(label("ぷっちゅん")): 
        st.session_state.memo_log += "ぷっちゅん\n"; st.session_state.last = "ぷっちゅん"
with c4:
    if st.button(label("追憶")): 
        st.session_state.memo_log += "追憶\n"; st.session_state.last = "追憶"

# --- ③ 小役・対応 ---
st.subheader("③ 小役・対応")
# 1段目（3列）
c5, c6, c7 = st.columns(3)
with c5:
    if st.button(label("🔔")): 
        st.session_state.memo_log += "🔔"; st.session_state.last = "🔔"
with c6:
    if st.button(label("非対応")): 
        st.session_state.memo_log += "非対応 "; st.session_state.last = "非対応"
with c7:
    if st.button(label("対応")): 
        st.session_state.memo_log += "対応 "; st.session_state.last = "対応"
# 2段目（3列）
c8, c9, c10 = st.columns(3)
with c8:
    if st.button(label("ミッション")): 
        st.session_state.memo_log += "ミッション "; st.session_state.last = "ミッション"
with c9:
    if st.button(label("確定役")): 
        st.session_state.memo_log += "確定役 "; st.session_state.last = "確定役"
with c10:
    if st.button(label("⭕️")): 
        st.session_state.memo_log += " ⭕️ "; st.session_state.last = "⭕️"

# --- ④ 報酬設定 ---
st.subheader("④ 報酬設定")
reward_val = st.number_input("報酬枚数", min_value=0, step=10, value=0, key="reward")
c11, c12, c13 = st.columns(3)
with c11:
    if st.button(label("ばいん")): 
        st.session_state.memo_log += f"ばいん {reward_val}\n"; st.session_state.last = "ばいん"
with c12:
    if st.button(label("ぺろぺろ")): 
        st.session_state.memo_log += f"ぺろぺろ {reward_val}\n"; st.session_state.last = "ぺろぺろ"
with c13:
    if st.button(label("愛すぷ")): 
        st.session_state.memo_log += f"愛すぷ {reward_val}\n"; st.session_state.last = "愛すぷ"

# --- 出力エリア ---
st.divider()
st.subheader("出力結果")
st.text_area("コピー用", value=st.session_state.memo_log, height=300)

if st.button("履歴をすべてリセット"):
    st.session_state.memo_log = ""; st.session_state.last = ""; st.rerun()
