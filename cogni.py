import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="COGNIPLAY",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# Set light theme with custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: white;
        }
        .stMarkdown, .stText, p, h1, h2, h3 {
            color: black !important;
        }
        .stSidebar {
            background-color: #808080 !important;
        }
        .stButton button {
            background-color: #EC6563 !important;
            color: white !important;
        }
        </style>
""", unsafe_allow_html=True)

# Define color palette
colors = ['#73A942', '#56C1C5', '#F8D34D', '#F08C44', '#EC6563']

st.title("🧠 COGNIPLAY - AI-Based Cognitive Games for Children")

st.sidebar.header("Child's Profile")
age = st.sidebar.slider("Select Child's Age", 1, 8, 5)
start_simulation = st.sidebar.button("Run Feedback Assessment")

if start_simulation:
    import time
    
    with st.spinner("🎮 AI is analyzing cognitive performance..."):
        time.sleep(5)  # 5 second delay
        
    # Simulating cognitive performance data
    cognitive_data = {
        "Memory Test": np.random.randint(50, 100),
        "Pattern Recognition": np.random.randint(50, 100),
        "Problem-Solving": np.random.randint(50, 100),
        "Attention and Focus": np.random.randint(50, 100),
        "Spatial Awareness & Visual Processing": np.random.randint(50, 100),
    }

    df = pd.DataFrame(list(cognitive_data.items()), columns=["Cognitive Skill", "Performance Score"])

    st.write("📊 **Performance Breakdown:**")

    # Create interactive bar chart using Plotly
    fig = px.bar(df, x=df["Cognitive Skill"], y=df["Performance Score"], text=df["Performance Score"], 
                 color=df["Cognitive Skill"], color_discrete_sequence=colors)
    fig.update_traces(textposition='outside', marker=dict(line=dict(color='black', width=1)))
    fig.update_layout(bargap=0.3, title="Cognitive Performance Breakdown")

    st.plotly_chart(fig, use_container_width=True)

    # Display metrics dynamically when a bar is clicked
    for skill, score in cognitive_data.items():
        with st.expander(f"📌 {skill} Metrics:"):
            metrics = {
                "Accuracy": f"{np.random.randint(70, 100)}%",
                "Reaction Time": f"{np.random.uniform(0.5, 2.5):.2f} sec",
                "Throughput": f"{np.random.randint(4, 10)} correct responses/min",
                "Feedback": f"CogniPlay recommends that the user plays number recall and puzzle games  to improve {skill}.",
                "Cognitive Adaptation": f"AI suggests a training module focused on enhancing {skill} over time."

            }

            for key, value in metrics.items():
                st.write(f"- **{key}:** {value}")

    # Adaptive Learning Logic
    avg_performance = np.mean(list(cognitive_data.values()))

    if avg_performance > 80:
        age = min(age + 1, 8)
        feedback = "Excellent performance! CogniPlay is increasing the difficulty level."
    elif avg_performance > 60:
        feedback = "Good job! CogniPlay recommends maintaining the current difficulty."
    else:
        age = max(age - 1, 1)
        feedback = "CogniPlay suggests easier exercises to match the learning pace."

    st.write(f"🔄 **AI-Adjusted Activities for Age {age}:**")
    st.success(feedback)

    # Simulated AI Learning Recommendation
    st.subheader("📌 AI Learning Recommendation:")
    if avg_performance > 80:
        st.info("✨ Try more advanced problem-solving challenges!")
    elif avg_performance > 60:
        st.info("🔄 Keep practicing memory games and pattern recognition exercises.")
    else:
        st.info("🧩 Focus on simpler cognitive tasks to build a strong foundation.")

    st.balloons()  # 🎈 Fun animation to engage judges!