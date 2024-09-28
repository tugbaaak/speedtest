import speedtest
import time

def hiz_testi():
    # Speedtest objesi oluştur
    st = speedtest.Speedtest()

    # En iyi sunucuyu seç
    st.get_best_server()

    # İndirme hızını ölç (Mbps cinsinden)
    indirme_hizi = st.download() / 10**6  # bits per second to Mbps

    # Yükleme hızını ölç (Mbps cinsinden)
    yukleme_hizi = st.upload() / 10**6  # bits per second to Mbps

    # Ping değerini ölç (ms cinsinden)
    ping = st.results.ping

    print(f"İndirme Hızı: {indirme_hizi:.2f} Mbps")
    print(f"Yükleme Hızı: {yukleme_hizi:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    print("-" * 30)

hiz_testi()

# # Sonsuz döngüye al ve her 5 dakikada bir testi tekrar et
# while True:
#     hiz_testi()
#     # 5 dakika (10 saniye) bekle
#     time.sleep(10)
