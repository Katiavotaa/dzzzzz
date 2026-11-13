import streamlit as st

st.set_page_config(page_title="Мій додаток!", page_icon="📖", layout="wide")

st.title("Рада бачити тебе в моєму додатку!")

tab1, tab2, tab3 = st.tabs(["про мене", "Мій інструмент", "Корисні посилання"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://www.freeiconspng.com/uploads/funny-icon-11.png", width=250)
    with col2:
        st.subheader("Привіт, мене звати Катя!")
        st.write("Я навчаюсь в комп'ютерній академії IT STEP.")

        with st.container():
            st.info("Мої контакти")
            st.markdown("- phone number: [ +380 73 661 02 54]")
            st.markdown("- E-Mail: [ masenko@gmail.com]")

with tab2:
    st.info("У процесі розробки")

with tab3:
    st.header("Мої корисні посилання")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Навчання")
        st.markdown("[Khan Academy](https://www.khanacademy.org/)")
        st.markdown("[GeoGebra](https://www.geogebra.org/)")

    with col2:
        st.subheader("Практика")
        st.markdown("[Duolingo](https://www.duolingo.com/)")
        st.markdown("[Scratch](https://scratch.mit.edu/)")