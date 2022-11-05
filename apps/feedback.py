import streamlit as st
import pandas as pd
import csv

# ----------------------- FEEDBACK SECTION --------------------------
# This section accepts feedback from the user and their comments are
# displayed after submission

def app():
    st.title("Feedback")
    name = st.text_input('Name:')
    age = st.number_input('Age:', value=18)
    date = st.date_input('Today\'s Date')
    date_string = str(date)
    comment = st.text_area('Comment')
    submit = st.button("SUBMIT")

    commentsFileName = 'comments.csv'
    fields = ['NAME', 'AGE', 'COMMENT', 'DATE']
    user_Comment = [name , age, comment, date_string]

    with open(commentsFileName, 'w') as commentsFileName:
        csvwriter = csv.writer(commentsFileName)
        csvwriter.writerow(fields)
        csvwriter.writerow(user_Comment)

    if submit:
        comment_section_CSV = pd.read_csv('comments.csv', sep=',')
        comment_section_data = pd.DataFrame(comment_section_CSV)

        # Prints the comment section
        st.subheader("Comments:")
        df = pd.DataFrame(
           comment_section_data,
           columns = ['NAME', 'AGE', 'COMMENT', 'DATE']
        )
        st.success("Thank you for the feedback!")
        st.dataframe(df)



