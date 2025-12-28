# 🏭 Industrial-Defect-DeepVision: PCB Yüzey Hataları İçin Derin Öğrenme Çözümü

<div align="center">

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![YOLOv13](https://img.shields.io/badge/YOLOv13-SOTA-blue?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![ResNet](https://img.shields.io/badge/ResNet-Hybrid-orange?style=for-the-badge)](https://arxiv.org/abs/1512.03385)
[![Industry 4.0](https://img.shields.io/badge/Industry-4.0-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution)
[![A100](https://img.shields.io/badge/NVIDIA-A100-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/data-center/a100/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Industrial-Defect-DeepVision**, elektronik üretim endüstrisinde (PCB) kalite kontrol süreçlerini otomatize etmek için geliştirilmiş; **Hibrit Sınıflandırma (ResNet)** ve **Nesne Tespiti (YOLO)** mimarilerini karşılaştıran kapsamlı bir **Otomatik Optik Denetim (AOI)** projesidir.

Bu çalışma; insan gözünden kaçabilen mikroskobik üretim hatalarını tespit etmek için farklı çözünürlük stratejilerini (640px vs 960px) ve donanım limitlerini **NVIDIA A100** üzerinde test ederek, endüstriyel kullanım için **en optimum (verimli)** çözümü sunar.

---

![624ac40503a5276b4daf4279_PCB-Assembly-Visual-Inspection (1)](https://github.com/user-attachments/assets/6a2f8e48-c292-43d4-a2ef-d29e342824dc)

## 🌍 Projenin Amacı ve Endüstriyel Motivasyon

Endüstri 4.0 standartlarında, üretim hatları çok yüksek hızlarda çalışmaktadır. Geleneksel manuel kontrol ve eski nesil yöntemler şu dezavantajlara sahiptir:
* **Yüksek Maliyet & Hata Riski:** İnsan gözü yorulabilir ve mikroskobik hataları kaçırabilir.
* **Hız Darboğazı:** Seri üretim hızına (Real-Time) yetişememe.

Bu proje, bu sorunları çözmek amacıyla; **Classification (Sınıflandırma)** ve **Detection (Tespit)** yaklaşımlarını kıyaslamış ve **Gerçek Zamanlı Edge (Uç) Sistemler** için en uygun mimariyi belirlemiştir.

---

## 🔍 Tespit Edilen Kritik Hatalar
Proje, **PCB Defect Dataset** (10.668 Görüntü) kullanılarak endüstride en sık karşılaşılan 6 hatayı tespit etmektedir.

> **⚠️ Kritik Veri Kısıtı:** Orijinal veri setindeki görüntülerin çözünürlüğü **600x600** pikseldir. Bu durum, "Spur" gibi 3-4 piksellik hataların tespitini zorlaştıran temel faktördür.

| Hata Sınıfı | Endüstriyel Tanım |
| :--- | :--- |
| **0 - Mouse Bite** | PCB kenarında, malzeme yorgunluğu veya kesim hatası kaynaklı çentikler. |
| **1 - Spur** | Devre yollarında istenmeyen, kısa devre riski taşıyan kıl inceliğinde bakır uzantıları. *(En zor sınıf)*. |
| **2 - Missing Hole** | Montaj aşamasını engelleyen, delinmemiş via veya komponent delikleri. |
| **3 - Short** | Kritik devre hatası; iki iletken hattın kazara birleşmesi. |
| **4 - Open Circuit** | İletim hattının kopması sonucu oluşan elektriksel kesinti. |
| **5 - Spurious Copper** | Tasarımda olmayan, kimyasal aşındırma sonrası kalan bakır artıkları. |

---

![val_batch0_pred_640_640](https://github.com/user-attachments/assets/d90f1ce9-3cdc-4e39-9550-7fbc9091ffb9)

## ⚙️ Teknik Mimari ve Yöntem Karşılaştırması

Bu çalışmada iki farklı derin öğrenme yaklaşımı test edilmiştir:

### 1. Yaklaşım: Hibrit Sınıflandırma (ResNet-50)
* **Yöntem:** `Resnet_pcbipynb.ipynb` dosyasında uygulanan bu yöntemde, şüpheli bölgeler **ROI Cropping** ile kesilip ResNet modeline sorulmuştur.
* **Sonuç:** Hata "sınıflandırma" başarısı yüksektir ancak **Bölge Öneri Ağı (RPN)** gerektirdiği için sistem yavaştır (Two-Stage Detector problemi).

<img width="1572" height="889" alt="image" src="https://github.com/user-attachments/assets/5b811c67-e19b-4f5c-aec9-2853ae3b5767" />



### 2. Yaklaşım: Tek Aşamalı Tespit (YOLOv13) - **(SEÇİLEN YÖNTEM)**
* **Yöntem:** Hatanın hem sınıfını hem konumunu tek seferde (Single-Stage) bulur.
* **Avantaj:** RPN katmanına ihtiyaç duymaz, üretim bandı hızına (Real-Time) uygundur.

---
![yolo](https://github.com/user-attachments/assets/05c82051-0d7d-499c-b2df-718c8cc5b228)

## 🔬 Deneysel Süreç: 640px vs 960px (A100 Challenge)

Projenin en kritik aşamasında, NVIDIA A100 donanımı kullanılarak çözünürlüğün etkisi analiz edilmiştir.

### Donanım Altyapısı
* **GPU:** NVIDIA A100-SXM4 (80GB VRAM).
* **RAM:** 167 GB (Veri önbellekleme için).

![NVIDIA-researchers-use-AI-to-design-better-arithmetic-circuits-that-power-our-AI-chips](https://github.com/user-attachments/assets/2d5d5a85-f87b-4658-a065-0225bb8427d3)

### Senaryo Karşılaştırması ve Sonuçlar

### Senaryo Karşılaştırması ve Sonuçlar

| Özellik | Senaryo A: 640px (Baseline) | Senaryo B: 960px (High-Res) |
| :--- | :--- | :--- |
| **Kod Dosyası** | `code_640x640.ipynb` | `code_960x960.ipynb` |
| **Donanım Yükü** | ~54.4GB VRAM @ Batch 109  |~56GB VRAM @ Batch 38  |
| **Eğitim Süresi** | **1.07 Saat** (Çok Hızlı) | **2.97 Saat** (Yavaş)  |
| **Mozaik Stratejisi** | ✅ Var (Mozaik + Kademeli Kapatma) | ✅ Var (Mozaik + Kademeli Kapatma) |
| **Precision (Kesinlik)**| **0.969** (Çok Yüksek)  | 0.966 (Benzer)|
| **Recall (Yakalama)** | **%46** (Stabil) |%45.9 (İyileşme Yok)  |
| **Durum** | **✅ OPTİMUM ÇÖZÜM** |❌ VERİMSİZ   |

> **🧪 Bilimsel Bulgular:**
> 1.  **Veri Doygunluğu:** Orijinal veriler **600x600 px** olduğu için , görüntüleri 960px'e çıkarmak (Upscaling) modele gerçek detay kazandırmamış, aksine interpolasyon gürültüsü oluşmuştur.
> 2.  **Maliyet/Performans:** 960px eğitimi, donanımı ve süreyi **~3 kat** artırmasına rağmen , **Recall** değerinde istatistiksel olarak anlamlı bir artış sağlamamıştır.


---

## 📂 Depo Yapısı ve Dosyalar

Proje dosyaları aşağıdaki yapıdadır:

* `Resnet_pcbipynb.ipynb`: ResNet-50 tabanlı sınıflandırma.
* `code_640x640.ipynb`: **Final Model.** Endüstriyel standartta (640px) eğitilen, optimize edilmiş YOLOv13 kodu.
* `code_960x960.ipynb`: A100 üzerinde yapılan deneysel yüksek çözünürlük çalışması.
* `rename_dataset.py`: Veri seti etiketlerini ve dosya isimlerini düzenleyen yardımcı script.

---

## 🚀 Sonuç ve Endüstriyel Entegrasyon

Yapılan kapsamlı testler sonucunda; **640px YOLOv13** modeli projenin nihai çözümü olarak belirlenmiştir.

* **Edge (Uç) Uyumluluğu:** 640px model, **NVIDIA Jetson Xavier / Orin Nano** gibi uç cihazlarda **30+ FPS** hızla çalışabilir.
* **Dağıtım:** Model, üretim hattına entegrasyon için **TensorRT** veya **ONNX** formatına dönüştürülmeye hazırdır.
---

<img width="1410" height="732" alt="Ekran görüntüsü 2025-12-28 153942" src="https://github.com/user-attachments/assets/c28b50fc-12c1-44b8-99b8-72953e102835" />


## 🛠️ Kurulum

```bash
# 1. Repoyu klonlayın
git clone [https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git](https://github.com/sadikgolpekk/Industrial-Defect-DeepVision.git)
cd Industrial-Defect-DeepVision

# 2. Gerekli kütüphaneleri yükleyin
pip install ultralytics torch torchvision

# 3. Final modeli (640px) eğitmek için
# code_640x640.ipynb notebook dosyasını çalıştırın veya script'e çevirin.
