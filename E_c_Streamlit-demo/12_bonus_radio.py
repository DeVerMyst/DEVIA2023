import streamlit as st

# Create an empty container
refresh_container = st.empty()

# Create a selectbox with dynamic options
selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected option
st.write("You selected:", selected_option)

# Modify the selectbox and trigger a refresh
if st.button("Refresh Selectbox"):
    selected_option = refresh_container.selectbox("Select an option", ["New Option 1", "New Option 2", "New Option 3"])


# import streamlit as st

# # Get the current state
# state = st.session_state

# # Create a selectbox with dynamic options
# selected_option = st.selectbox("Select an option", state.options)

# # Display the selected option
# st.write("You selected:", selected_option)

# # Modify the options list to trigger a refresh
# if st.button("Refresh Options"):
#     state.options = ["New Option 1", "New Option 2", "New Option 3"]
