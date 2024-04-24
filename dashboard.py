import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

data_day = pd.read_csv("data_day.csv")
data_hour = pd.read_csv("data_hour.csv")

st.title('Submission Dicoding Belajar Analisis Data dengan Python')
tab1, tab2, tab3 = st.tabs(["Perkenalan", "Pertanyan 1", "Pertanyaan 2"])
 
with tab1:
    st.header(" Halo!💃✨💫💥")
    st.subheader("Perkenalkan nama saya Idha. Ini adalah proyek streamlit pertama saya. Mohon harap maklum jika terdapat banyak kesalahan he..he..")

    st.write(
    """
    Email: idhakurniawati03@gmail.com \n
    ID Dicoding: idhakt
    """
    )
 
with tab2:
    st.header("Pertanyaan Pertama")
    st.subheader("Bagaimana performa rental Bike Sharing pada data_day terhadap pengaruh lingkungan dan musim?")
    st.markdown("\n**Berikut diagram performa rental Bike Sharing pada data_day**")

    # Konversi kolom 'dteday' menjadi tipe data datetime
    data_day['dteday'] = pd.to_datetime(data_day['dteday'])

    # Mengatur indeks DataFrame berdasarkan kolom 'dteday'
    data_day.set_index('dteday', inplace=True)

    # Menggambar plot jumlah pengguna sepanjang tahun
    plt.figure(figsize=(10, 6))
    plt.plot(data_day.index, data_day['cnt'], marker='o', linestyle='-')
    plt.title('Jumlah Pengguna Sepanjang Tahun')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
    with st.expander("Penjelasan"):
        st.write(
        """Berdasarkan grafik jumlah pengguna sepanjang tahun. Pada tahun 2012 user mengalami peningkatan yang sangat tinggi, bahkan paling tinggi dalam rentang waktu 2011 sampai dengan 2012. Walau begitu, pada tahun 2012 Bike-sharing rental juga mengalami penurunan paling rendah dalam rentang waktu 2011 sampai dengan 2012.
        """
        )

    col1, col2 = st.columns(2)
    with col1:
        numerical_features = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
        categorical_features = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']

        # Fitur kategorikal
        feature = st.selectbox("Pilih fitur kategorikal di bawah ini untuk melihat diagram :", categorical_features)

        # Hitung jumlah dan persentase
        count = data_day[feature].value_counts()
        percent = 100 * data_day[feature].value_counts(normalize=True)
        df = pd.DataFrame({'Jumlah sampel': count, 'Persentase': percent.round(1)})

        # Tampilkan dataframe
        st.write(df)
        #Tampilkan pie chart
        fig, ax = plt.subplots()
        count.plot(kind='pie', title=feature, autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)
        
        st.markdown("\n**Kesimpulan**")
        st.write(
            """
            Berdasarkan visualisasi data_day di atas peningkatan user terjadi pada musim gugur dengan cuaca cerah sedikit berawan. Pada saat liburan terjadi peningkatan yang sangat tinggi pada rental bike yaitu sebesar 3280.95%. User cenderung menggunakan rental bike di hari kerja. Hal ini menunjukkan, kemungkinan besar user adalah pekerja dan atau pelajar. Selain itu, Pengaruh suhu sangat mempengaruhi user menggunakan rental bike.
            """
            )

    with col2:
        st.markdown(
            """
            **Karakteristik Dataset** : 
            - instant: index
            - dteday : date
            - season : musim (1:musim semi, 2:musim panas, 3:musim gugur, 4:musim dingin)
            - yr : tahun (0: 2011, 1:2012)
            - mnth : month ( 1 to 12)
            - hr : jam (0 to 23)
            - holiday : hari libur atau tidak (di ekstrak dari http://dchr.dc.gov/page/holiday-schedule)
            - weekday : hari dalam seminggu
            - workingday : jika hari bukan akhir pekan atau hari libur adalah 1, sebaliknya adalah 0
            + weathersit : 
                - 1: Cerah, sedikit berawan, berawan
                - 2: Berkabut dan berawan, Berkabut dan sedikit berawan, berkabut, Berkabut dan sangat berawan
                - 3: Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan
                - 4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut
            - temp : Suhu normal dalam Celcius. Nilainya dibagi menjadi 41 (maks)
            - atemp: Suhu luar ruang dinormalisasi dalam Celcius. Nilainya dibagi 50 (maks)
            - hum: Kelembaban yang dinormalisasi. Nilainya dibagi menjadi 100 (maks)
            - windspeed: kecepatan angin yang dinormalisasi. Nilainya dibagi menjadi 67 (maks)
            - casual: jumlah pengguna biasa
            - registered: jumlah pengguna berlangganan
            - cnt: jumlah sepeda sewaan termasuk oleh pengguna biasa dan pengguna yang berlangganan
            """)
        

 
with tab3:
    st.header("Pertanyaan Kedua")
    st.subheader("Bagaimana performa rental Bike Sharing pada data_hour terhadap pengaruh lingkungan dan musim?")
    st.markdown("\n**Berikut diagram performa rental Bike Sharing pada data_hour**")

    col1, col2 = st.columns(2)
    with col1:
        numerical_features = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
        categorical_features = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']

        # Fitur kategorikal
        feature = st.selectbox("Pilih fitur kategorikal di bawah ini untuk melihat diagram :", categorical_features, key=hash("selectbox"))

        # Hitung jumlah dan persentase
        count = data_hour[feature].value_counts()
        percent = 100 * data_day[feature].value_counts(normalize=True)
        df = pd.DataFrame({'Jumlah sampel': count, 'Persentase': percent.round(1)})

        # Tampilkan dataframe
        st.write(df)
        #Tampilkan pie chart
        fig, ax = plt.subplots()
        count.plot(kind='pie', title=feature, autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)
        
        st.markdown("\n**Kesimpulan**")
        st.write(
            """
            Berdasarkan visualisasi data_hour di atas peningkatan user terjadi pada musim gugur dengan cuaca cerah sedikit berawan. Pada saat liburan terjadi peningkatan yang sangat tinggi pada rental bike yaitu sebesar 3275.8%. User cenderung menggunakan rental bike di hari kerja. Hal ini menunjukkan, kemungkinan besar user adalah pekerja dan atau pelajar. Selain itu, Pengaruh suhu sangat mempengaruhi user menggunakan rental bike.
            """
            )

    with col2:
        st.markdown(
            """
            **Karakteristik Dataset** : 
            - instant: index
            - dteday : date
            - season : musim (1:musim semi, 2:musim panas, 3:musim gugur, 4:musim dingin)
            - yr : tahun (0: 2011, 1:2012)
            - mnth : month ( 1 to 12)
            - hr : jam (0 to 23)
            - holiday : hari libur atau tidak (di ekstrak dari http://dchr.dc.gov/page/holiday-schedule)
            - weekday : hari dalam seminggu
            - workingday : jika hari bukan akhir pekan atau hari libur adalah 1, sebaliknya adalah 0
            + weathersit : 
                - 1: Cerah, sedikit berawan, berawan
                - 2: Berkabut dan berawan, Berkabut dan sedikit berawan, berkabut, Berkabut dan sangat berawan
                - 3: Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan
                - 4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut
            - temp : Suhu normal dalam Celcius. Nilainya dibagi menjadi 41 (maks)
            - atemp: Suhu luar ruang dinormalisasi dalam Celcius. Nilainya dibagi 50 (maks)
            - hum: Kelembaban yang dinormalisasi. Nilainya dibagi menjadi 100 (maks)
            - windspeed: kecepatan angin yang dinormalisasi. Nilainya dibagi menjadi 67 (maks)
            - casual: jumlah pengguna biasa
            - registered: jumlah pengguna berlangganan
            - cnt: jumlah sepeda sewaan termasuk oleh pengguna biasa dan pengguna yang berlangganan
            """)
        

 