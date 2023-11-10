import numpy as np
import pandas as pd
import streamlit as st

st.write("""
  # Проект выполнили:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("""
     ### Анастасия Можайская
    """)
    st.image('milyj-seryj-kotenok-vysunul-yazyk.jpg')

with col2:
    st.write("""
         ### Тигран Арутюнян
        """)
    st.image('malenkij-goluboglazyj-kotenok-na-trave.jpg')

with col3:
    st.write("""
         ###  Руслан Волощенко
        """)
    st.image('d352e721a066c97c757f.jpg')