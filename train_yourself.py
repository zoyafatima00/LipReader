import streamlit as st

def display_train_yourself():
    st.markdown('<div class="title">Train Yourself</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Use the IPA chart below to train yourself on American English phonemes.</div>', unsafe_allow_html=True)
    st.markdown("""
    <a title="American IPA chart with sounds and examples" href="https://americanipachart.com">
    <object type="image/svg+xml" data="https://americanipachart.s3.amazonaws.com/american-IPA-chart-english.svg" style="width: 770px;">
    American IPA chart (IPA chart for General American)<br>
    <img width="770" height="5219" src="https://americanipachart.s3.amazonaws.com/american-IPA-chart-english.png" alt="American IPA chart">
    </object></a>
    """, unsafe_allow_html=True)
    st.markdown("""
    ### About the IPA Chart
    The International Phonetic Alphabet (IPA) is an alphabetic system of phonetic notation based primarily on the Latin alphabet. It was devised by the International Phonetic Association as a standardized representation of the sounds of spoken language. The IPA is used by linguists, speech-language pathologists, singers, actors, lexicographers, and translators.

    ### How to Use the IPA Chart
    Click on any symbol in the chart to hear the corresponding sound. Practice making the sounds yourself by mimicking the audio. The chart includes all the sounds used in American English.
    """)

