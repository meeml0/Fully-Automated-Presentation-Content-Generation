---
name: create_weekly_presentation
description: Yeni bir haftalık sunum oluşturmak istendiğinde temel şablonu kopyalayarak yeni sunumu yapılandırır.
---

# Yeni Haftalık Sunum Oluşturma (Create Weekly Presentation)

**Tetikleyici (Trigger):** Kullanıcı "yeni bir sunum yarat", "yeni hafta sunumunu oluştur" veya benzer bir komutla yeni içerik talep ettiğinde devreye girer.

## Uygulama Adımları

Kullanıcı yeni bir sunum oluşturmanı istediğinde **asla sıfırdan kod yazmaya başlama**. KESİNLİKLE aşağıdaki süreci izle:

### 1. Şablonu Kopyala (Zorunlu İlk Adım)
- **Kaynak dosya:** `c:\Users\ufuka\Desktop\Olasılık\temel sunum yapısı.tex`
- Bütün değişikliklerden önce `run_command` aracıyla (Örn: PowerShell) şablon dosyasını yeni haftanın adıyla kopyala.
- **Örnek Komut:** `Copy-Item "c:\Users\ufuka\Desktop\Olasılık\temel sunum yapısı.tex" "c:\Users\ufuka\Desktop\Olasılık\8-hafta-olasilik.tex"`

### 2. Dosya İçi Metadata Güncelleme
- Kopyalayarak elde ettiğin yeni `.tex` dosyasını düzenlemeye başla.
- `\subtitle{Hafta X: ...}` alanını kullanıcının belirttiği haftaya ve başlığa göre güncelle.

### 3. İçerik ve Gövde Entegrasyonu
- Şablonda hazır bulunan `\section`, `\subsection` ve `\begin{frame} ... \end{frame}` iskeletlerine sadık kalarak kullanıcının istediği konuyu yerleştir.
- Sisteminize tanımlanmış olan `Olasılık Sunum Kuralları`nı (MEMORY kurallarını), özellikle "overlay (<1->)", kolon (`[T]`) ve görsel taşmama kurallarını kusursuz uyguladığından emin ol.
- Kullanıcıdan gelen soruları veya anlatımları boş frame iskeletlerinin içine doldur. Gerekmiyorsa şablondaki fazla taslak bölümlerini temizle.

### 4. Bütünlüğü Koruma
- Tüm sunumlarda standart olan sayfa yapısını (`İçindekiler` ve kapanıştaki `Yapay Zeka Asistanı`, `Bizi Takip Edin!` slaytları) kullanıcı silmeni özellikle istemedikçe **KESİNLİKLE KORU**.
- Sonunda projenin hata vermeden derlenebildiğini doğrula.
