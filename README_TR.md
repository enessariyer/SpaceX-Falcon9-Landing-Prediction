# SpaceX Falcon 9 Landing Prediction Project 🚀

Bu proje, SpaceX'in Falcon 9 fırlatmalarındaki ilk aşama iniş başarısını tahmin etmek amacıyla uçtan uca bir veri bilimi iş akışını kapsamaktadır. Fiyat farklarını ve başarı oranlarını analiz ederek, bir fırlatmanın maliyetini ve riskini öngörmeyi hedefler.

## 📁 Proje Yapısı

| Dosya / Klasör | Açıklama |
| :--- | :--- |
| `notebooks/` | Veri toplama, görselleştirme ve makine öğrenmesi süreçlerini içeren Jupyter Notebooklar. |
| `images/` | Sunum ve README için kullanılan analiz grafiklerinin çıktıları. |
| `scripts/` | Dash interaktif web uygulaması kodu. |
| `requirements.txt` | Projenin çalışması için gerekli kütüphane listesi. |

---

## 🛠️ Kullanılan Teknolojiler

* **Diller:** Python 3.x
* **Veri Analizi:** Pandas, NumPy
* **Görselleştirme:** Matplotlib, Seaborn, Folium, Plotly Dash
* **Veritabanı:** SQL / PostgreSQL
* **Makine Öğrenmesi:** Scikit-Learn (Logistic Regression, SVM, Decision Tree, KNN)

---

## 🚀 Analiz Adımları

### 1. Veri Toplama ve Hazırlama
* SpaceX API'si ve web scraping yöntemleriyle fırlatma verileri toplandı.
* Eksik veriler giderildi ve SQL sorguları ile temel analizler yapıldı.

### 2. Keşifçi Veri Analizi (EDA)
Fırlatma sahaları, yük miktarı (Payload Mass) ve yörünge (Orbit) tiplerine göre başarı oranları analiz edildi.
> ![Launch Site vs Payload](images/launchsite_vs_payload.png)

### 3. İnteraktif Görselleştirme
**Folium** kullanılarak fırlatma sahalarının harita üzerindeki konumları ve **Plotly Dash** ile interaktif başarı analiz paneli oluşturuldu.

### 4. Makine Öğrenmesi (ML)
Veriler standartlaştırıldı (StandardScaler) ve en iyi hiperparametreleri bulmak için `GridSearchCV` kullanıldı. 
* **En İyi Model:** Decision Tree
* **Doğruluk Oranı (Accuracy):** %83.3

---

## 🏁 Sonuçlar ve Değerlendirme (Conclusion)

Bu proje sonucunda, SpaceX Falcon 9 iniş başarılarını etkileyen temel faktörler hakkında şu çıkarımlara ulaşıldı:

* **Fırlatma Sahası Dinamikleri:** KSC LC-39A sahası, diğer sahalara kıyasla en yüksek başarı oranına sahiptir. VAFB SLC-4E ise kutupsal yörünge fırlatmalarında kritik bir rol oynamaktadır.
* **Yük Ağırlığı Etkisi:** Analizler, 2000kg - 5000kg arası yük ağırlıklarının (Payload Mass) iniş başarısı için en "optimum" aralık olduğunu göstermektedir. 8000kg ve üzeri fırlatmalarda riskin arttığı gözlemlenmiştir.
* **Yörünge Başarısı:** LEO (Alçak Dünya Yörüngesi) fırlatmaları, iniş başarısı açısından en yüksek yüzdeye sahipken, GTO fırlatmaları daha düşük bir başarı oranına sahiptir.
* **Model Performansı:** Eğitilen makine öğrenmesi modelleri arasında **Decision Tree**, test setinde %83.3 doğruluk ile en istikrarlı sonucu vermiştir.
* **Maliyet Analizi:** İniş başarısının önceden tahmin edilebilmesi, SpaceX'in roketleri yeniden kullanabilme (reusability) stratejisi için kritik olan fırlatma maliyetlerini yaklaşık %70 oranında azaltma potansiyelini doğrular niteliktedir.

---