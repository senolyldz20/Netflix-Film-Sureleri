#1.Veriler liste şeklinde sözlüğe eklenmesi
#Yıl ve süre listesi oluşturma
yıllar = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021,2022]
sureler = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90, 85, 60]

#Yukarıdaki listeleri sözlüğe çevirme
movie_dict = {"yıllar":[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
              "sureler":[103, 101, 99, 100, 100, 95, 95, 96, 93, 90]}
print(movie_dict)


#2.Sözlükten DataFrame oluşturma
import pandas as pd
sureler_df = pd.DataFrame(movie_dict)
print(sureler_df)


#3. Verilerin görsel olarak işlenmesi
#matplotlib import edilmesi
import matplotlib.pyplot as plt
fig = plt.figure()

#Yayın yılları ve sürelerinin çizgi grafiğe dökülmesi
plt.plot(sureler_df["yıllar"], sureler_df["sureler"])

#Başlıkların oluşturulması
plt.title("Netflix Filim Süreleri 2011-2020")
plt.xlabel("Yıllar")
plt.ylabel("Süreler")

plt.show()