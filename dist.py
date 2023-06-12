import streamlit as st
import scipy.stats as scipy
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

def main():

    st.title ("DISTRIBUSI NORMAL,EKSPONENSIAL DAN SIMPLE STATISTIC ")

    with st.sidebar:
        tipe = st.radio('Pilih tipe' , ['Dist_Normal' , 'Dist_Exponensial', 'Simple_Stat'])

    if tipe == 'Dist_Normal':
        
        st.write("## Woah Selamat Datang di Page Distribusi Normal, Saatnya Pilih Ekspetasi dan Sigma nya")

        x = np.linspace(-10, 10, 100)
        mu = st.slider('Pilih Ekspetasi', -10.0, 10.0, 0.0)

        sigma = st.slider('Pilih Sigma', 0.0, 5.0, 1.5)

        density_norm = scipy.norm(mu, sigma).pdf(x)

        fig, ax = plt.subplots()
        ax.plot(x, density_norm)
        st.pyplot(fig)

    if tipe == 'Dist_Exponensial':

        st.write("## Wow Ternyata Kamu Tertarik Sama Ekponensial Yaaa, Good Choice Saatnya  Pilih Lamda")

        lam = st.slider('Pilih Lamda', 0.0, 5.0)

        x = np.linspace(lam, 10, 100)

        dens_exp = scipy.expon(lam).pdf(x)

        fig, ax = plt.subplots()
        ax.plot(x, dens_exp)
        st.pyplot(fig)

    if tipe == 'Simple_Stat':    
            data = st.file_uploader("Upload Disini Yaw", type=["csv", "txt"])
            if data is not None:
                df = pd.read_csv(data)
                data_raw = df.copy()
                st.subheader("Perhitungan Deskriptif Data ")
                st.write(data_raw.describe())
                st.subheader("Korelasi Antar Data")
                st.write(df.corr())
        
if __name__ == '__main__':
    main()