import grequests
import streamlit as st
from typing import Any


def run() -> dict[int, Any]:
    rs = [grequests.get(f'https://httpbin.org/status/{code}') for code in range(200, 206)]
    data = {}
    for index, response in grequests.imap_enumerated(rs, size=5):
        data[index] = response
    return data 

if st.button("RUN"):
    data = run()
    st.write(data)


