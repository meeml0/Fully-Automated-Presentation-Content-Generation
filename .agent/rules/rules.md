---
trigger: always_on
---

# Olasılık Sunum Kuralları

Bu kurallar `Olasılık` klasöründeki haftalık beamer sunumlarının ortak yapısından türetilmiştir.
Amaç genel LaTeX tavsiyesi vermek değil, bu projedeki sunum dilini ve iskeletini korumaktır.

## 1. Temel Şablon

- Sunumlar `\documentclass[light]{lutbeamer}` ile yazılır.
- Ana ders kimliği korunur:
  - `\title{MATH 204 -- Olasılık ve İstatistik}`
  - uygun hafta başlığı için `\subtitle{Hafta X: ...}`
- Bibliyografya varsa `biblatex + biber` düzeni korunur ve `\addbibresource{references.bib}` kullanılır.
- Paket ekleme konusunda muhafazakar ol:
  - Mevcut yapıda sık görülen paketler: `pgfpages`, `ragged2e`, `booktabs`, `amssymb`, `fontawesome5`, `tikz`, `pgfplots`
  - Yeni paket sadece gerçekten gerekliyse eklenir.

## 2. Açılış ve Kapanış İskeleti

- Açılışta tipik sıra korunur:
  1. logolu ya da görselli tam kapak frame’i
  2. `\maketitle{}`
  3. `İçindekiler` frame’i
- `\setbeamertemplate{navigation symbols}{}` korunur.
- Tüm sunumlarda bölüm başlarında otomatik akış frame’i vardır; `\AtBeginSection[]{...}` yapısını bozma.
- Kapanışta mümkünse şu yapı korunur:
  - özet / çıkış bileti
  - kaynaklar
  - gerekiyorsa haftalık uygulama veya yapay zeka asistanı frame’i
  - en sonda `plain,noframenumbering` kapanış frame’i

## 3. Bölüm Akışı

- Sunumlar `section` ve `subsection` mantığıyla ilerler.
- Her ana konu genelde şu pedagojik zinciri izler:
  1. motivasyon veya kavramsal giriş
  2. tanım / temel fikir
  3. kısa örnek veya uygulama
  4. pekiştirme sorusu
  5. çözüm
- Kullanıcı özellikle istemedikçe konuları sadece formül yığını olarak verme.
- Haftalar arası köprü kur:
  - “Hafta X’ten ne getiriyoruz?”
  - “Bu hafta neyi ölçeceğiz / öğreneceğiz?”
  - “Bir sonraki haftaya köprü”

## 4. Frame Tasarım Kuralları

- Varsayılan olarak kısa ve yoğun frame yaz.
- Bir frame tek ana fikir taşısın.
- Uzun soru veya çözüm tek frame’e sıkıştırılmamalı:
  - gerekirse `Soru`
  - sonra `Çözüm`
  - çok uzunsa `Detaylı Çözüm`
- `columns` kullanıldığında tercih edilen yapı:

```latex
\begin{columns}[T]
  \begin{column}{0.48\textwidth}
    ...
  \end{column}
  \begin{column}{0.48\textwidth}
    ...
  \end{column}
\end{columns}
```

- Yaygın kolon genişlikleri:
  - `0.48 / 0.48` iki kolon için
  - `0.62 / 0.35` görsel + açıklama türü yerleşimler için
- Top hizalama için `[T]` tercih edilir.
- İçerik taşacaksa önce metni sadeleştir, sonra `\small` veya `\scriptsize` kullan.

## 5. Block Kullanımı

- `block`: tanım, temel fikir, senaryo, çözüm adımı
- `exampleblock`: örnek, uygulama, mühendislik vakası, soru
- `alertblock`: gerçekten vurgulanması gereken sonuç, kritik yorum, sık hata, karar mesajı
- `alertblock` kullanımı yasak değil; bu projede bilinçli vurgu için kullanılıyor.
- Aynı frame içinde bloklar çoğu zaman şu düzenle akar:
  - solda açıklama / soru
  - sağda çözüm / yorum

## 6. Dil ve Ton

- Tüm içerik Türkçe yazılır.
- Teknik terimler gerektiğinde İngilizcesi parantez içinde verilebilir:
  - örn. `Birikimli Dağılım Fonksiyonu (CDF)`
- Dil öğretici ama mekanik olmayan olmalı.
- Sık kullanılan ifade türleri:
  - `Motivasyon`
  - `Kavramsal köprü`
  - `Uygulama`
  - `Yorum`
  - `Sık hata`
  - `Çıkış bileti`
- Anlatım sadece tanım vermemeli; yorum ve karar bağlamı da içermeli.

## 7. Örnek ve Soru Politikası

- Sorular mümkün olduğunca mühendislik, üretim, kalite kontrol, yazılım, elektronik, sistem güvenilirliği gibi bağlamlarla yazılmalı.
- Soru yerleşimi konu anlatımının hemen arkasından gelmeli.
- Kısa soru/çözüm için iki kolonlu tek frame kullanılabilir.
- Uzun sorularda ayrı frame aç:
  - `Soru n: ...`
  - `Soru n: Çözüm`
  - gerekiyorsa `Soru n: Detaylı Çözüm`
- Çözüm sadece işlem vermemeli; son satırda kısa yorum içermeli.

## 8. Matematik Yazımı

- Matematiksel anlatım sade ve ders anlatımına uygun olmalı.
- Gereksiz numaralı denklem kullanma; çoğu durumda `\[...\]`, `align*`, `aligned` yeterlidir.
- Uzun eşitlikleri tek satırda taşırma:
  - satır kır
  - `aligned` kullan
  - gerekiyorsa yazıyı küçült
- Metin içi matematik kısa tutulmalı.
- Sonuçlar mümkünse yorumlanmalı:
  - sadece sayı değil, ne anlama geldiği de yazılmalı.

## 9. Fragile ve Özel Yapılar

- `fragile` sadece gerçekten gerektiğinde kullanılmalı.
- Bu projede `fragile` en çok şu durumlarda görülür:
  - verbatim benzeri içerik
  - hassas matematik / özel yapı kombinasyonları
  - quiz veya özel formatlı frame’ler
- Her frame’e refleks olarak `fragile` ekleme.

## 10. Görsel ve TikZ Kullanımı

- Görseller anlatımı desteklemeli; süs için eklenmemeli.
- `tikz` ve `pgfplots` aktif olarak kullanılıyor; mevcut görsel dil korunmalı.
- Genişlikler çoğunlukla bağlama göre verilir:
  - `\textwidth`
  - `\linewidth`
  - `\paperwidth / \paperheight` kapaklarda
- Görsel içeren frame’lerde genelde bir taraf açıklama, diğer taraf görseldir.

## 11. İçindekiler ve Akış Sayfaları

- `İçindekiler` frame’i genelde iki kolonlu verilir.
- `\tableofcontents` için section grupları haftaya göre bölünebilir.
- Uzun sunumlarda bölüm başlangıçlarında `Sunum Akışı` veya `Sunum Planı` frame’i kullanılmalıdır.

## 12. Kaynaklar ve Son Bölümler

- Kaynaklar frame’i genelde:

```latex
\begin{frame}[allowframebreaks]{Kaynaklar}
```

- `allowframebreaks` esas olarak kaynaklar ve gerçekten uzun detaylı çözüm frame’lerinde kullanılabilir.
- Projede bazı haftalarda `Yapay Zeka Asistanınız: NotebookLM` benzeri kapanış frame’leri var; kullanıcı aksini istemedikçe bu çizgi korunabilir.

## 13. Yasak veya Kaçınılacak Davranışlar

- Genel amaçlı, şablondan kopuk beamer tavsiyeleri dayatma.
- `Madrid`, `beaver` gibi başka tema önerileri getirme; mevcut tema `lutbeamer`.
- Her yere aşırı `\pause`, overlay veya animasyon ekleme.
- İçeriği sırf kısa olsun diye pedagojik akışı bozma.
- Uzun paragrafı küçücük puntoda tek frame’e gömme.
- Mühendislik bağlamı istenmişken soyut ve bağlamsız örnekler yazma.
- `alertblock` kullanımını tamamen yasaklama; bu projede meşru kullanım alanı var.
- Kullanıcı istemedikçe dosyanın tamamını yeniden yazma/reformat etme.
- Kullanıcı istemedikçe `.tex` dosyasında toplu bul-değiştir (global replace) yapma.
- `.tex` dosyalarını script ile otomatik yeniden üretme/rewrite etme.

## 14. Yeni Hafta Üretirken İzlenecek Kalıp

- Yeni hafta hazırlarken mümkünse şu omurga kullan:
  1. kapak
  2. içindekiler
  3. önceki haftadan köprü / motivasyon
  4. kavram haritası veya öğrenme hedefi
  5. ana bölüm 1
  6. ilgili soru ve çözüm
  7. ana bölüm 2
  8. ilgili soru ve çözüm
  9. özet / mini-quiz / çıkış bileti
  10. kaynaklar
  11. gerekiyorsa AI asistanı / kapanış

## 15. Ajan İçin Son Kontrol Listesi

- Bu hafta başlığı ve ders kimliği doğru mu?
- Açılış sırası bozuldu mu?
- Section/subsection yapısı korunuyor mu?
- Konu anlatımı hemen ardından örnek veya soru geliyor mu?
- Sorular mühendislik bağlamlı mı?
- Uzun çözüm gerekiyorsa ayrı frame açıldı mı?
- İki kolonlu frame’lerde genişlikler güvenli mi?
- Taşma riski olan frame’ler sadeleştirildi mi?
- Kapanışta özet ve kaynaklar var mı?
- Yeni içerik mevcut haftaların tonuyla uyumlu mu?

## 16. Karakter ve Encoding Güvenliği (KIRMIZI ÇİZGİ)

Bu bölüm zorunludur. İhlal edilirse değişiklik geçersiz sayılır.

- Bu projedeki `.tex`, `.bib`, `.md` metin dosyaları UTF-8 olarak korunur.
- Türkçe karakterler aynen korunur: `ı İ ş Ş ğ Ğ ü Ü ö Ö ç Ç`.
- Türkçe metinleri ASCII'ye dönüştürmek yasak:
  - `ş -> s`, `ğ -> g`, `ü -> u`, `ö -> o`, `ç -> c`, `ı -> i` gibi sadeleştirme yapılamaz.
- Mojibake/bozuk encoding çıktıları kesinlikle yasak:
  - `Ã`, `Ä`, `Å`, `â€™`, `â€œ`, `â€`, `ÅŸ`, `Ä±` vb.
- Normal metin içinde Unicode escape/entity kullanımı yasak:
  - `\u0131`, `&#351;`, `0x...` gibi temsillerle harf yazma.
- Kullanıcı açıkça istemedikçe Python/shell script ile `.tex` dosyasını baştan yazma yasak.
- Düzenleme yöntemi varsayılan olarak hedefli patch olmalı; sadece istenen bölüm değiştirilmeli.
- Kullanıcı istemediği bölgelerde içerik değiştirme, taşıma, yeniden adlandırma yapma.

### 16.1 Zorunlu Doğrulama (Her Düzenleme Sonrası)

- Şüpheli encoding dizilerini tara:
  - `rg -n "Ã|Ä|Å|â€™|â€œ|â€|\\\u0|&#[0-9]{2,5};" *.tex`
- Derleme zinciri doğrulaması yap:
  - `xelatex` (ve gerekiyorsa `biber`) sonrası logda yeni karakter hatası olmamalı.
- Logda aşağıdaki tipte hata varsa teslim etmeden düzelt:
  - `Missing character`
  - `There is no ... in font`

### 16.2 İhlal Durumunda Zorunlu Davranış

- Karakter bozulması tespit edilirse ajan yeni değişikliğe devam etmez.
- Önce bozulmayı geri alır veya son sağlam metne döner.
- Sonra sadece hedef bölge için minimal patch ile tekrar uygular.
