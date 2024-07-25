import streamlit as st
import pandas as pd

# css = (
#     "<style>section.main > div {max-width:"
#     + f"{80}"
#     + "rem}</style>"
# )
# st.html(css)

st.title('AWS Dog')

data = 'https://aws-bucket1-polyjb.s3.amazonaws.com/Health_AnimalBites.csv'
df = pd.read_csv(data)
df.drop(['BreedIDDesc', 'head_sent_date', 'release_date'], axis=1, inplace=True)
st.write(df)

# data_top = data.head()
# data_top

object_url = 'https://aws-bucket1-polyjb.s3.amazonaws.com/curious_dog.jpg'
st.image(object_url, caption="'Live, laugh, love, AWS.' - AWS Dog")
