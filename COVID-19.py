# COVID-19 DATA ANALYSIS USING STREAMLIT

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="COVID-19 Data Analysis", page_icon="🦠", layout="wide")

st.title("🦠 COVID-19 Data Analysis")
st.write("Enter COVID-19 data for different countries and analyze it.")

class CovidAnalysis:

    def __init__(self):
        self.country = []
        self.cases = []
        self.recoveries = []
        self.deaths = []

    def get_data(self):
        n = st.number_input(
            "Enter Number of Countries",
            min_value=1,
            step=1
        )

        for i in range(int(n)):
            st.subheader(f"Country {i+1}")

            self.country.append(
                st.text_input(
                    f"Country Name {i+1}",
                    key=f"country{i}"
                )
            )

            self.cases.append(
                st.number_input(
                    f"Cases {i+1}",
                    min_value=0,
                    step=1,
                    key=f"case{i}"
                )
            )

            self.recoveries.append(
                st.number_input(
                    f"Recoveries {i+1}",
                    min_value=0,
                    step=1,
                    key=f"recovery{i}"
                )
            )

            self.deaths.append(
                st.number_input(
                    f"Deaths {i+1}",
                    min_value=0,
                    step=1,
                    key=f"death{i}"
                )
            )

    def create_dataframe(self):

        self.df = pd.DataFrame({
            "Country": self.country,
            "Cases": self.cases,
            "Recoveries": self.recoveries,
            "Deaths": self.deaths
        })

    def analysis(self):

        total_cases = np.sum(self.df["Cases"])
        total_recoveries = np.sum(self.df["Recoveries"])
        total_deaths = np.sum(self.df["Deaths"])

        average_cases = np.mean(self.df["Cases"])

        highest_country = self.df.loc[
            self.df["Cases"].idxmax(),
            "Country"
        ]

        lowest_country = self.df.loc[
            self.df["Cases"].idxmin(),
            "Country"
        ]

        st.success("Analysis Completed")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Cases", total_cases)
        col2.metric("Total Recoveries", total_recoveries)
        col3.metric("Total Deaths", total_deaths)

        st.metric("Average Cases", round(average_cases, 2))

        st.write("### Highest Cases Country")
        st.info(highest_country)

        st.write("### Lowest Cases Country")
        st.info(lowest_country)

        st.write("### Data Table")
        st.dataframe(self.df)

    def graph(self):

        fig, ax = plt.subplots(figsize=(8,5))

        ax.bar(self.df["Country"], self.df["Cases"])

        ax.set_title("COVID-19 Cases by Country")
        ax.set_xlabel("Country")
        ax.set_ylabel("Cases")

        st.pyplot(fig)


obj = CovidAnalysis()

obj.get_data()

if st.button("Analyze Data"):

    obj.create_dataframe()

    obj.analysis()

    obj.graph()