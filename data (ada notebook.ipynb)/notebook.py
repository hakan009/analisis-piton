# %% [markdown]
# # Proyek Analisis Data: Air-quality-dataset
# 
# - Nama: Hakan Alif Pramudya
# - Email: hakanalifpramudya13@gmail.com
# - Id Dicoding: hakanalifp

# %% [markdown]
# ## Menentukan Pertanyaan Bisnis

# %% [markdown]
# - Bagaimana level polusi dan hubungan CO ?
# - Bagaimana konsentrasi rata-rata PM2.5 bervariasi kumpulan data ? 

# %% [markdown]
# ## Menyiapkan semua library yang dibuthkan

# %%
# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# 

# %% [markdown]
# ## Data Wrangling

# %% [markdown]
# ### Gathering Data

# %% [markdown]
# ### Memuat tabel changping

# %%
# Membaca data dari file CSV ke dalam DataFrame
changping_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
changping_df.head()

# %% [markdown]
# ### Memuat tabel dingling

# %%
# Membaca data dari file CSV ke dalam DataFrame
dingling_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
dingling_df.head()

# %% [markdown]
# ### Memuat tabel dongsi

# %%
# Membaca data dari file CSV ke dalam DataFrame
dongsi_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
dongsi_df.head()

# %% [markdown]
# ### Memuat tabel guanyuan

# %%
# Membaca data dari file CSV ke dalam DataFrame
guanyuan_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
guanyuan_df.head()

# %% [markdown]
# ### Memuat tabel gucheng

# %%
# Membaca data dari file CSV ke dalam DataFrame
gucheng_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
gucheng_df.head()

# %% [markdown]
# ### Memuat tabel huairou

# %%
# Membaca data dari file CSV ke dalam DataFrame
huairou_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
huairou_df.head()

# %% [markdown]
# ### Memuat tabel nongzhanguan

# %%
# Membaca data dari file CSV ke dalam DataFrame
nongzhanguan_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
nongzhanguan_df.head()

# %% [markdown]
# ### Memuat tabel shunyi

# %%
# Membaca data dari file CSV ke dalam DataFrame
shunyi_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
shunyi_df.head()

# %% [markdown]
# ### Memuat tabel tiantan

# %%
# Membaca data dari file CSV ke dalam DataFrame
tiantan_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
tiantan_df.head()

# %% [markdown]
# ### Memuat tabel wanliu

# %%
# Membaca data dari file CSV ke dalam DataFrame
wanliu_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
wanliu_df.head()

# %% [markdown]
# ### Memuat tabel wanshouxigong

# %%
# Membaca data dari file CSV ke dalam DataFrame
wanshouxigong_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
wanshouxigong_df.head()

# %% [markdown]
# ### Memuat tabel aotizhongxin

# %%
# Membaca data dari file CSV ke dalam DataFrame
aotizhongxin_df = pd.read_csv("https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")

# Menampilkan lima baris pertama dari DataFrame
aotizhongxin_df.head()

# %% [markdown]
# ### Assessing Data

# %% [markdown]
# ### Menilai Data changping_df

# %%
# Menampilkan informasi tentang struktur DataFrame changping_df
changping_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
changping_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", changping_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
changping_df.describe()

# %% [markdown]
# ### Menilai Data dingling_df

# %%
# Menampilkan informasi tentang struktur DataFrame dingling_df
dingling_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
dingling_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", dingling_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
changping_df.describe()

# %% [markdown]
# ### Menilai Data dongsi_df

# %%
# Menampilkan informasi tentang struktur DataFrame dongsi_df
dongsi_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
dongsi_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", dongsi_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
dongsi_df.describe()

# %% [markdown]
# ### Menilai Data guanyuan_df

# %%
# Menampilkan informasi tentang struktur DataFrame guanyuan_df
guanyuan_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
guanyuan_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", guanyuan_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
guanyuan_df.describe()

# %% [markdown]
# ### Menilai Data gucheng_df

# %%
# Menampilkan informasi tentang struktur DataFrame gucheng_df
gucheng_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
gucheng_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", gucheng_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
gucheng_df.describe()

# %% [markdown]
# ### Menilai Data huairou_df
# 

# %%
# Menampilkan informasi tentang struktur DataFrame huairou_df
huairou_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
huairou_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", huairou_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
huairou_df.describe()

# %% [markdown]
# ### Menilai Data nongzhanguan_df
# 

# %%
# Menampilkan informasi tentang struktur DataFrame nongzhanguan_df
nongzhanguan_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
nongzhanguan_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", nongzhanguan_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
nongzhanguan_df.describe()

# %% [markdown]
# ### Menilai Data shunyi_df
# 

# %%
# Menampilkan informasi tentang struktur DataFrame shunyi_df
shunyi_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
shunyi_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", shunyi_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
shunyi_df.describe()

# %% [markdown]
# ### Menilai Data tiantan_df
# 

# %%
# Menampilkan informasi tentang struktur DataFrame tiantan_df
tiantan_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
tiantan_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", tiantan_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
tiantan_df.describe()

# %% [markdown]
# ### Menilai Data wanliu_df
# 

# %%
# Menampilkan informasi tentang struktur DataFrame wanliu_df
wanliu_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
wanliu_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", wanliu_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
wanliu_df.describe()

# %% [markdown]
# ### Menilai Data wanshouxigong_df

# %%
# Menampilkan informasi tentang struktur DataFrame wanshouxigong_df
wanshouxigong_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
wanshouxigong_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", wanshouxigong_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
wanshouxigong_df.describe()

# %% [markdown]
# ### Menilai Data aotizhongxin_df

# %%
# Menampilkan informasi tentang struktur DataFrame aotizhongxin_df
aotizhongxin_df.info()

# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
aotizhongxin_df.isna().sum()

# %%
# Menampilkan jumlah baris yang merupakan duplikasi dalam DataFrame
print("Jumlah duplikasi: ", aotizhongxin_df.duplicated().sum())

# %%
# Menampilkan ringkasan statistik dari DataFrame
aotizhongxin_df.describe()

# %% [markdown]
# ### Cleaning Data

# %% [markdown]
# ### Membersihkan Data changping_df

# %% [markdown]
# #### Mengatasi Outlier changping_df

# %%
# Outlier PM2.5
Q1_pm25 = changping_df['PM2.5'].quantile(0.25)
Q3_pm25 = changping_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = changping_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = changping_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
changping_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = changping_df['PM10'].quantile(0.25)
Q3_pm10 = changping_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = changping_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = changping_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
changping_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = changping_df['SO2'].quantile(0.25)
Q3_so2 = changping_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = changping_df['SO2'] < minimum_so2
kondisi_more_than_so2 = changping_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
changping_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = changping_df['NO2'].quantile(0.25)
Q3_no2 = changping_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = changping_df['NO2'] < minimum_no2
kondisi_more_than_no2 = changping_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
changping_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

changping_df['NO2'] = pd.to_numeric(changping_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = changping_df['CO'].quantile(0.25)
Q3_co = changping_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = changping_df['CO'] < minimum_co
kondisi_more_than_co = changping_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
changping_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = changping_df['O3'].quantile(0.25)
Q3_o3 = changping_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = changping_df['O3'] < minimum_o3
kondisi_more_than_o3 = changping_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
changping_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
changping_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
changping_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value changping_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
changping_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
changping_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
changping_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
changping_df['NO2'] = pd.to_numeric(changping_df['NO2'], errors='coerce')
changping_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
changping_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
changping_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = changping_df['TEMP'].mean()
changping_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = changping_df['PRES'].mean()
changping_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = changping_df['DEWP'].mean()
changping_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = changping_df['RAIN'].mean()
changping_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
changping_df.fillna(value="NNW", inplace=True)

# WSPM
changping_df['WSPM'] = pd.to_numeric(changping_df['WSPM'], errors='coerce')
mean_wspm = changping_df['WSPM'].mean()
changping_df['WSPM'].fillna(mean_wspm, inplace=True)


# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
changping_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data dingling_df

# %% [markdown]
# #### Mengatasi Outlier dingling_df

# %%
# Outlier PM2.5
Q1_pm25 = dingling_df['PM2.5'].quantile(0.25)
Q3_pm25 = dingling_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = dingling_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = dingling_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
dingling_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = dingling_df['PM10'].quantile(0.25)
Q3_pm10 = dingling_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = dingling_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = dingling_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
dingling_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = dingling_df['SO2'].quantile(0.25)
Q3_so2 = dingling_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = dingling_df['SO2'] < minimum_so2
kondisi_more_than_so2 = dingling_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
dingling_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = dingling_df['NO2'].quantile(0.25)
Q3_no2 = dingling_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = dingling_df['NO2'] < minimum_no2
kondisi_more_than_no2 = dingling_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
dingling_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

dingling_df['NO2'] = pd.to_numeric(dingling_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = dingling_df['CO'].quantile(0.25)
Q3_co = dingling_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = dingling_df['CO'] < minimum_co
kondisi_more_than_co = dingling_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
dingling_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = dingling_df['O3'].quantile(0.25)
Q3_o3 = dingling_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = dingling_df['O3'] < minimum_o3
kondisi_more_than_o3 = dingling_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
dingling_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
dingling_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
dingling_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value dingling_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
dingling_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
dingling_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
dingling_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
dingling_df['NO2'] = pd.to_numeric(dingling_df['NO2'], errors='coerce')
dingling_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
dingling_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
dingling_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = dingling_df['TEMP'].mean()
dingling_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = dingling_df['PRES'].mean()
dingling_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = dingling_df['DEWP'].mean()
dingling_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = dingling_df['RAIN'].mean()
dingling_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
dingling_df.fillna(value="NNW", inplace=True)

# WSPM
dingling_df['WSPM'] = pd.to_numeric(dingling_df['WSPM'], errors='coerce')
mean_wspm = dingling_df['WSPM'].mean()
dingling_df['WSPM'].fillna(mean_wspm, inplace=True)


# %%
# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
dingling_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data dongsi_df

# %% [markdown]
# #### Mengatasi Outlier dongsi_df

# %%
# Outlier PM2.5
Q1_pm25 = dongsi_df['PM2.5'].quantile(0.25)
Q3_pm25 = dongsi_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = dongsi_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = dongsi_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
dongsi_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = dongsi_df['PM10'].quantile(0.25)
Q3_pm10 = dongsi_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = dongsi_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = dongsi_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
dongsi_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = dongsi_df['SO2'].quantile(0.25)
Q3_so2 = dongsi_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = dongsi_df['SO2'] < minimum_so2
kondisi_more_than_so2 = dongsi_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
dongsi_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = dongsi_df['NO2'].quantile(0.25)
Q3_no2 = dongsi_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = dongsi_df['NO2'] < minimum_no2
kondisi_more_than_no2 = dongsi_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
dongsi_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

dongsi_df['NO2'] = pd.to_numeric(dongsi_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = dongsi_df['CO'].quantile(0.25)
Q3_co = dongsi_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = dongsi_df['CO'] < minimum_co
kondisi_more_than_co = dongsi_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
dongsi_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = dongsi_df['O3'].quantile(0.25)
Q3_o3 = dongsi_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = dongsi_df['O3'] < minimum_o3
kondisi_more_than_o3 = dongsi_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
dongsi_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
dongsi_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
dongsi_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value dongsi_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
dongsi_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
dongsi_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
dongsi_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
dongsi_df['NO2'] = pd.to_numeric(dongsi_df['NO2'], errors='coerce')
dongsi_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
dongsi_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
dongsi_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = dongsi_df['TEMP'].mean()
dongsi_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = dongsi_df['PRES'].mean()
dongsi_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = dongsi_df['DEWP'].mean()
dongsi_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = dongsi_df['RAIN'].mean()
dongsi_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
dongsi_df.fillna(value="ENE", inplace=True)

# WSPM
dongsi_df['WSPM'] = pd.to_numeric(dongsi_df['WSPM'], errors='coerce')
mean_wspm = dongsi_df['WSPM'].mean()
dongsi_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
dongsi_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data guanyuan_df

# %% [markdown]
# #### Mengatasi Outlier guanyuan_df

# %%
# Outlier PM2.5
Q1_pm25 = guanyuan_df['PM2.5'].quantile(0.25)
Q3_pm25 = guanyuan_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = guanyuan_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = guanyuan_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
guanyuan_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = guanyuan_df['PM10'].quantile(0.25)
Q3_pm10 = guanyuan_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = guanyuan_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = guanyuan_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
guanyuan_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = guanyuan_df['SO2'].quantile(0.25)
Q3_so2 = guanyuan_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = guanyuan_df['SO2'] < minimum_so2
kondisi_more_than_so2 = guanyuan_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
guanyuan_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = guanyuan_df['NO2'].quantile(0.25)
Q3_no2 = guanyuan_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = guanyuan_df['NO2'] < minimum_no2
kondisi_more_than_no2 = guanyuan_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
guanyuan_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

guanyuan_df['NO2'] = pd.to_numeric(guanyuan_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = guanyuan_df['CO'].quantile(0.25)
Q3_co = guanyuan_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = guanyuan_df['CO'] < minimum_co
kondisi_more_than_co = guanyuan_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
guanyuan_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = guanyuan_df['O3'].quantile(0.25)
Q3_o3 = guanyuan_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = guanyuan_df['O3'] < minimum_o3
kondisi_more_than_o3 = guanyuan_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
guanyuan_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
guanyuan_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
guanyuan_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value guanyuan_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
guanyuan_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
guanyuan_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
guanyuan_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
guanyuan_df['NO2'] = pd.to_numeric(guanyuan_df['NO2'], errors='coerce')
guanyuan_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
guanyuan_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
guanyuan_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = guanyuan_df['TEMP'].mean()
guanyuan_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = guanyuan_df['PRES'].mean()
guanyuan_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = guanyuan_df['DEWP'].mean()
guanyuan_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = guanyuan_df['RAIN'].mean()
guanyuan_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
guanyuan_df.fillna(value="ENE", inplace=True)

# WSPM
guanyuan_df['WSPM'] = pd.to_numeric(guanyuan_df['WSPM'], errors='coerce')
mean_wspm = guanyuan_df['WSPM'].mean()
guanyuan_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
guanyuan_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data gucheng_df

# %% [markdown]
# #### Mengatasi Outlier gucheng_df

# %%
# Outlier PM2.5
Q1_pm25 = gucheng_df['PM2.5'].quantile(0.25)
Q3_pm25 = gucheng_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = gucheng_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = gucheng_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
gucheng_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = gucheng_df['PM10'].quantile(0.25)
Q3_pm10 = gucheng_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = gucheng_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = gucheng_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
gucheng_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = gucheng_df['SO2'].quantile(0.25)
Q3_so2 = gucheng_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = gucheng_df['SO2'] < minimum_so2
kondisi_more_than_so2 = gucheng_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
gucheng_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = gucheng_df['NO2'].quantile(0.25)
Q3_no2 = gucheng_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = gucheng_df['NO2'] < minimum_no2
kondisi_more_than_no2 = gucheng_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
gucheng_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

gucheng_df['NO2'] = pd.to_numeric(gucheng_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = gucheng_df['CO'].quantile(0.25)
Q3_co = gucheng_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = gucheng_df['CO'] < minimum_co
kondisi_more_than_co = gucheng_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
gucheng_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = gucheng_df['O3'].quantile(0.25)
Q3_o3 = gucheng_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = gucheng_df['O3'] < minimum_o3
kondisi_more_than_o3 = gucheng_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
gucheng_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
gucheng_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
gucheng_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value guanyuan_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
gucheng_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
gucheng_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
gucheng_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
gucheng_df['NO2'] = pd.to_numeric(gucheng_df['NO2'], errors='coerce')
gucheng_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
gucheng_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
gucheng_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = gucheng_df['TEMP'].mean()
gucheng_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = gucheng_df['PRES'].mean()
gucheng_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = gucheng_df['DEWP'].mean()
gucheng_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = gucheng_df['RAIN'].mean()
gucheng_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
gucheng_df.fillna(value="ENE", inplace=True)

# WSPM
gucheng_df['WSPM'] = pd.to_numeric(gucheng_df['WSPM'], errors='coerce')
mean_wspm = gucheng_df['WSPM'].mean()
gucheng_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
gucheng_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data huairou_df

# %% [markdown]
# #### Mengatasi Outlier huairou_df

# %%
# Outlier PM2.5
Q1_pm25 = huairou_df['PM2.5'].quantile(0.25)
Q3_pm25 = huairou_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = huairou_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = huairou_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
huairou_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = huairou_df['PM10'].quantile(0.25)
Q3_pm10 = huairou_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = huairou_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = huairou_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
huairou_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = huairou_df['SO2'].quantile(0.25)
Q3_so2 = huairou_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = huairou_df['SO2'] < minimum_so2
kondisi_more_than_so2 = huairou_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
huairou_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = huairou_df['NO2'].quantile(0.25)
Q3_no2 = huairou_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = huairou_df['NO2'] < minimum_no2
kondisi_more_than_no2 = huairou_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
huairou_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

huairou_df['NO2'] = pd.to_numeric(huairou_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = huairou_df['CO'].quantile(0.25)
Q3_co = huairou_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = huairou_df['CO'] < minimum_co
kondisi_more_than_co = huairou_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
huairou_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = huairou_df['O3'].quantile(0.25)
Q3_o3 = huairou_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = huairou_df['O3'] < minimum_o3
kondisi_more_than_o3 = huairou_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
huairou_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
huairou_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
huairou_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value huairou_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
huairou_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
huairou_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
huairou_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
huairou_df['NO2'] = pd.to_numeric(huairou_df['NO2'], errors='coerce')
huairou_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
huairou_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
huairou_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = huairou_df['TEMP'].mean()
huairou_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = huairou_df['PRES'].mean()
huairou_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = huairou_df['DEWP'].mean()
huairou_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = huairou_df['RAIN'].mean()
huairou_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
huairou_df.fillna(value="ENE", inplace=True)

# WSPM
huairou_df['WSPM'] = pd.to_numeric(huairou_df['WSPM'], errors='coerce')
mean_wspm = huairou_df['WSPM'].mean()
huairou_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
huairou_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data nongzhanguan_df

# %% [markdown]
# #### Mengatasi Outlier nongzhanguan_df

# %%
# Outlier PM2.5
Q1_pm25 = nongzhanguan_df['PM2.5'].quantile(0.25)
Q3_pm25 = nongzhanguan_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = nongzhanguan_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = nongzhanguan_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
nongzhanguan_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = nongzhanguan_df['PM10'].quantile(0.25)
Q3_pm10 = nongzhanguan_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = nongzhanguan_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = nongzhanguan_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
nongzhanguan_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = nongzhanguan_df['SO2'].quantile(0.25)
Q3_so2 = nongzhanguan_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = nongzhanguan_df['SO2'] < minimum_so2
kondisi_more_than_so2 = nongzhanguan_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
nongzhanguan_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = nongzhanguan_df['NO2'].quantile(0.25)
Q3_no2 = nongzhanguan_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = nongzhanguan_df['NO2'] < minimum_no2
kondisi_more_than_no2 = nongzhanguan_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
nongzhanguan_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

nongzhanguan_df['NO2'] = pd.to_numeric(nongzhanguan_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = nongzhanguan_df['CO'].quantile(0.25)
Q3_co = nongzhanguan_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = nongzhanguan_df['CO'] < minimum_co
kondisi_more_than_co = nongzhanguan_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
nongzhanguan_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = nongzhanguan_df['O3'].quantile(0.25)
Q3_o3 = nongzhanguan_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = nongzhanguan_df['O3'] < minimum_o3
kondisi_more_than_o3 = nongzhanguan_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
nongzhanguan_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
nongzhanguan_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
nongzhanguan_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value nongzhanguan_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
nongzhanguan_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
nongzhanguan_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
nongzhanguan_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
nongzhanguan_df['NO2'] = pd.to_numeric(nongzhanguan_df['NO2'], errors='coerce')
nongzhanguan_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
nongzhanguan_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
nongzhanguan_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = nongzhanguan_df['TEMP'].mean()
nongzhanguan_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = nongzhanguan_df['PRES'].mean()
nongzhanguan_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = nongzhanguan_df['DEWP'].mean()
nongzhanguan_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = nongzhanguan_df['RAIN'].mean()
nongzhanguan_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
nongzhanguan_df.fillna(value="ENE", inplace=True)

# WSPM
nongzhanguan_df['WSPM'] = pd.to_numeric(nongzhanguan_df['WSPM'], errors='coerce')
mean_wspm = nongzhanguan_df['WSPM'].mean()
nongzhanguan_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
nongzhanguan_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data shunyi_df

# %% [markdown]
# #### Mengatasi Outlier shunyi_df

# %%
# Outlier PM2.5
Q1_pm25 = shunyi_df['PM2.5'].quantile(0.25)
Q3_pm25 = shunyi_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = shunyi_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = shunyi_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
shunyi_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = shunyi_df['PM10'].quantile(0.25)
Q3_pm10 = shunyi_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = shunyi_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = shunyi_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
shunyi_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = shunyi_df['SO2'].quantile(0.25)
Q3_so2 = shunyi_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = shunyi_df['SO2'] < minimum_so2
kondisi_more_than_so2 = shunyi_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
shunyi_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = shunyi_df['NO2'].quantile(0.25)
Q3_no2 = shunyi_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = shunyi_df['NO2'] < minimum_no2
kondisi_more_than_no2 = shunyi_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
shunyi_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

shunyi_df['NO2'] = pd.to_numeric(shunyi_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = shunyi_df['CO'].quantile(0.25)
Q3_co = shunyi_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = shunyi_df['CO'] < minimum_co
kondisi_more_than_co = shunyi_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
shunyi_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = shunyi_df['O3'].quantile(0.25)
Q3_o3 = shunyi_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = shunyi_df['O3'] < minimum_o3
kondisi_more_than_o3 = shunyi_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
shunyi_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
shunyi_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
shunyi_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value shunyi_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
shunyi_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
shunyi_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
shunyi_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
shunyi_df['NO2'] = pd.to_numeric(shunyi_df['NO2'], errors='coerce')
shunyi_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
shunyi_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
shunyi_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = shunyi_df['TEMP'].mean()
shunyi_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = shunyi_df['PRES'].mean()
shunyi_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = shunyi_df['DEWP'].mean()
shunyi_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = shunyi_df['RAIN'].mean()
shunyi_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
shunyi_df.fillna(value="ENE", inplace=True)

# WSPM
shunyi_df['WSPM'] = pd.to_numeric(shunyi_df['WSPM'], errors='coerce')
mean_wspm = shunyi_df['WSPM'].mean()
shunyi_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
shunyi_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data tiantan_df

# %% [markdown]
# #### Mengatasi Outlier tiantan_df

# %%
# Outlier PM2.5
Q1_pm25 = tiantan_df['PM2.5'].quantile(0.25)
Q3_pm25 = tiantan_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = tiantan_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = tiantan_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
tiantan_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = tiantan_df['PM10'].quantile(0.25)
Q3_pm10 = tiantan_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = tiantan_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = tiantan_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
tiantan_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = tiantan_df['SO2'].quantile(0.25)
Q3_so2 = tiantan_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = tiantan_df['SO2'] < minimum_so2
kondisi_more_than_so2 = tiantan_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
tiantan_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = tiantan_df['NO2'].quantile(0.25)
Q3_no2 = tiantan_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = tiantan_df['NO2'] < minimum_no2
kondisi_more_than_no2 = tiantan_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
tiantan_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

tiantan_df['NO2'] = pd.to_numeric(tiantan_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = tiantan_df['CO'].quantile(0.25)
Q3_co = tiantan_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = tiantan_df['CO'] < minimum_co
kondisi_more_than_co = tiantan_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
tiantan_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = tiantan_df['O3'].quantile(0.25)
Q3_o3 = tiantan_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = tiantan_df['O3'] < minimum_o3
kondisi_more_than_o3 = tiantan_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
tiantan_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
tiantan_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
tiantan_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value tiantan_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
shunyi_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
shunyi_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
shunyi_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
shunyi_df['NO2'] = pd.to_numeric(shunyi_df['NO2'], errors='coerce')
shunyi_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
shunyi_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
shunyi_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = shunyi_df['TEMP'].mean()
shunyi_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = shunyi_df['PRES'].mean()
shunyi_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = shunyi_df['DEWP'].mean()
shunyi_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = shunyi_df['RAIN'].mean()
shunyi_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
shunyi_df.fillna(value="ENE", inplace=True)

# WSPM
shunyi_df['WSPM'] = pd.to_numeric(shunyi_df['WSPM'], errors='coerce')
mean_wspm = shunyi_df['WSPM'].mean()
shunyi_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
shunyi_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data wanliu_df

# %% [markdown]
# #### Mengatasi Outlier wanliu_df

# %%
# Outlier PM2.5
Q1_pm25 = wanliu_df['PM2.5'].quantile(0.25)
Q3_pm25 = wanliu_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = wanliu_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = wanliu_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
wanliu_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = wanliu_df['PM10'].quantile(0.25)
Q3_pm10 = wanliu_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = wanliu_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = wanliu_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
wanliu_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = wanliu_df['SO2'].quantile(0.25)
Q3_so2 = wanliu_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = wanliu_df['SO2'] < minimum_so2
kondisi_more_than_so2 = wanliu_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
wanliu_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = wanliu_df['NO2'].quantile(0.25)
Q3_no2 = wanliu_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = wanliu_df['NO2'] < minimum_no2
kondisi_more_than_no2 = wanliu_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
wanliu_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

wanliu_df['NO2'] = pd.to_numeric(wanliu_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = wanliu_df['CO'].quantile(0.25)
Q3_co = wanliu_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = wanliu_df['CO'] < minimum_co
kondisi_more_than_co = wanliu_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
wanliu_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = wanliu_df['O3'].quantile(0.25)
Q3_o3 = wanliu_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = wanliu_df['O3'] < minimum_o3
kondisi_more_than_o3 = wanliu_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
wanliu_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
wanliu_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
wanliu_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value wanliu_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
shunyi_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
shunyi_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
shunyi_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
shunyi_df['NO2'] = pd.to_numeric(shunyi_df['NO2'], errors='coerce')
shunyi_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
shunyi_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
shunyi_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = shunyi_df['TEMP'].mean()
shunyi_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = shunyi_df['PRES'].mean()
shunyi_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = shunyi_df['DEWP'].mean()
shunyi_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = shunyi_df['RAIN'].mean()
shunyi_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
shunyi_df.fillna(value="ENE", inplace=True)

# WSPM
shunyi_df['WSPM'] = pd.to_numeric(shunyi_df['WSPM'], errors='coerce')
mean_wspm = shunyi_df['WSPM'].mean()
shunyi_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
shunyi_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data wanshouxigong_df

# %% [markdown]
# #### Mengatasi Outlier wanshouxigong_df

# %%
# Outlier PM2.5
Q1_pm25 = wanshouxigong_df['PM2.5'].quantile(0.25)
Q3_pm25 = wanshouxigong_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = wanshouxigong_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = wanshouxigong_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
wanshouxigong_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = wanshouxigong_df['PM10'].quantile(0.25)
Q3_pm10 = wanshouxigong_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = wanshouxigong_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = wanshouxigong_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
wanshouxigong_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = wanshouxigong_df['SO2'].quantile(0.25)
Q3_so2 = wanshouxigong_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = wanshouxigong_df['SO2'] < minimum_so2
kondisi_more_than_so2 = wanshouxigong_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
wanshouxigong_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = wanshouxigong_df['NO2'].quantile(0.25)
Q3_no2 = wanshouxigong_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = wanshouxigong_df['NO2'] < minimum_no2
kondisi_more_than_no2 = wanshouxigong_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
wanshouxigong_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

wanshouxigong_df['NO2'] = pd.to_numeric(wanshouxigong_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = wanshouxigong_df['CO'].quantile(0.25)
Q3_co = wanshouxigong_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = wanshouxigong_df['CO'] < minimum_co
kondisi_more_than_co = wanshouxigong_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
wanshouxigong_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = wanshouxigong_df['O3'].quantile(0.25)
Q3_o3 = wanshouxigong_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = wanshouxigong_df['O3'] < minimum_o3
kondisi_more_than_o3 = wanshouxigong_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
wanshouxigong_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
wanshouxigong_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
wanshouxigong_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value wanshouxigong_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
wanshouxigong_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
wanshouxigong_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
wanshouxigong_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
wanshouxigong_df['NO2'] = pd.to_numeric(wanshouxigong_df['NO2'], errors='coerce')
wanshouxigong_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
wanshouxigong_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
wanshouxigong_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = wanshouxigong_df['TEMP'].mean()
wanshouxigong_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = wanshouxigong_df['PRES'].mean()
wanshouxigong_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = wanshouxigong_df['DEWP'].mean()
wanshouxigong_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = wanshouxigong_df['RAIN'].mean()
wanshouxigong_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
wanshouxigong_df.fillna(value="ENE", inplace=True)

# WSPM
wanshouxigong_df['WSPM'] = pd.to_numeric(wanshouxigong_df['WSPM'], errors='coerce')
mean_wspm = wanshouxigong_df['WSPM'].mean()
wanshouxigong_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
wanshouxigong_df.isna().sum()

# %% [markdown]
# ### Membersihkan Data aotizhongxin_df

# %% [markdown]
# #### Mengatasi Outlier aotizhongxin_df

# %%
# Outlier PM2.5
Q1_pm25 = aotizhongxin_df['PM2.5'].quantile(0.25)
Q3_pm25 = aotizhongxin_df['PM2.5'].quantile(0.75)
IQR_pm25 = Q3_pm25 - Q1_pm25

maximum_pm25 = Q3_pm25 + (1.5 * IQR_pm25)
minimum_pm25 = Q1_pm25 - (1.5 * IQR_pm25)

kondisi_lower_than_pm25 = aotizhongxin_df['PM2.5'] < minimum_pm25
kondisi_more_than_pm25 = aotizhongxin_df['PM2.5'] > maximum_pm25

# Ganti outliers in 'PM2.5' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_pm25, 'PM2.5'] = minimum_pm25
aotizhongxin_df.loc[kondisi_more_than_pm25, 'PM2.5'] = maximum_pm25

####
# Outlier PM10
Q1_pm10 = aotizhongxin_df['PM10'].quantile(0.25)
Q3_pm10 = aotizhongxin_df['PM10'].quantile(0.75)
IQR_pm10 = Q3_pm10 - Q1_pm10

maximum_pm10 = Q3_pm10 + (1.5 * IQR_pm10)
minimum_pm10 = Q1_pm10 - (1.5 * IQR_pm10)

kondisi_lower_than_pm10 = aotizhongxin_df['PM10'] < minimum_pm10
kondisi_more_than_pm10 = aotizhongxin_df['PM10'] > maximum_pm10

# Ganti outliers in 'PM10' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_pm10, 'PM10'] = minimum_pm10
aotizhongxin_df.loc[kondisi_more_than_pm10, 'PM10'] = maximum_pm10

###
# Outlier SO2
Q1_so2 = aotizhongxin_df['SO2'].quantile(0.25)
Q3_so2 = aotizhongxin_df['SO2'].quantile(0.75)
IQR_so2 = Q3_so2 - Q1_so2

maximum_so2 = Q3_so2 + (1.5 * IQR_so2)
minimum_so2 = Q1_so2 - (1.5 * IQR_so2)

kondisi_lower_than_so2 = aotizhongxin_df['SO2'] < minimum_so2
kondisi_more_than_so2 = aotizhongxin_df['SO2'] > maximum_so2

# Ganti outliers in 'SO2' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_so2, 'SO2'] = minimum_so2
aotizhongxin_df.loc[kondisi_more_than_so2, 'SO2'] = maximum_so2

###
# Outlier NO2
Q1_no2 = aotizhongxin_df['NO2'].quantile(0.25)
Q3_no2 = aotizhongxin_df['NO2'].quantile(0.75)
IQR_no2 = Q3_no2 - Q1_no2

maximum_no2 = Q3_no2 + (1.5 * IQR_no2)
minimum_no2 = Q1_no2 - (1.5 * IQR_no2)

kondisi_lower_than_no2 = aotizhongxin_df['NO2'] < minimum_no2
kondisi_more_than_no2 = aotizhongxin_df['NO2'] > maximum_no2

# Ganti outliers in 'NO2' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_no2, 'NO2'] = minimum_no2
aotizhongxin_df.loc[kondisi_more_than_no2, 'NO2'] = maximum_no2

aotizhongxin_df['NO2'] = pd.to_numeric(aotizhongxin_df['NO2'], errors='coerce')

###
# Outlier CO
Q1_co = aotizhongxin_df['CO'].quantile(0.25)
Q3_co = aotizhongxin_df['CO'].quantile(0.75)
IQR_co = Q3_co - Q1_co

maximum_co = Q3_co + (1.5 * IQR_co)
minimum_co = Q1_co - (1.5 * IQR_co)

kondisi_lower_than_co = aotizhongxin_df['CO'] < minimum_co
kondisi_more_than_co = aotizhongxin_df['CO'] > maximum_co

# Ganti outliers in 'CO' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_co, 'CO'] = minimum_co
aotizhongxin_df.loc[kondisi_more_than_co, 'CO'] = maximum_co

###
# Outlier O3
Q1_o3 = aotizhongxin_df['O3'].quantile(0.25)
Q3_o3 = aotizhongxin_df['O3'].quantile(0.75)
IQR_o3 = Q3_o3 - Q1_o3

maximum_o3 = Q3_o3 + (1.5 * IQR_o3)
minimum_o3 = Q1_o3 - (1.5 * IQR_o3)

kondisi_lower_than_o3 = aotizhongxin_df['O3'] < minimum_o3
kondisi_more_than_o3 = aotizhongxin_df['O3'] > maximum_o3

# Ganti outliers in 'O3' dengan hitungan minimum or maximum
aotizhongxin_df.loc[kondisi_lower_than_o3, 'O3'] = minimum_o3
aotizhongxin_df.loc[kondisi_more_than_o3, 'O3'] = maximum_o3

# Menampilkan ringkasan statistik dari DataFrame
aotizhongxin_df.describe()


# %% [markdown]
# #### Mengatasi Missing Value aotizhongxin_df

# %%
# Melakukan interpolasi untuk mengisi nilai yang hilang pada kolom 'PM2.5' dengan metode linear
# 'limit_direction' digunakan untuk mengatur arah interpolasi ke depan (forward)
aotizhongxin_df['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)

# PM10
aotizhongxin_df['PM10'].interpolate(method='linear', limit_direction='forward', inplace=True)

# SO2
aotizhongxin_df['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# NO2
aotizhongxin_df['NO2'] = pd.to_numeric(aotizhongxin_df['NO2'], errors='coerce')
aotizhongxin_df['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)

# CO
aotizhongxin_df['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)

# O3
aotizhongxin_df['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

# Imputing missing values in 'TEMP' column with mean
mean_temp = aotizhongxin_df['TEMP'].mean()
aotizhongxin_df['TEMP'].fillna(mean_temp, inplace=True)

# PRES
mean_pres = aotizhongxin_df['PRES'].mean()
aotizhongxin_df['PRES'].fillna(mean_pres, inplace=True)

# DEWP
mean_dewp = aotizhongxin_df['DEWP'].mean()
aotizhongxin_df['DEWP'].fillna(mean_dewp, inplace=True)

# RAIN
mean_rain = aotizhongxin_df['RAIN'].mean()
aotizhongxin_df['RAIN'].fillna(mean_rain, inplace=True)

# wd
aotizhongxin_df.fillna(value="ENE", inplace=True)

# WSPM
aotizhongxin_df['WSPM'] = pd.to_numeric(aotizhongxin_df['WSPM'], errors='coerce')
mean_wspm = aotizhongxin_df['WSPM'].mean()
aotizhongxin_df['WSPM'].fillna(mean_wspm, inplace=True)

# Menampilkan jumlah nilai null (NaN) dalam setiap kolom DataFrame
aotizhongxin_df.isna().sum()

# %% [markdown]
# ## Exploratory Data Analysis (EDA)

# %% [markdown]
# ### Explore Data aotizhongxin_df

# %%
aotizhongxin_df.describe(include="all")

# %% [markdown]
# #### PM 2.5

# %%
aotizhongxin_df.sort_values(by="No").head(20)


# %% [markdown]
# #### CO

# %%
aotizhongxin_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data changping_df

# %% [markdown]
# #### PM2.5

# %%
changping_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
changping_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data dingling_df

# %% [markdown]
# #### PM2.5

# %%
dingling_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
dingling_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data dongsi_df

# %% [markdown]
# #### PM2.5

# %%
dongsi_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
dongsi_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data guanyuan_df

# %% [markdown]
# #### PM2.5 

# %%
guanyuan_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
guanyuan_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data gucheng_df

# %% [markdown]
# #### PM2.5

# %%
gucheng_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
gucheng_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data huairou_df

# %% [markdown]
# #### PM2.5

# %%
huairou_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
huairou_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data nongzhanguan_df

# %% [markdown]
# #### PM2.5

# %%
nongzhanguan_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
nongzhanguan_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data shunyi_df

# %% [markdown]
# #### PM2.5

# %%
shunyi_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
shunyi_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data tiantan_df

# %% [markdown]
# #### PM2.5

# %%
tiantan_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
tiantan_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data wanliu_df

# %% [markdown]
# #### PM2.5

# %%
wanliu_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
wanliu_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Explore Data wanshouxigong_df

# %% [markdown]
# #### PM2.5

# %%
wanshouxigong_df.sort_values(by="No").head(20)

# %% [markdown]
# #### CO

# %%
wanshouxigong_df.groupby(by="CO").agg({
        "No": "nunique",
        "CO": ["max", "min", "mean", "std"]
})

# %% [markdown]
# ### Merge 1

# %%
data1_df = pd.merge(
    left=aotizhongxin_df,
    right=changping_df,
    how="left",
    left_on="No",
    right_on="No"
)
data1_df.head()

# %% [markdown]
# ### Merge 2

# %%
data2_df = pd.merge(
    left=dingling_df,
    right=dongsi_df,
    how="left",
    left_on="No",
    right_on="No"
)
data2_df.head()

# %% [markdown]
# ### Merge 3

# %%
data3_df = pd.merge(
    left=guanyuan_df,
    right=gucheng_df,
    how="left",
    left_on="No",
    right_on="No"
)
data3_df.head()

# %% [markdown]
# ### Merge 4

# %%
data4_df = pd.merge(
    left=huairou_df,
    right=nongzhanguan_df,
    how="left",
    left_on="No",
    right_on="No"
)
data4_df.head()

# %% [markdown]
# ### Merge 5

# %%
data5_df = pd.merge(
    left=shunyi_df,
    right=tiantan_df,
    how="left",
    left_on="No",
    right_on="No"
)
data5_df.head()

# %% [markdown]
# ### Merge 6

# %%
data6_df = pd.merge(
    left=wanliu_df,
    right=wanshouxigong_df,
    how="left",
    left_on="No",
    right_on="No"
)
data6_df.head()

# %% [markdown]
# ### all_df

# %%
# Concatenate dataframes vertically
all_df = pd.concat([data1_df, data2_df, data3_df, data4_df, data5_df, data6_df], axis=0)

all_df.head()

# %% [markdown]
# ## Visualization & Explanatory Analysis

# %% [markdown]
# ### aotizhongxin_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
aotizhongxin_df['Month'] = aotizhongxin_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=aotizhongxin_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=aotizhongxin_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### changping_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
changping_df['Month'] = changping_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=changping_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=changping_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### dingling_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
dingling_df['Month'] = dingling_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=dingling_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=dingling_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### dongsi_df

# %% [markdown]
# #### PM 2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
dongsi_df['Month'] = dongsi_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=dongsi_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=dongsi_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()

# %% [markdown]
# ### guanyuan_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
guanyuan_df['Month'] = guanyuan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=guanyuan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=guanyuan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### gucheng_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
gucheng_df['Month'] = gucheng_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=gucheng_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=gucheng_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### huairou_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
huairou_df['Month'] = huairou_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=huairou_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=huairou_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### nongzhanguan_df

# %% [markdown]
# #### PM2.5  

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
nongzhanguan_df['Month'] = nongzhanguan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=nongzhanguan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=nongzhanguan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### shunyi_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
shunyi_df['Month'] = shunyi_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=shunyi_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=shunyi_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# #### tiantan_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
tiantan_df['Month'] = tiantan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=tiantan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tiantan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### wanliu_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
wanliu_df['Month'] = wanliu_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=wanliu_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=wanliu_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# #### wanshouxigong_df

# %% [markdown]
# #### PM2.5

# %%
# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
wanshouxigong_df['Month'] = wanshouxigong_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=wanshouxigong_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# #### CO

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(data=wanshouxigong_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ## Dashboard

# %%
all_df.to_csv("all_data.csv", index=False)

# %% [markdown]
# ## Streamlit

# %%
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# %% [markdown]
# ## Dataframe

# %% [markdown]
# ### create_pm2.5() 

# %% [markdown]
# ### aotizhongxin_df

# %%
def create_pm25_aotizhongxin_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    aotizhongxin_df['Month'] = aotizhongxin_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=aotizhongxin_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_aotizhongxin_df

# %% [markdown]
# ### changping_df

# %%
def create_pm25_changping_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    changping_df['Month'] = changping_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=changping_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_changping_df

# %% [markdown]
# ### dingling_df

# %%
def create_pm25_dingling_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    dingling_df['Month'] = dingling_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=dingling_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_dingling_df

# %% [markdown]
# ### dongsi_df

# %%
def create_pm25_dongsi_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    dongsi_df['Month'] = dongsi_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=dongsi_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_dongsi_df

# %% [markdown]
# ### guanyuan_df

# %%
def create_pm25_guanyuan_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    guanyuan_df['Month'] = guanyuan_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=guanyuan_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_guanyuan_df

# %% [markdown]
# ### gucheng_df

# %%
def create_pm25_gucheng_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    gucheng_df['Month'] = gucheng_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=gucheng_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_gucheng_df

# %% [markdown]
# ### huairou_df

# %%
def create_pm25_huairou_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    huairou_df['Month'] = huairou_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=huairou_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_huairou_df

# %% [markdown]
# ### nongzhanguan_df

# %%
def create_pm25_nongzhanguan_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    nongzhanguan_df['Month'] = nongzhanguan_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=nongzhanguan_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_nongzhanguan_df

# %% [markdown]
# ### shunyi_df

# %%
def create_pm25_shunyi_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    shunyi_df['Month'] = shunyi_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=shunyi_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_shunyi_df

# %% [markdown]
# ### tiantan_df

# %%
def create_pm25_tiantan_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    tiantan_df['Month'] = tiantan_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=tiantan_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_tiantan_df

# %% [markdown]
# ### wanliu_df

# %%
def create_pm25_wanliu_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    wanliu_df['Month'] = wanliu_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=wanliu_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_wanliu_df

# %% [markdown]
# ### wanshouxigong_df

# %%
def create_pm25_wanshouxigong_df(df):
    # Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
    wanshouxigong_df['Month'] = wanshouxigong_df['month'].apply(lambda x: f'Month {x}')

    # Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(data=wanshouxigong_df, x='Month', y='PM2.5', ci=None)
    plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Rata-rata PM2.5')
    plt.xticks(rotation=45)
    plt.show()
    
    return create_pm25_wanshouxigong_df

# %% [markdown]
# ## CO

# %% [markdown]
# ### aotizhongxin_df

# %%
def create_co_aotizhongxin_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=aotizhongxin_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_aotizhongxin_df

# %% [markdown]
# ### changping_df

# %%
def create_co_changping_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=changping_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_changping_df

# %% [markdown]
# ### dingling_df

# %%
def create_co_dingling_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=dingling_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_dingling_df

# %% [markdown]
# ### dongsi_df

# %%
def create_co_dongsi_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=dongsi_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_dongsi_df

# %% [markdown]
# ### guanyuan_df

# %%
def create_co_guanyuan_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=guanyuan_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_guanyuan_df

# %% [markdown]
# ### gucheng_df

# %%
def create_co_gucheng_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=gucheng_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_gucheng_df

# %% [markdown]
# ### huairou_df

# %%
def create_co_huairou_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=huairou_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_huairou_df

# %% [markdown]
# ### nongzhanguan_df

# %%
def create_co_nongzhanguan_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=nongzhanguan_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_nongzhanguan_df

# %% [markdown]
# ### shunyi_df

# %%
def create_co_shunyi_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=shunyi_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_shunyi_df

# %% [markdown]
# ### tiantan_df

# %%
def create_co_tiantan_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=tiantan_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_tiantan_df

# %% [markdown]
# ### wanliu_df

# %%
def create_co_wanliu_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=wanliu_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_wanliu_df

# %% [markdown]
# ### wanshouxigong_df

# %%
def create_co_wanshouxigong_df(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=wanshouxigong_df, x='CO', y='PM2.5', alpha=0.5)
    plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
    plt.xlabel('Level Polusi (CO)')
    plt.ylabel('Konsentrasi PM2.5')
    plt.show()
    
    return create_co_wanshouxigong_df

# %% [markdown]
# ## Load all_df

# %%
all_df = pd.read_csv("https://raw.githubusercontent.com/hakan009/analisis-piton/main/dashboard/all_data.csv")

# %% [markdown]
# ## Lengkapi
# 

# %%
st.header('Hakan Alif P :sparkles:')

# %% [markdown]
# ## PM2.5

# %% [markdown]
# ### aotizhongxin_df

# %%
st.subheader("PM 2.5 aotizhongxin_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
aotizhongxin_df['Month'] = aotizhongxin_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=aotizhongxin_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### changping_df

# %%
st.subheader("PM 2.5 changping_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
changping_df['Month'] = changping_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=changping_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### dingling_df

# %%
st.subheader("PM 2.5 changping_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
dingling_df['Month'] = dingling_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=dingling_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### dongsi_df

# %%
st.subheader("PM 2.5 dongsi_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
dongsi_df['Month'] = dongsi_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=dongsi_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### guanyuan_df

# %%
st.subheader("PM 2.5 guanyuan_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
guanyuan_df['Month'] = guanyuan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=guanyuan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### gucheng_df

# %%
st.subheader("PM 2.5 gucheng_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
gucheng_df['Month'] = gucheng_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=gucheng_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### huairou_df

# %%
st.subheader("PM 2.5 huairou_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
gucheng_df['Month'] = gucheng_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=gucheng_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### nongzhanguan_df

# %%
st.subheader("PM 2.5 nongzhanguan_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
nongzhanguan_df['Month'] = nongzhanguan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=nongzhanguan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### shunyi_df

# %%
st.subheader("PM 2.5 shunyi_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
shunyi_df['Month'] = shunyi_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=shunyi_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### tiantan_df

# %%
st.subheader("PM 2.5 tiantan_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
tiantan_df['Month'] = tiantan_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=tiantan_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### wanliu_df

# %%
st.subheader("PM 2.5 wanliu_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
wanliu_df['Month'] = wanliu_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=wanliu_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### wanshouxigong_df

# %%
st.subheader("PM 2.5 wanliu_df")

# Menambahkan kolom baru 'Month' berdasarkan kolom 'month'
wanshouxigong_df['Month'] = wanshouxigong_df['month'].apply(lambda x: f'Month {x}')

# Visualisasi variasi konsentrasi rata-rata PM2.5 tiap bulan
plt.figure(figsize=(12, 6))
sns.barplot(data=wanshouxigong_df, x='Month', y='PM2.5', ci=None)
plt.title('Variasi Konsentrasi Rata-rata PM2.5 Tiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ## CO

# %% [markdown]
# ### aotizhongxin_df

# %%
st.subheader("CO aotizhongxin_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=aotizhongxin_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()

# %% [markdown]
# ### changping_df

# %%
st.subheader("CO changping_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=changping_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### dingling_df

# %%
st.subheader("CO dingling_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=dingling_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### dongsi_df

# %%
st.subheader("CO dongsi_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=dingling_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### guanyuan_df

# %%
st.subheader("CO guanyuan_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=guanyuan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### gucheng_df

# %%
st.subheader("CO gucheng_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=gucheng_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### huairou_df

# %%
st.subheader("CO huairou_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=huairou_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### nongzhanguan_df

# %%
st.subheader("CO nongzhanguan_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=nongzhanguan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### shunyi_df

# %%
st.subheader("CO shunyi_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=shunyi_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### tiantan_df

# %%
st.subheader("CO tiantan_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=tiantan_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### wanliu_df

# %%
st.subheader("CO wanliu_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=wanliu_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### wanshouxigong_df

# %%
st.subheader("CO wanshouxigong_df")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=wanshouxigong_df, x='CO', y='PM2.5', alpha=0.5)
plt.title('Hubungan antara Level Polusi (CO) dan Konsentrasi PM2.5')
plt.xlabel('Level Polusi (CO)')
plt.ylabel('Konsentrasi PM2.5')
plt.show()


# %% [markdown]
# ### Pertanyaan 1: 

# %% [markdown]
# Bagaimana level polusi dan hubungan CO ?

# %% [markdown]
# ### Pertanyaan 2: 

# %% [markdown]
# Bagaimana konsentrasi rata-rata PM2.5 bervariasi kumpulan data ? 

# %% [markdown]
# ## Conclusion

# %% [markdown]
# ### Pertanyaan 1: 

# %% [markdown]
# Setiap bertambah maka level polusi semakin bertambah dan zat lainnya juga berubah

# %% [markdown]
# ### Pertanyaan 2: 

# %% [markdown]
# Setiap bulan dapat bertambah dan berkurang dan tiap bulan level konsentrasi dapat mengubah level polusi


