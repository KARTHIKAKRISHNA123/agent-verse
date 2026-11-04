import streamlit as st
from youtube_analyzer import build_youtube_agent

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """

st.set_page_config(
    page_title=" ▶️ TubeLens - YouTube Video Analyzer",
    layout="centered"
)
st.title(" ▶️ TubeLens - YouTube Video Analyzer")


# import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df


# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

st.write("Hello, welcome to TubeLens - YouTube Video Analyzer! This app allows you to analyze YouTube videos and extract valuable insights from them. Please enter the URL of the YouTube video you want to analyze below.")

# st.title(" ▶️ YouTube Video Analyzer")


# Cache - fast and temporary storage of the agent object, fast access temporary storage => Most frequently accessed data is stored in cache for faster access. Cache is temporary storage, and it is cleared when the app is restarted or when the cache is cleared manually.
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# input Box for YouTube video URL
video_url = st.text_input("Enter the YouTube video URL:", "") # str

button = st.button("Analyze Video") # True / False

print("Video URL:", video_url)
print("Analyze Button:", button)

if button and video_url:
    with st.spinner("Analyzing the video..."):
        response =agent.run(
            f"Analyze this video: {video_url}",

        )

    st.markdown("### Analysis Result Of The Video:")

    st.markdown(response.content)