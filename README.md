# İnternet Hız Testi Scripti

Bu Python scripti, `speedtest` kütüphanesini kullanarak internet hızınızı ölçmek için tasarlanmıştır. Script, indirme hızı, yükleme hızı ve ping değerlerini gösterir. Ayrıca, belirli aralıklarla hız testi yapmak için sonsuz bir döngüde çalıştırılabilir.

## Gereksinimler

Bu scriptin çalışması için aşağıdaki gereksinimlere ihtiyaç vardır:

- Python 3.x
- `speedtest-cli` kütüphanesi

### Gerekli Kütüphanenin Kurulumu

`speedtest-cli` kütüphanesini kurmak için aşağıdaki komutu kullanabilirsiniz:

```sh
pip install speedtest-cli
```

## Kullanım
Scripti çalıştırarak anlık hız testi yapabilirsiniz.
İsterseniz, scripti bir döngü içinde çalıştırıp, her 5 dakikada bir hız testi yaptırabilirsiniz.
Tek Seferlik Hız Testi
Aşağıdaki komutu çalıştırarak internet hızınızı test edebilirsiniz:

```sh
python hiz_testi.py
```
Bu işlem sonucunda aşağıdaki değerler ekranda görüntülenir:

- İndirme Hızı (Mbps)
- Yükleme Hızı (Mbps)
- Ping (ms)

## Sürekli Hız Testi
Sonsuz döngüye alarak her 5 dakikada bir hız testi yapmak için, scriptin sonundaki yorum satırlarını kaldırın ve şu komutu çalıştırın:

```sh
while True:
    hiz_testi()
    time.sleep(300)  # 5 dakika (300 saniye)
```
Bu komut, her 5 dakikada bir hız testi yapacaktır. Test sonuçları her döngü sonunda ekrana yazdırılacaktır.

## Örnek Çıktı

```sh
İndirme Hızı: 50.32 Mbps
Yükleme Hızı: 12.45 Mbps
Ping: 25.67 ms
------------------------------
```
github reposunun linki: ´[speedtest](https://github.com/tugbaaak/speedtest.git)´ = https://github.com/tugbaaak/speedtest.git