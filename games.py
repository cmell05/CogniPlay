import streamlit as st
import random
import time

# Initialize game state
if "board" not in st.session_state:
    emojis = ["🍎", "🍌", "🍉", "🍇", "🍒", "🥕", "🌽", "🍕"] * 2  # Pairs of emojis
    random.shuffle(emojis)
    st.session_state.board = emojis
    st.session_state.revealed = [False] * 16  # False = Hidden, True = Revealed
    st.session_state.selected = []  # Track selected cards
    st.session_state.matched = set()  # Store matched indices
    st.session_state.lock = False  # Prevent multiple selections at once

# Game title
st.title("🃏 Match the Pairs Game")

# Display instructions
st.markdown("""
### How to Play:
1. Click on a card to reveal the fruit.
2. Try to find a matching pair.
3. If two cards **match**, they stay revealed.
4. If they **don’t match**, they close again after **1 second**.
5. Match all pairs to win!
""")

# Display cards as buttons
cols = st.columns(4)
for i in range(16):
    col = cols[i % 4]
    if st.session_state.revealed[i] or i in st.session_state.matched:
        col.button(st.session_state.board[i], key=f"card_{i}", disabled=True)
    else:
        if col.button("❓", key=f"card_{i}") and not st.session_state.lock:
            st.session_state.selected.append(i)
            st.session_state.revealed[i] = True

# Check for matches (after two cards are selected)
if len(st.session_state.selected) == 2:
    idx1, idx2 = st.session_state.selected
    st.session_state.lock = True  # Prevent more selections

    if st.session_state.board[idx1] == st.session_state.board[idx2]:  # If they match
        st.session_state.matched.add(idx1)
        st.session_state.matched.add(idx2)
    else:
        time.sleep(1)  # **Cards disappear after 1 second**
        st.session_state.revealed[idx1] = False
        st.session_state.revealed[idx2] = False

    st.session_state.selected = []  # Reset selection
    st.session_state.lock = False  # Unlock selections
    st.rerun()  # **Forces UI update**

# Win condition
if len(st.session_state.matched) == 16:
    st.success("🎉 Congratulations! You found all pairs!")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.clear()  # **Fully resets the game state**
    st.rerun()
