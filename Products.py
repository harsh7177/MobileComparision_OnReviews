import streamlit as st
import pickle
import numpy as np
from scrapping import scrap,review_scrap,anime
from explore_page import show_explore_page
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO
import textwrap


plt.style.use('ggplot')

def show_predict_page(pro1,pro2):
    if len(pro1) > 0 and len(pro2)>0:     
        try:
            data1 = scrap(pro1)
            data2 = scrap(pro2)
            data=pd.concat([data1.head(2), data2.head(2)], ignore_index=True)
            if isinstance(data1, pd.DataFrame) and isinstance(data2, pd.DataFrame):
               
                st.markdown(
    """
    <div style="background-color:#ff7e5f;padding:10px;border-radius:10px;box-shadow:2px 2px 4px rgba(0,0,0,0.5);">
        <h1 style="color:#ffffff;font-size:36px;text-shadow:2px 2px 4px rgba(0,0,0,0.5);padding:10px;">
            Device Properties
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)
                for i in range(0, len(data['Variant']), 2):
                    col1, col2 = st.columns(2)
                    col1.write(":red[{}]".format(data['Variant'][i]))
                    details1 = data['Details'][i]
                    formatted_details1 = "<br>".join([f'<span class="star-bullet"></span> {item.strip()}' for item in details1])
                    st.markdown(
                                    """
                                    <style>
                                    .star-bullet::before {
                                        content: "\u2605";
                                        color: goldenrod; /* Change color to golden */
                                        margin-right: 5px; /* Add some spacing between bullet and text */
                                    }
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                                )
                    col1.markdown(formatted_details1, unsafe_allow_html=True)

                    if i + 1 < len(data['Variant']):
                        col2.write(":red[{}]".format(data['Variant'][i+1]))
                        details2 = data['Details'][i + 1]
                        formatted_details2 = "<br>".join([f'<span class="star-bullet"></span> {item.strip()}' for item in details2])
                        st.markdown(
                                            """
                                            <style>
                                            .star-bullet::before {
                                                content: "\u2605";
                                                color: goldenrod; /* Change color to golden */
                                                margin-right: 5px; /* Add some spacing between bullet and text */
                                            }
                                            </style>
                                            """,
                                            unsafe_allow_html=True
                                        )
                        col2.markdown(formatted_details2, unsafe_allow_html=True)
                        st.divider()

                   

                x_values_wrapped = [textwrap.fill(label, width=10) for label in data['Variant']]
                y_values = [int(price) for price in data['Price']]
                plt.bar(x_values_wrapped,y_values)
                plt.gcf().set_size_inches(10,6)
                plt.title('Item Variants Prices')
                st.pyplot(plt)
                
            else:
                st.write("Data returned by scrap function is not a DataFrame.")
        except Exception as e:
            st.write(e)
