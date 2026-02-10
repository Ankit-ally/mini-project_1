import streamlit as st
import pandas as pd
import numpy as np

import  matplotlib.pyplot as plt
import altair as alt




st.title("Title")

data = pd.DataFrame(
    np.random.rand(100,3),
    columns=['A','B','C']
)

#st.write(data)

# st.line_chart(data)

# st.line_chart(data,y=["A"])

# st.area_chart(data)
# st.area_chart(data,y=["B"])

# st.bar_chart(data)

# fig,ax = plt.subplots()
# ax.scatter(data['A'],data['B'])
# st.pyplot(fig)


# chart= alt.Chart(data).mark_circle().encode(x='A',y= 'B')
# st.altair_chart(chart,use_container_width= True)

# st.graphviz_chart("""
# digraph{
#     watch -> like 
#     like -> share
#     share -> subscribe
#     subscribe -> channel 
                  
#                   }

# """              )

data=pd.DataFrame({
    'lat':[33.7749, 40.7128 , 34.0522,41.8781,47.6062],
    'log':[-122.4194, -74.0060, -118.2437,-122.3327]
})
st.map(data)
