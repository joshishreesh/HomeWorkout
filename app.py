import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Home Calisthenics Guide",
    page_icon="💪",
    layout="centered"
)

# --- CSS for better mobile/iPad viewing ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .exercise-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title & Intro ---
st.title("💪 Home Calisthenics Body Map")
st.write("Tap a muscle group below to see the best no-equipment exercises.")

# --- Exercise Data ---
# Note: YouTube links are used here for reliability. 
# You can replace these with local GIF paths if you have them.
exercises = {
    "Chest (Pectorals)": [
        {
            "name": "Standard Push-Up",
            "desc": "Keep your body in a straight line. Lower your chest to the floor and push back up.",
            "video": "https://www.youtube.com/watch?v=IODxDxX7oi4" 
        },
        {
            "name": "Wide Push-Up",
            "desc": "Place hands wider than shoulders to target the outer chest.",
            "video": "https://www.youtube.com/watch?v=rr6eFNNDQde"
        }
    ],
    "Back (Lats/Traps)": [
        {
            "name": "Doorway Rows",
            "desc": "Hold a door frame, lean back, and pull your chest towards the door using your back muscles.",
            "video": "https://www.youtube.com/watch?v=rloYp-vY8yQ"
        },
        {
            "name": "Superman Hold",
            "desc": "Lie on your stomach. Lift your arms and legs off the ground simultaneously. Hold.",
            "video": "https://www.youtube.com/watch?v=z6PJMT2y8GQ"
        }
    ],
    "Legs (Quads/Glutes)": [
        {
            "name": "Air Squats",
            "desc": "Feet shoulder-width apart. Lower your hips back and down as if sitting in a chair.",
            "video": "https://www.youtube.com/watch?v=rMVWQXhzDpo"
        },
        {
            "name": "Reverse Lunges",
            "desc": "Step backward with one leg, lowering your hips until both knees are at 90-degree angles.",
            "video": "https://www.youtube.com/watch?v=g8-CImHsfqc"
        }
    ],
    "Shoulders (Deltoids)": [
        {
            "name": "Pike Push-Up",
            "desc": "Get into a downward dog position. Lower your head toward the floor and push back up.",
            "video": "https://www.youtube.com/watch?v=sposDXWEB0A"
        }
    ],
    "Arms (Triceps/Biceps)": [
        {
            "name": "Chair Dips",
            "desc": "Use a sturdy chair. Lower your body by bending elbows, then push back up. Focus on triceps.",
            "video": "https://www.youtube.com/watch?v=0326dy_-CzM"
        },
        {
            "name": "Diamond Push-Up",
            "desc": "Hands together in a diamond shape under your chest. Great for triceps.",
            "video": "https://www.youtube.com/watch?v=J0DnG1_S92I"
        }
    ],
    "Abs (Core)": [
        {
            "name": "Plank",
            "desc": "Hold a push-up position on your elbows. Keep core tight and back straight.",
            "video": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
        },
        {
            "name": "Leg Raises",
            "desc": "Lie on back, lift legs straight up to 90 degrees, then lower slowly without touching the floor.",
            "video": "https://www.youtube.com/watch?v=JB2oyawG9KI"
        }
    ]
}

# --- Visual Selector (Grid Layout) ---
st.subheader("Select Target Area")

col1, col2 = st.columns(2)

selected_group = None

with col1:
    if st.button("Chest"):
        selected_group = "Chest (Pectorals)"
    if st.button("Back"):
        selected_group = "Back (Lats/Traps)"
    if st.button("Abs / Core"):
        selected_group = "Abs (Core)"

with col2:
    if st.button("Legs"):
        selected_group = "Legs (Quads/Glutes)"
    if st.button("Shoulders"):
        selected_group = "Shoulders (Deltoids)"
    if st.button("Arms"):
        selected_group = "Arms (Triceps/Biceps)"

# --- Display Area ---
st.markdown("---")

if selected_group:
    st.header(f"Workouts for: {selected_group}")
    
    current_exercises = exercises[selected_group]
    
    for ex in current_exercises:
        with st.container():
            st.subheader(ex['name'])
            st.write(f"**How to do it:** {ex['desc']}")
            # Embedding YouTube video. 
            # If you have local GIFs, use st.image("path/to/gif.gif") instead.
            st.video(ex['video'])
            st.markdown("---")
else:
    st.info("👆 Tap a body part above to see exercises!")
