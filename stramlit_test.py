import streamlit as st
from datetime import datetime

def rental_information():
    st.title("Socar So good")

    # 대여 정보 입력
    st.header("대여 정보")
    rental_date = st.date_input("대여 날짜", min_value=datetime.today())
    rental_time = st.time_input("대여 시작 시간")

    # 반납 정보 입력
    st.header("반납 정보")
    return_date = st.date_input("반납 날짜", min_value=rental_date)
    return_time = st.time_input("반납 시간")

    # 여행 기간 입력
    st.header("여행 기간")
    trip_duration_options = ["당일여행", "1박2일", "2박3일"]
    trip_duration = st.selectbox("여행 기간을 선택하세요", trip_duration_options)

    # 여행 테마 입력
    st.header("여행 테마")
    travel_theme_options = ["산", "바다", "실내여행지", "액티비티", "문화와역사", "테마마크"]
    travel_theme = st.selectbox("여행 테마를 선택하세요", travel_theme_options)

    # 입력된 정보 출력
    st.header("입력된 정보")
    st.write(f"대여 날짜: {rental_date}")
    st.write(f"대여 시작 시간: {rental_time}")
    st.write(f"반납 날짜: {return_date}")
    st.write(f"반납 시간: {return_time}")
    st.write(f"여행 기간: {trip_duration}")
    st.write(f"여행 테마: {travel_theme}")

if __name__ == "__main__":
    rental_information()