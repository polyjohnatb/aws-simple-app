import streamlit as st
import pandas as pd

# css = (
#     "<style>section.main > div {max-width:"
#     + f"{80}"
#     + "rem}</style>"
# )
# st.html(css)

st.title('AWS Dog')

data = ('Health_AnimalBites.csv')
df = pd.read_csv(data)
df.drop(['BreedIDDesc', 'head_sent_date', 'release_date'], axis=1, inplace=True)
st.write(df)

# data_top = data.head()
# data_top

st.image('curious_dog.jpg', caption="'Live, laugh, love, AWS.' - AWS Dog")