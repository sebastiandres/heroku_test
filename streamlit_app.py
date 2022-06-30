import streamlit as st
import numpy as np
import pandas as pd

st.markdown("This is where you put your **private** content.")

st.subheader("Maybe some data")
st.markdown("Some data that you want to share with your collaborators but needs to remain private.")
N = 5
df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
st.dataframe(df)  # Same as st.write(df)

st.subheader("Maybe some plots")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader("Maybe cat pictures")
st.image("https://cataas.com/cat/cute")