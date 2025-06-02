
import streamlit as st
from PIL import Image
import os


st.set_page_config(page_title="荷包蛋製作遊戲", layout="centered")
st.title("🔍 請依順序完成每個步驟配對")

# 7 個步驟文字與圖片
steps = [
    "放鍋子", 
    "開火", 
    "放油", 
    "將蛋放到平底鍋", 
    "將蛋翻面", 
    "關火", 
    "荷包蛋放到盤子"
]

image_paths = [
    "images/step1.png",
    "images/step2.png",
    "images/step3.png",
    "images/step4.png",
    "images/step5.png",
    "images/step6.png",
    "images/step7.png"
]

# 建立 session state 追蹤遊戲狀態
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "matched" not in st.session_state:
    st.session_state.matched = [False] * 7
if "pending" not in st.session_state:
    st.session_state.pending = None

st.subheader(f"請點選對應圖片：**步驟 {st.session_state.current_step+1} — {steps[st.session_state.current_step]}**")

# 按鈕：點選步驟文字（左上）
st.write("### 選這個")
if st.button("👉 " + steps[st.session_state.current_step]):
    st.session_state.pending = st.session_state.current_step

st.divider()

# 顯示所有圖片與步驟說明卡片
cols = st.columns(3)
for i in range(7):
    with cols[i % 3]:
        st.image(image_paths[i], use_container_width=True)
        if st.button(f"選擇 {steps[i]}", key=f"img{i}"):
            if st.session_state.pending == i:
                st.session_state.matched[i] = True
                st.session_state.current_step += 1
                st.session_state.pending = None
            else:
                st.warning("❌ 圖片與步驟不符，請再試一次")

# 結束畫面
if all(st.session_state.matched):
    st.success("🎉 全部完成！荷包蛋完成啦～")

# 重新開始按鈕
if st.button("🔁 重新開始"):
    st.session_state.current_step = 0
    st.session_state.matched = [False] * 7
    st.session_state.pending = None
    st.rerun()
