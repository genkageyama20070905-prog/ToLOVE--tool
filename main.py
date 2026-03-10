import streamlit as st

st.set_page_config(page_title="メモ", layout="centered")
st.title("メモ")

# --- 1. URLから履歴を復元する処理 (リロード対策) ---
if "log" in st.query_params and 'memo_log' not in st.session_state:
    st.session_state.memo_log = st.query_params["log"]

# セッション状態の初期化
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = ""
if 'last_action' not in st.session_state:
    st.session_state.last_action = "なし"

# --- 2. 共通の更新関数 ---
def update_log(text, action):
    st.session_state.memo_log += text
    st.session_state.last_action = action
    # URLの末尾にデータを書き込む (これでリロードしても消えない)
    st.query_params["log"] = st.session_state.memo_log

# --- 直前の操作を表示 ---
st.info(f"💡 最後に押したボタン: **{st.session_state.last_action}**")

# --- ① 当選ゲーム数 ---
st.subheader("① 当選ゲーム数")
game_input = st.number_input("ゲーム数", min_value=0, step=1, value=0, key="game")
if st.button("🔢 ゲーム数を出力"):
    update_log(f"\n{game_input} ", f"ゲーム数({game_input})")

# --- ② 当選契機 ---
st.subheader("② 当選契機")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("バルーン"): update_log("バルーン\n", "バルーン")
with c2:
    if st.button("スイート"): update_log("スイート\n", "スイート")
with c3:
    if st.button("ぷっちゅん"): update_log("ぷっちゅん\n", "ぷっちゅん")
with c4:
    if st.button("追憶"): update_log("追憶\n", "追憶")

# --- ③ ST小役 ---
st.subheader("③ 小役・対応")
c5, c6, c7, c8, c9, c10 = st.columns(6)
with c5:
    if st.button("🔔"): update_log("🔔", "🔔")
with c6:
    if st.button("非対応"): update_log("非対応 ", "非対応")
with c7:
    if st.button("対応"): update_log("対応 ", "対応")
with c8:
    if st.button("ミッション"): update_log("ミッション ", "ミッション")
with c9:
    if st.button("確定役"): update_log("確定役 ", "確定役")
with c10:
    if st.button("⭕️"): update_log(" ⭕️ ", "⭕️")

# --- ④ 報酬 ---
st.subheader("④ 報酬")
reward_val = st.number_input("報酬枚数", min_value=0, step=10, value=0, key="reward")
c11, c12, c13 = st.columns(3)
with c11:
    if st.button("ばいん"): update_log(f"ばいん {reward_val}\n", f"ばいん({reward_val})")
with c12:
    if st.button("ぺろぺろ"): update_log(f"ぺろぺろ {reward_val}\n", f"ぺろぺろ({reward_val})")
with c13:
    if st.button("愛すぷ"): update_log(f"愛すぷ {reward_val}\n", f"愛すぷ({reward_val})")

# --- 出力エリア ---
st.divider()
st.subheader("出力結果")
st.text_area("メモ帳用テキスト", value=st.session_state.memo_log, height=300)

if st.button("履歴をすべてリセット"):
    st.session_state.memo_log = ""
    st.session_state.last_action = "リセット済み"
    st.query_params.clear() # URLをリセット
    st.rerun()

