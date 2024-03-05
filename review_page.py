from scrapping import scrap,review_scrap,anime
import streamlit as st
import matplotlib.pyplot as plt
import time
from streamlit_lottie import st_lottie
import matplotlib
matplotlib.use('Qt5Agg')
import seaborn as sns
import pandas as pd




def show_keyword_page(pro1,pro2,keyword):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    try:
        data1=scrap(pro1)
        data2=scrap(pro2)
        rev_df1=review_scrap(data1['href'][0])
        rev_df2=review_scrap(data2['href'][0])
        avg_len=((len(rev_df1)+len(rev_df2))/2)
    except Exception as e:
        st.write(e)
    if keyword.lower()=="all":
        combined_df = pd.concat([rev_df1['Rating'].value_counts(), rev_df2['Rating'].value_counts()], axis=1)
        combined_df.columns = [f'{pro1.upper()} Ratings', f'{pro2.upper()} Ratings']
        combined_df = combined_df.reset_index().rename(columns={'index': 'Rating'})
        st.write(combined_df)
        melted_df = combined_df.melt(id_vars='Rating', var_name='Product', value_name='Count')

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.style.use('fivethirtyeight')
        sns.barplot(x='Rating', y='Count', hue='Product', data=melted_df)
        plt.title('Ratings for {}'.format(keyword.upper()))
        plt.ylabel('Count')
        plt.xlabel('Rating')
        plt.xticks(rotation=0)

        # Display plot in Streamlit
        st.pyplot()
    else:
        filtered_df1 = rev_df1[rev_df1['Review'].str.lower().str.contains(keyword.lower())]
        filtered_df2 = rev_df1[rev_df2['Review'].str.lower().str.contains(keyword.lower())]  
        combined_df = pd.concat([filtered_df1['Rating'].value_counts(), filtered_df2['Rating'].value_counts()], axis=1)
        combined_df.columns = [f'{pro1.upper()} Ratings', f'{pro2.upper()} Ratings']
        combined_df = combined_df.reset_index().rename(columns={'index': 'Rating'})
        st.write(combined_df)

        # Melt dataframe for seaborn plot
        melted_df = combined_df.melt(id_vars='Rating', var_name='Product', value_name='Count')

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.style.use('fivethirtyeight')
        sns.barplot(x='Rating', y='Count', hue='Product', data=melted_df)
        plt.title('Ratings for {}'.format(keyword.upper()))
        plt.ylabel('Count')
        plt.xlabel('Rating')
        plt.xticks(rotation=0)

        # Display plot in Streamlit
        st.pyplot()
        if st.button('Want to See Reviews??'):
            st.header('Reviews on {} of {}'.format(keyword.capitalize(),pro1.title()))
            st.write(filtered_df1)
            st.header('Reviews on {} of {}'.format(keyword.capitalize(),pro2.title()))
            st.write(filtered_df2)


        