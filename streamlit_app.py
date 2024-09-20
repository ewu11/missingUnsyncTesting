import streamlit as st
import pandas as pd

# File upload
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Display original data
    st.write("Original Data:")
    st.dataframe(df)

    # Perform some operations, e.g., adding a new column
    df['New Column'] = df['Existing Column'] * 2

    # Display processed data
    st.write("Processed Data:")
    st.dataframe(df)

    # Create a download button for the modified Excel file
    @st.cache_data
    def convert_df_to_excel(df):
        # Write DataFrame to Excel using pandas and save to a BytesIO buffer
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        return output.getvalue()

    processed_excel = convert_df_to_excel(df)
    st.download_button(
        label="Download Processed Excel",
        data=processed_excel,
        file_name="processed_file.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
