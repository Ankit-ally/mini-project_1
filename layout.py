import streamlit as st
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt



data = {
'num':[x for x in range(1,11)],
'square':[x**2 for x in range(1,11)],
'twice':[x*2 for x in range(1,11)],
'thrice':[x*3 for x in range(1,11)],
}
df = pd.DataFrame(data)


st.sidebar.selectbox('select any number',df.columns)

fig,ax = plt.subplots()
ax.plot(df['num'],df['col'])

ax.set_title(f'plot of {'col'} vs num')
ax.set_xlabel('num')
ax.set_ylabel('col')

st.pyplot(fig)