import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
plt.style.use("fivethirtyeight")
st.set_option('deprecation.showPyplotGlobalUse', False)
from home import df

def main():
    st.title("The EDA Page")
    # Lets do Univariate Histograms 
    def histograms(data):
        df.hist()
        plt.tight_layout()
        st.pyplot()

    # Lets do side by side histplot adn boxplots 
    def histplot_boxplot(data, feature, figsize=(12,7), bins=None):
        fig, (ax_box, ax_hist)=plt.subplots(
        nrows=2,
        sharex=True,
        gridspec_kw={"height_ratios":(0.25, 0.75)},
        figsize=figsize )
        
        sns.boxplot(data=data, x=feature, showmeans=True, color="violet", ax=ax_box)
        sns.histplot(data=data, x=feature,pallete="winter", bins=bins, ax=ax_hist) if bins else sns.histplot(data=data,
                                                                        x=feature, ax=ax_hist)
        ax_hist.axvline(data[feature].mean(), linestyle="--", color="green")
        ax_hist.axvline(data[feature].median(), linestyle="-", color="black")
        st.pyplot()
    
    # univariate Countplot
    def countplot(data, feature):
        plt.figure(figsize=(12,7))
        ax=sns.countplot(data=data, x=feature, color="green")
        for p in ax.patches:
            x=p.get_bbox().get_points()[:,0]
            y=p.get_bbox().get_points()[1,1]
            ax.annotate("{:.3g}%".format(100.*y/len(data)), (x.mean(), y), ha="center", va="bottom")
        st.pyplot()

    st.subheader('Choose the Plot')
    plot=st.sidebar.selectbox("Choose The PLOT", ('histograms', 'histplot_boxplot', 'countplot'))
    if plot=='histograms':
        if st.sidebar.button("Plot graph"):
            histograms(df)

    if plot=='histplot_boxplot':
        if st.sidebar.button("Plot graph"):
            for col in  df.select_dtypes(exclude="O").columns:
                histplot_boxplot(data=df, feature=col)

    if plot=='countplot':
        if st.sidebar.button("Plot graph"):
            countplot(data=df, feature="Outcome")


if __name__=='__main__':
    main()