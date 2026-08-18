import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

query_sql = st.text_area(
    label="Entrez la requête",
    value=""
)


result = duckdb.sql(query_sql).df()

st.write(query_sql)
st.dataframe(result)