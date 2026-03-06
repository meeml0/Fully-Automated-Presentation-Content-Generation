---
name: latex-beamer-zebra-syllabus-table
description: LaTeX Beamer sunumlarında haftalık ders planı/syllabus tablolarını belirli bir zebra stilinde üretmek ve mevcut tabloları aynı stile dönüştürmek. Triggers: haftalık ders planı, syllabus table, zebra tablo, beamer tablo, ara sınav satırını vurgula, final satırını kırmızı yap, mevcut tabloyu bu stile çevir.
---

# LaTeX Beamer Zebra Syllabus Table

Bu skill, LaTeX Beamer sunumlarında haftalık ders planı (syllabus) tablolarını standart bir "zebra" stilinde (alternatif renkli satırlar) üretmek veya mevcut tabloları bu stile dönüştürmek için kullanılır.

## Özellikler ve Kurallar

Bu skill kullanıldığında aşağıdaki kurallara kesinlikle uyulmalıdır:

- Beamer içinde `frame` tabanlı syllabus tablosu üretilmelidir.
- Tablo hizalaması için `\centering` kullanılmalıdır.
- Tabloyu slayta sığdırmak için `\resizebox` kullanılmalıdır (örn: `\resizebox{0.65\textwidth}{!}{...}`).
- Zebra boyama için `\rowcolors{2}{gray!10}{white}` kullanılmalıdır.
- Özel satır vurguları için `\rowcolor` kullanılmalıdır (ör. ara sınav için `yellow!20`, final için `red!10`).
- Tablo çizgileri için `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) kullanılmalıdır. Dikey çizgi kullanılmamalıdır.
- Sütun yapısı genelde `c l l` şeklinde olmalıdır.
- Türkçe karakter sorunları (bozuk karakterler) düzeltilmelidir.
- Mevcut bir tablo dönüştürülürken kullanıcı **içeriği bozulmamalı**, sadece tablo stili standardize edilmelidir.

## Örnek Varsayılan Stil (Kalıp)

Aşağıdaki kalıp, varsayılan stil olarak kabul edilmeli ve birebir uygulanmalıdır:

```latex
\begin{frame}{Haftalık Ders Planı (Syllabus)}
    \centering
    \resizebox{0.65\textwidth}{!}{
    \rowcolors{2}{gray!10}{white}
    \begin{tabular}{c l l}
        \toprule
        \textbf{Hafta} & \textbf{Konu} & \textbf{Araçlar/Notlar} \\
        \midrule
        1 & ... & (Bu Hafta) \\
        2 & ... & \\
        \rowcolor{yellow!20} 8 & \textbf{Ara Sınav} & \\
        \rowcolor{red!10} 15 & \textbf{Genel Sınav} & \\
        \bottomrule
    \end{tabular}
    }
\end{frame}
```
