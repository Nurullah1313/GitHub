"""
Bu program kameradan aldığı görüntüden istenilen rengi( mavi ) tespit üzerinden  başta tanımlı olan sabit çizginin
başına doğru bir vektör çizer ve bu sabit çizgi ile yapılan açıyı ekranın sol üst köşesine yazar

renk.py dosyası ile aynı klasörde olması gerekir

@NURULLAH ŞAHİN
nurullahs764@gmail.com
"""



import cv2
import numpy as np
import math
import renk as rnk # renk ayırt etme işlemi için verilen kütüphabe

x1 = 0 #vektörün originden gittiği x noktası
y1 = 0 #vektörün originden gittiği y noktası
o1 = 300 #orijin noktasının x i temsil eden nokta
o2 = 300 #orijinin y noktasını temsil eden nokta
kamera = cv2.VideoCapture(0)#kullanılacak kamerayı tanıtıyoruz
a=0
b=0
diziR = [80,149,0,136,255,255]#görüntüde takip edilmesini istediğimiz rengin değerlerini sırasıyla giriyoruz
            # ilk üç parametre düşük değerler sonraki üç parametre yüksek değerler
while True:
    try:# hata olursa eğer kodun durmasını engellemek için
        ret,img = kamera.read()#kameradan görüntüyü alıyoruz
        img = cv2.resize(img,(600,600),interpolation = cv2.INTER_AREA) # görüntünün boyutunu ayarlıyoruz bu kısım kordinat açısından önemli
        img,x,y = rnk.cember_ciz(img,*diziR)#program içine gömdüğümüz renk modülünün içindeki renk ayırd edip çember çizme fonksiyonunu kullanıyoruz
        x1 = int(x)#gelen x değeri kordinat düzleminde kullanılacağı için virgüllü olamaz
        y1 = int(y)#gelen y değeri kordinat düzleminde kullanılacağı için virgüllü olamaz
        # olası bir konum kaybında eski konumunu kullanması için yazılan kod bölümü
        if x1 == 0 and y1 == 0:
            x1 = a
            y1 = b
        a = x1
        b = y1


    except Exception as e:
        pass

    cv2.line(img, (o1, o2), (600, 300), (255, 0, 0), 2)#ekrana sabit bir çizgi atıyoruz sonraki çizginin bu çizgi ile açısı hesaplanacak
    cv2.line(img, (o1, o2), (x1, y1), (0, 255, 0), 2)#ekranda takip edilen nesnenin üzerinden sabit çizginin başlangıcına doğru atılan çizgi
    #ilerde çizginin bölgesini belirlemek için aşşağıdaki değişkenleri tanımlıyoruz
    isaretx = "+"
    isarety = "-"

    #vektörün kordinat düzlemi üzerindeki bölgesini belirlemek için x ve y nin işaretlerine ihtiyacımız var
    if x1 > 300:
        isaretx = "+"
    elif x1 < 300:
        isaretx = "-"
    elif  (x1 == 300) and (y1 < 300):
        isaretx = "90"
    elif  (x1 == 300) and (y1 > 300):
        isaretx = "270"
    elif  (x1 == 300) and (y1 == 300):
        isaretx = "0"
    if y1 > 300:
        isarety = "-"
    elif y1 < 300:
        isarety = "+"

    #vektörün x ve y işaretine göre kordinat düzlemi üzerinde bölgesi belirleniyor
    bolge = 1
    if isaretx == "+" and isarety == "+":
        bolge = 1
    elif isaretx == "-" and isarety == "+":
        bolge = 2
    elif isaretx == "-" and isarety == "-":
        bolge = 3
    elif isaretx == "+" and isarety == "-":
        bolge = 4
    elif isaretx == "90":
        bolge = 5
    elif isaretx == "270":
        bolge = 6
    elif isaretx == "0":
        bolge = 7

    # bolge belirlendiğine göre açı hesabını yapabiliriz
    if bolge == 1:
        b1 = o2 - y1
        a1 = x1 - o1
        aci = round(math.degrees(math.atan(b1/a1)),3)#açı değerini hesapladıktan sonra virgülden sonra virgül dahil 3 değer al
        aci = str(aci)#ekrana yazdıra bilmek için aci değişkenini str yapıyoruz
        img = cv2.putText(img,"aci = "+ aci,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
    elif bolge == 2:
        b1 = o2 - y1
        a1 = o1 - x1
        aci =round( 180 - math.degrees(math.atan(b1/a1)),3)
        aci = str(aci)
        img = cv2.putText(img, "aci = "+ aci, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
    elif bolge == 3:
        a1 = o1 - x1
        b1 = y1 - o2
        aci =round( 180 + math.degrees(math.atan(b1/a1)),3)
        aci = str(aci)
        img = cv2.putText(img, "aci = "+ aci, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
    elif bolge == 4:
        a1 = x1 - o1
        b1 = y1 - o2
        aci =round( 360 - math.degrees(math.atan(b1/a1)),3)
        aci = str(aci)
        img = cv2.putText(img, "aci = "+ aci, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
    elif bolge == 5:
        img = cv2.putText(img, "aci = 90", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
    elif bolge == 6:
        mask = cv2.putText(img, "aci = 270", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
    else:
        img = cv2.putText(img, "aci = 0", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),4)
        aci = 0


    cv2.imshow('original resim',img)#tüm degerler ile resmi ekrana basıyoruz
    if cv2.waitKey(25) & 0xFF == ord("q"):# q tuşuna basılır ise programı sonlandır
        break
kamera.release()
cv2.destroyAllWindows()