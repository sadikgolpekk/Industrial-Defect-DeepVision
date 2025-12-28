# 🏭 Industrial-Defect-DeepVision: PCB Yüzey Hataları İçin Derin Öğrenme Çözümü

<div align="center">

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![YOLOv13](https://img.shields.io/badge/YOLOv13-SOTA-blue?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![Industry 4.0](https://img.shields.io/badge/Industry-4.0-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution)
[![A100](https://img.shields.io/badge/NVIDIA-A100-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/data-center/a100/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Industrial-Defect-DeepVision**, elektronik üretim endüstrisinde (PCB) kalite kontrol süreçlerini otomatize etmek için geliştirilmiş, **YOLOv13** tabanlı bir **Otomatik Optik Denetim (AOI)** projesidir.

Bu çalışma; insan gözünden kaçabilen mikroskobik üretim hatalarını (kılcal kısa devreler, kopuk yollar vb.) tespit etmek için **Yüksek Çözünürlüklü Eğitim (High-Res Training)** ve **Küçük Nesne Tespiti (Small Object Detection)** tekniklerini birleştirir.

---

![624ac40503a5276b4daf4279_PCB-Assembly-Visual-Inspection (1)](https://github.com/user-attachments/assets/6a2f8e48-c292-43d4-a2ef-d29e342824dc)



## 🌍 Projenin Amacı ve Endüstriyel Motivasyon

Endüstri 4.0 standartlarında, üretim hatları çok yüksek hızlarda çalışmaktadır. Geleneksel manuel kalite kontrol yöntemleri şu dezavantajlara sahiptir:
* **Yüksek Maliyet:** İnsan gücüne dayalı kontrol pahalıdır.
* **Hata Riski:** Operatör yorgunluğu nedeniyle hatalar gözden kaçabilir.
* **Darboğaz:** Seri üretim hızına yetişilememesi üretimi yavaşlatır.

Bu proje, bu sorunları çözmek amacıyla, **NVIDIA A100** donanımı üzerinde optimize edilmiş bir Derin Öğrenme modeli ile **gerçek zamanlı ve yüksek hassasiyetli** bir denetim sistemi sunar.

---

## 🔍 Tespit Edilen Kritik Hatalar
Proje, **PCB Defect Dataset** (10.668 Görüntü) kullanılarak endüstride en sık karşılaşılan 6 hatayı tespit etmektedir:

| Hata Sınıfı | Endüstriyel Tanım |
| :--- | :--- |
| **0 - Mouse Bite** | PCB kenarında, malzeme yorgunluğu veya kesim hatası kaynaklı çentikler. |
| **1 - Spur** | Devre yollarında istenmeyen, kısa devre riski taşıyan kıl inceliğinde bakır uzantıları. *(Tespiti en zor sınıftır)* |
| **2 - Missing Hole** | Montaj aşamasını engelleyen, delinmemiş via veya komponent delikleri. |
| **3 - Short** | Kritik devre hatası; iki iletken hattın kazara birleşmesi. |
| **4 - Open Circuit** | İletim hattının kopması sonucu oluşan elektriksel kesinti. |
| **5 - Spurious Copper** | Tasarımda olmayan, kimyasal aşındırma sonrası kalan bakır artıkları. |

---

## ⚙️ Teknik Mimari ve Mühendislik Yaklaşımı

Bu projeyi standart bir yapay zeka uygulamasından ayıran temel optimizasyonlar şunlardır:

### 1. Yüksek Çözünürlüklü Eğitim (960px Stratejisi) 🚀
* **Sorun:** Veri setindeki orijinal görüntüler **600x600** pikseldir. Bu çözünürlükte, 3-4 piksel boyutundaki "Spur" hataları model tarafından gürültü (noise) sanılarak filtrelenmekteydi.
* **Çözüm:** Model girdisi **960x960** piksele (Upscaling) çıkarılarak eğitilmiştir.
* **Sonuç:** Küçük nesnelerin görünürlüğü artırılmış ve özellikle **Recall (Hata Yakalama)** oranında belirgin artış sağlanmıştır.

### 2. Donanım Optimizasyonu (NVIDIA A100) ⚡
Eğitim süreci **Google Colab Pro+** altyapısında, **NVIDIA A100-SXM4 (80GB VRAM)** kullanılarak gerçekleştirilmiştir.
* **AutoBatch:** Dinamik batch boyutu ( ile GPU belleği tam kapasite  kullanılmaya çalışılmıştır.
* **RAM Caching:** Disk darboğazını (I/O Bottleneck) aşmak için veri seti tamamen RAM'e önbelleklenmiştir.


![NVIDIA-researchers-use-AI-to-design-better-arithmetic-circuits-that-power-our-AI-chips](https://github.com/user-attachments/assets/2d5d5a85-f87b-4658-a065-0225bb8427d3)

### 3. Model Seçimi: YOLOv13s
Literatürdeki sınıflandırma (ResNet) modellerinin yerelleştirme (Localization) eksikliğini gidermek için, **Attention (Dikkat)** mekanizmalarını (HyperACE) kendi içinde barındıran **YOLOv13s** mimarisi tercih edilmiştir.

---

## 📊 Deneysel Sonuçlar (Ön Bulgular)

Proje kapsamında "Standart Çözünürlük" ve "Yüksek Çözünürlüklü" eğitim senaryoları karşılaştırılmıştır:

| Metrik | 640px (Baseline) | 960px (Industrial-Optimized) | Değerlendirme |
| :--- | :--- | :--- | :--- |
| **Precision** | Düşük-Orta | **Çok Yüksek (%89+)** | 960px model hataları çok daha net ayırt etmektedir. |
| **Recall** | %46 (Doygunluk Sınırı) | **Artış Eğiliminde** | Yüksek çözünürlük, modelin küçük hataları "gözden kaçırmasını" engellemektedir. |
| **Küçük Nesne Başarısı** | Zayıf | **Güçlü** | Özellikle "Spur" hatalarında tespit başarısı artmıştır. |

*(Detaylı loss grafikleri ve Confusion Matrix eğitim tamamlandığında eklenecektir.)*

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi ortamınızda test etmek için:

```bash
# 1. Repoyu klonlayın
git clone [https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git](https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git)
cd Industrial-Defect-DeepVision

# 2. Gerekli kütüphaneleri yükleyin
pip install ultralytics torch torchvision

# 3. Eğitimi başlatın
python train.py
