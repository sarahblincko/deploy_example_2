import streamlit as st

pg = st.navigation(
    [
        st.Page("homepage.py", title="Welcome"),
        st.Page("simulation_page.py", title="Clinic Simulation"),
        st.Page("lsoa_map_sb.py", title="LSOA Map")
    ]
)
pg.run()