# 🏭 Industrial-Defect-DeepVision: PCB Yüzey Hataları İçin Derin Öğrenme Çözümü

<div align="center">

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![YOLOv13](https://img.shields.io/badge/YOLOv13-SOTA-blue?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![ResNet](https://img.shields.io/badge/ResNet-Hybrid-orange?style=for-the-badge)](https://arxiv.org/abs/1512.03385)
[![Industry 4.0](https://img.shields.io/badge/Industry-4.0-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution)
[![A100](https://img.shields.io/badge/NVIDIA-A100-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/data-center/a100/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Industrial-Defect-DeepVision**, elektronik üretim endüstrisinde (PCB) kalite kontrol süreçlerini otomatize etmek için geliştirilmiş; [cite_start]**Hibrit Sınıflandırma (ResNet)** ve **Nesne Tespiti (YOLO)** mimarilerini karşılaştıran kapsamlı bir **Otomatik Optik Denetim (AOI)** projesidir[cite: 5, 9, 12].

[cite_start]Bu çalışma; insan gözünden kaçabilen mikroskobik üretim hatalarını tespit etmek için farklı çözünürlük stratejilerini (640px vs 960px) ve donanım limitlerini **NVIDIA A100** üzerinde test ederek, endüstriyel kullanım için **en optimum (verimli)** çözümü sunar[cite: 156, 157, 275].

---

![624ac40503a5276b4daf4279_PCB-Assembly-Visual-Inspection (1)](https://github.com/user-attachments/assets/6a2f8e48-c292-43d4-a2ef-d29e342824dc)

## 🌍 Projenin Amacı ve Endüstriyel Motivasyon

Endüstri 4.0 standartlarında, üretim hatları çok yüksek hızlarda çalışmaktadır. Geleneksel manuel kontrol ve eski nesil yöntemler şu dezavantajlara sahiptir:
* [cite_start]**Yüksek Maliyet & Hata Riski:** İnsan gözü yorulabilir ve mikroskobik hataları kaçırabilir[cite: 11].
* [cite_start]**Hız Darboğazı:** Seri üretim hızına (Real-Time) yetişememe[cite: 46].

Bu proje, bu sorunları çözmek amacıyla; [cite_start]**Classification (Sınıflandırma)** ve **Detection (Tespit)** yaklaşımlarını kıyaslamış ve **Gerçek Zamanlı Edge (Uç) Sistemler** için en uygun mimariyi belirlemiştir[cite: 324, 325, 326].

---

## 🔍 Tespit Edilen Kritik Hatalar
[cite_start]Proje, **PCB Defect Dataset** (10.668 Görüntü) kullanılarak endüstride en sık karşılaşılan 6 hatayı tespit etmektedir[cite: 23, 24].

> [cite_start]**⚠️ Kritik Veri Kısıtı:** Orijinal veri setindeki görüntülerin çözünürlüğü **600x600** pikseldir[cite: 32]. [cite_start]Bu durum, "Spur" gibi 3-4 piksellik hataların tespitini zorlaştıran temel faktördür[cite: 34].

| Hata Sınıfı | Endüstriyel Tanım |
| :--- | :--- |
| **0 - Mouse Bite** | [cite_start]PCB kenarında, malzeme yorgunluğu veya kesim hatası kaynaklı çentikler[cite: 26]. |
| **1 - Spur** | Devre yollarında istenmeyen, kısa devre riski taşıyan kıl inceliğinde bakır uzantıları. [cite_start]*(En zor sınıf)*[cite: 27]. |
| **2 - Missing Hole** | [cite_start]Montaj aşamasını engelleyen, delinmemiş via veya komponent delikleri[cite: 28]. |
| **3 - Short** | [cite_start]Kritik devre hatası; iki iletken hattın kazara birleşmesi[cite: 29]. |
| **4 - Open Circuit** | [cite_start]İletim hattının kopması sonucu oluşan elektriksel kesinti[cite: 30]. |
| **5 - Spurious Copper** | [cite_start]Tasarımda olmayan, kimyasal aşındırma sonrası kalan bakır artıkları[cite: 31]. |

---

![val_batch0_pred_640_640](https://github.com/user-attachments/assets/d90f1ce9-3cdc-4e39-9550-7fbc9091ffb9)

## ⚙️ Teknik Mimari ve Yöntem Karşılaştırması

[cite_start]Bu çalışmada iki farklı derin öğrenme yaklaşımı test edilmiştir[cite: 37]:

### 1. Yaklaşım: Hibrit Sınıflandırma (ResNet-50)
* [cite_start]**Yöntem:** `Resnet_pcbipynb.ipynb` dosyasında uygulanan bu yöntemde, şüpheli bölgeler **ROI Cropping** ile kesilip ResNet modeline sorulmuştur[cite: 38, 40].
* [cite_start]**Sonuç:** Hata "sınıflandırma" başarısı yüksektir ancak **Bölge Öneri Ağı (RPN)** gerektirdiği için sistem yavaştır (Two-Stage Detector problemi)[cite: 44, 45, 46].

### 2. Yaklaşım: Tek Aşamalı Tespit (YOLOv13) - **(SEÇİLEN YÖNTEM)**
* [cite_start]**Yöntem:** Hatanın hem sınıfını hem konumunu tek seferde (Single-Stage) bulur[cite: 41, 42].
* [cite_start]**Avantaj:** RPN katmanına ihtiyaç duymaz, üretim bandı hızına (Real-Time) uygundur[cite: 48, 49].

---

## 🔬 Deneysel Süreç: 640px vs 960px (A100 Challenge)

Projenin en kritik aşamasında, NVIDIA A100 donanımı kullanılarak çözünürlüğün etkisi analiz edilmiştir.

### Donanım Altyapısı
* [cite_start]**GPU:** NVIDIA A100-SXM4 (80GB VRAM)[cite: 156].
* **RAM:** 167 GB (Veri önbellekleme için).

![NVIDIA-researchers-use-AI-to-design-better-arithmetic-circuits-that-power-our-AI-chips](https://github.com/user-attachments/assets/2d5d5a85-f87b-4658-a065-0225bb8427d3)

### Senaryo Karşılaştırması ve Sonuçlar

| Özellik | Senaryo A: 640px (Baseline) | Senaryo B: 960px (High-Res) |
| :--- | :--- | :--- |
| **Kod Dosyası** | `code_640x640.ipynb` | `code_960x960.ipynb` |
| **Donanım Yükü** | [cite_start]Düşük (~54.4GB VRAM @ Batch 109) [cite: 161] | [cite_start]Çok Yüksek (~56GB VRAM @ Batch 38) [cite: 266] |
| **Eğitim Süresi** | [cite_start]**1.07 Saat** (Çok Hızlı) [cite: 160] | [cite_start]**2.97 Saat** (Yavaş) [cite: 266] |
| **Mozaik Stratejisi** | Standart | [cite_start]Kademeli Kapatma (Close Mosaic=10) [cite: 268] |
| **Recall (Başarım)** | [cite_start]%46 (Stabil) [cite: 165] | [cite_start]%45.9 (İyileşme Yok) [cite: 270] |
| **Durum** | **✅ OPTİMUM ÇÖZÜM** | [cite_start]❌ VERİMSİZ (Diminishing Returns) [cite: 258] |

> **🧪 Bilimsel Bulgular:**
> [cite_start]1.  **Veri Doygunluğu:** Orijinal veriler 600px olduğu için, 960px'e upscaling yapmak modele gerçek detay kazandırmamış, aksine interpolasyon gürültüsünü öğrenmesine (Overfitting) neden olmuştur[cite: 273, 274].
> [cite_start]2.  **Maliyet/Performans:** 960px eğitimi donanımı 3 kat daha fazla yormasına rağmen Recall değerinde anlamlı bir artış sağlamamıştır[cite: 277, 278].

---

## 📂 Depo Yapısı ve Dosyalar

Proje dosyaları aşağıdaki yapıdadır:

* `Resnet_pcbipynb.ipynb`: ResNet-50 tabanlı sınıflandırma ve hibrit denemeler.
* `code_640x640.ipynb`: **Final Model.** Endüstriyel standartta (640px) eğitilen, optimize edilmiş YOLOv13 kodu.
* `code_960x960.ipynb`: A100 üzerinde yapılan deneysel yüksek çözünürlük çalışması.
* `rename_dataset.py`: Veri seti etiketlerini ve dosya isimlerini düzenleyen yardımcı script.

---

## 🚀 Sonuç ve Endüstriyel Entegrasyon

Yapılan kapsamlı testler sonucunda; [cite_start]**640px YOLOv13** modeli projenin nihai çözümü olarak belirlenmiştir[cite: 279, 280].

* [cite_start]**Edge (Uç) Uyumluluğu:** 640px model, **NVIDIA Jetson Xavier / Orin Nano** gibi uç cihazlarda **30+ FPS** hızla çalışabilir[cite: 329, 330].
* [cite_start]**Dağıtım:** Model, üretim hattına entegrasyon için **TensorRT** veya **ONNX** formatına dönüştürülmeye hazırdır[cite: 331].

---

## 🛠️ Kurulum

```bash
# 1. Repoyu klonlayın
git clone [https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git](https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git)
cd Industrial-Defect-DeepVision

# 2. Gerekli kütüphaneleri yükleyin
pip install ultralytics torch torchvision

# 3. Final modeli (640px) eğitmek için
# code_640x640.ipynb notebook dosyasını çalıştırın veya script'e çevirin.
