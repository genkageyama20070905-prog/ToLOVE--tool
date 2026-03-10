import streamlit as st

st.set_page_config(page_title="メモ", layout="centered")

# --- 1. URLから履歴を復元する処理 ---
# ページ読み込み時にURLパラメータ "log" をチェックする
query_params = st.query_params
if "log" in query_params and 'memo_log' not in st.session_state:
    st.session_state.memo_log = query_params["log"]

# セッション状態の初期化
if 'memo_log' not in st.session_state:
    st.session_state.memo_log = ""
if 'last_action' not in st.session_state:
    st.session_state.last_action = "なし"

# --- 2. 共通の保存・更新関数 ---
def update_and_save(text, action):
    st.session_state.memo_log += text
    st.session_state.last_action = action
    # URLに履歴を書き込む（これでリロードしても消えない）
    st.query_params["log"] = st.session_state.memo_log

st.title("メモ")
# --- 画面中央・右寄りに現在の入力を固定表示する設定 ---
latest_line = st.session_state.memo_log.split('\n')[-1] if st.session_state.memo_log else "なし"

st.markdown(f"""
    <style>
    .floating-box {{
        position: fixed;
        top: 50%;         /* 画面の中央（縦） */
        right: 10px;      /* 右端から10px */
        transform: translateY(-50%); /* 中央にぴったり合わせる */
        width: 120px;     /* 幅（お好みで調整） */
        background-color: rgba(255, 255, 255, 0.9); /* 半透明の白 */
        border: 2px solid #333;
        border-radius: 10px;
        padding: 10px;
        z-index: 1000;
        font-size: 14px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        word-wrap: break-word; /* 長い時に折り返す */
    }}
    </style>
    <div class="floating-box">
        <span style="font-size: 10px; color: #666;">現在の行:</span><br>
        {latest_line}
    </div>
    """, unsafe_allow_index=True)

# --- 直前の操作を表示 ---
st.info(f"💡 最後に押したボタン: **{st.session_state.last_action}**")

# --- ① 当選ゲーム数 ---
st.subheader("① 当選ゲーム数")
game_input = st.number_input("ゲーム数", min_value=0, step=1, value=0, key="game")
if st.button("🔢 ゲーム数を出力"):
    update_and_save(f"\n{game_input} ", f"ゲーム数({game_input})")

# --- ② 当選契機 ---
st.subheader("② 当選契機")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("バルーン"): update_and_save("バルーン\n", "バルーン")
with c2:
    if st.button("スイート"): update_and_save("スイート\n", "スイート")
with c3:
    if st.button("ぷっちゅん"): update_and_save("ぷっちゅん\n", "ぷっちゅん")
with c4:
    if st.button("追憶"): update_and_save("追憶\n", "追憶")

# --- ③ ST小役 ---
st.subheader("③ 小役・対応")
c5, c6, c7, c8, c9, c10 = st.columns(6)
with c5:
    if st.button("🔔"): update_and_save("🔔", "🔔")
with c6:
    if st.button("非対応"): update_and_save("非対応 ", "非対応")
with c7:
    if st.button("対応"): update_and_save("対応 ", "対応")
with c8:
    if st.button("ミッション"): update_and_save("ミッション ", "ミッション")
with c9:
    if st.button("確定役"): update_and_save("確定役 ", "確定役")
with c10:
    if st.button("⭕️"): update_and_save(" ⭕️ ", "⭕️")

# --- ④ 報酬 ---
st.subheader("④ 報酬")
reward_val = st.number_input("報酬枚数", min_value=0, step=10, value=0, key="reward")
c11, c12, c13 = st.columns(3)
with c11:
    if st.button("ばいん"): update_and_save(f"ばいん {reward_val}\n", f"ばいん({reward_val})")
with c12:
    if st.button("ぺろぺろ"): update_and_save(f"ぺろぺろ {reward_val}\n", f"ぺろぺろ({reward_val})")
with c13:
    if st.button("愛すぷ"): update_and_save(f"愛すぷ {reward_val}\n", f"愛すぷ({reward_val})")

# --- 出力エリア ---
st.divider()
st.subheader("出力結果")
st.text_area("メモ帳用テキスト", value=st.session_state.memo_log, height=300)

# --- 3. クリップボードコピー（iPhone対応版） ---
import streamlit.components.v1 as components
if st.button("📋 履歴をコピー"):
    # JSで安全にコピー
    components.html(f"""
        <script>
        const text = `{st.session_state.memo_log}`;
        const el = window.parent.document.createElement('textarea');
        el.value = text;
        window.parent.document.body.appendChild(el);
        el.select();
        window.parent.document.execCommand('copy');
        window.parent.document.body.removeChild(el);
        alert("コピーしました！");
        </script>
    """, height=0)

if st.button("履歴をすべてリセット"):
    st.session_state.memo_log = ""
    st.session_state.last_action = "リセット済み"
    st.query_params.clear() # URLをきれいにする
    st.rerun()
