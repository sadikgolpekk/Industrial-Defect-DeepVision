

import os


def isim_degistir(image_yolu,etiket_yolu,prefix):
    gorseller=sorted(os.listdir(image_yolu))
    for i,gorsel in enumerate(gorseller,1):
        isim,ext=os.path.splitext(gorsel)
        yeni_isim=f"{prefix}_{i:04d}"
        os.rename(os.path.join(image_yolu,gorsel),os.path.join(image_yolu,yeni_isim+ext))
        
        etiket=os.path.join(etiket_yolu,isim+".txt")

        if os.path.exists(etiket):
            os.rename(etiket,os.path.join(etiket_yolu,yeni_isim+".txt"))
        print(f"[+] {prefix} klasörü yeniden adlandırıldı ({len(gorseller)} dosya)")



dosya_yolu=fr"C:\Users\sadik\Desktop\KOU CENG 3\Derin Öğrenmenin Temelleri\Project\pcb-defect-dataset"
alt_dosyalar=["train","val","test"]

for a in alt_dosyalar:
    image_yolu=os.path.join(dosya_yolu,a,"images")
    etiket_yolu=os.path.join(dosya_yolu,a,"labels")
    isim_degistir(image_yolu,etiket_yolu,a) 
