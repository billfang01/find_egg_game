
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="荷包蛋製作遊戲", layout="centered")

st.title("🍳 請點選正確的步驟圖卡：")

# 步驟對應標題
steps = [
    "步驟一 放鍋子",
    "步驟二 開火",
    "步驟三 放油",
    "步驟四 將蛋放到平底鍋",
    "步驟五 將蛋翻面",
    "步驟六 關火",
    "步驟七 荷包蛋放到盤子"
]

# 圖片載入
image_files = [f"images/step{i+1}.png" for i in range(7)]

# 顯示圖片與標籤
for i in range(7):
    with st.container():
        st.image(image_files[i], use_column_width=True)
        st.markdown(f"**{steps[i]}**")

# 重新開始按鈕
if st.button("🔁 重新開始"):
    st.experimental_rerun()
