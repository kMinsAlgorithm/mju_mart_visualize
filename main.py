import streamlit as st
import pandas as pd
import numpy as np
import datetime

from mocking_data import get_mocking_data

chart_data = get_mocking_data()


def main():
    st.title("명지 마트 재고 현황")
    st.write("301개 품목에 대한 재고 현황을 보여줍니다.")

    multiselect = st.multiselect("Choose Item", (i for i in range(1, 302)))
    how_long = st.number_input(
        "How long?", min_value=10, max_value=100, value=20, step=1
    )

    filtered_data = chart_data[list(map(lambda x: str(x), multiselect))]

    if multiselect:
        line_chart = st.line_chart(filtered_data[:how_long])
    else:
        line_chart = st.line_chart(chart_data[:how_long])

    # 마지막 timestamp와 재고량 출력
    st.write("마지막 시간과 재고량")
    # last_timestamp = chart_data.index[-1]
    # last_values = chart_data.loc[last_timestamp].to_dict()
    # for col, value in last_values.items():
    #     st.write(f"{col}: {value} @ {last_timestamp}")

    st.dataframe(chart_data)


if __name__ == "__main__":
    main()
