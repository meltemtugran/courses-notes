
#FONKSİYONAR
#FONKSİYONDA İŞLEMLER:
#MATEMATİKSEL İŞLEMLER:
 2+3
2*3
2-3       
2/3
2**3#üss alma(**):ikinin üçümcü kuvveti demek.

#şimdi bunları fonksiyon kullnarak yaptıralım:
  #  def:ben şimdifonksiyon yazcam demek 
  #kare_al : fonskiyonun ismi sen seçiyorsun
  #( ) parantez içi:bu fonksiyon hangi argümanlar abağlı olduğunu söyler
  def kare_al(x):#iki noktaüst üste önemli
      x**2 
      #print demezsen işlem içerde gerçekleşir.ancak consola yazmaz.sonucu
      def topla(x):
          print(x+10)#iki noktadan sonra aşağıy ainip ne yapmasınıistediğini yazıyorsun.eğer konsola yazdırmasını sitiyorsan print içinde yaz .
          
          topla(4)     
topla(100)      

def topla(x):
    print("girilen sayının toplamı:" + str(x+10))#str almamızın sebebi string ve integeri birleştirmiyor. biz de integeri string yaptık.
print(topla(5))

def topla(x):
print("girilen sayı :" +str(x),"girilen sayının toplamı:" +str((x+10)))

#şimdi tekrar  yapalım
def kare_al(x):
    print(x**3)
kare_al(2)

#peki ben 2 farklı tür değilekn kullanmak istersem x ve y gibi o zaman napıcam.
def kare_al(x,y):
    print(x**y)
kare_al(2, 3)#bu satırın print satırından gerid olamsı önemli
kare_al(y=2,x=5)#↓yukardakinin böyle de yazabilirisn eğer aynı

#FONKSİYONARIN ÇIKTISINI GİRDİ OLARAK KULLNMAK :return fonksiyonu kullanılır.
#ilk başta bimiyormuş gibi 
def işlem_yap (x,y,z):
    print((x+y)/z)
işlem_yap(2,3,4)  #normal olarak işlmi yaptı
 
çıktı=işlem_yap(2,3,4)
çıktı
 print(çıktı)#bunu çalıştırınca  error akıyorum.
 
 #görüldüğü gibi çıktıyı printe giridi olarakk kabul ettiremedk.return fonk. kullanmak zorundayız.
 
 
  def işlem_yap (x,y,z):
      return((x+y)/z)
  işlem_yap(4,5,6)
  çıktı=işlem_yap(4,5,6)
çıktı  
print(çıktı)    #♠hata almıyorum

#KARAR YAPILARI:if else
x=100
y=200
if x<y:
    print(" x küçüktür y den")
else:
        print("x küçük değildir y den")#else de üstteki if ile aynı sütünda en başta olmalı

gider=100
gelir=200
if gider== gelir:
    print("gider gelir birbirne eşit")
else:
    print("gider gelireşit değil")#printler de aynı sütünda hizalı olacak yoksa hata verir
    
#KARAR YAPILARI:elif:birden fazla koşuliçin kullanılır
x=10
y=20
z=30

 if x>y:
    print("büyük")
 elif x>z:
     print("büyük")
 else :
     print("x en küçük")


 sınır=1000000
sirket_adı=input("çalıştığınız şirketi giriniz:")#kullanıcıdan girid almak için input kullanılır.
gelir= int(input("gelirinizi girin:"))#kullanıcıdan alınan input her zaman string olarak kaydolur. bunu değiştirmek için başına int yazrzak değiştirebilirz.
if gelir>sınır:
    print("zenginsiniz")
elif gelir==sınır:
    print("normalsiniz")
else:
    print("fakirsiniz")  
    
    #FOR DÖNGÜSÜ
listem = ["ali","veli","49","50"]
for i in listem:
    print(i) #listemde i yi tek tek dolaştır dedim.dolaşırken yapacağı işlemi de printe yazdım i dedim yani sadece yaz.
     maas=[100,200,300,400]
     for i in maas:
         print(i*5)
         
 maas=[100,200,300,400,"meltem"]  
for i in maas
    print(i*10)#hata alırız sebebi:integr ve string çarpılmaz,toplanmaz...
    
 #FOR VE FONKSİYON KULLNARAK:
maas=[1000,2000,3000,40000] 
def yeni_maas(x):
    print(x*20/100+x)
    
for i in maas:
    yeni_maas(i)
        

    #İF FOR VE FONKBİRLİKTE KULLNAMA ÖRNEĞİ: bir kısım yüzde 20 zam alın ,bir ksıım yüzde elli zam alın ,bir kısım ise zam almasın :
maaslar=[1000,2000,3000,4000,5000,6000]

def yeni_maas1(x):
    print(x*20/100+ x)
def yeni_maas2(x):
    print(x*50/100+ x)
                   
for i in maaslar:
    if i<=2000:
       yeni_maas1(i)
    elif i>=3000 and i<5000 :  #PYTHINDA ve bağlacı ampersandla değil and diye yapılır.
         yeni_maas2(i)
    else :
         print("yeterince zenginsin zaten ne zammı")
         
         #BREAK AND CONTINUE: döngüler içerisinde(for sayesinde) belli bir şartı sağlayan eleman bulunduğunda (if sayesinde) döngünğn durmasını ya da elemanın çıkarılmasını istediğimizde bunu yapıyoruz:
             
#örnek:maaşlardan 3000 e gelince dursun
maaslar=[800,650,50,100,200,700,10000,25]#görüldüğü gibi maaşlar sıralı değil.küçükten büyüğe .sıralamak için sort fonk kullanıyoruz.bunu ezberlemiyoruz:
dir(maaslar) #bunu çalıştırınca consolda fonklar diziliyor.onları araştırarakbulabilirsin sırlama yapan fonkiyonu.
maaslar.sort()   
maaslar   #tekrar çağırdığımıda sıralı  olarak geldi fonksiyona
maaslar=[800,650,50,100,200,700,3000,10000,25]
maaslar.sort()
maaslar
for i in maaslar:
    if i==3000:
       print("kesildi")  
       break
    print(i)     #noldu 3000 görünce durdu 3000 ve 10 000 i yazmadı.                                
    

#CONTINUE: 3000 İ GÖRÜNCE durmasın onu atlayıp devam etsin

maaslar=[800,650,50,100,200,700,3000,10000,25]
maaslar.sort()
maaslar
for i in maaslar:
    if i==3000:
        print("atladım onu")
        continue
    print(i)
    
    #WHILE:(dığı sürece)bu/herhangi belirlenen) şart geçerli olduğu sürece demek:
        
sayi=1
while sayi < 10:
    sayi += 1
    print(sayi)#while da dikkat edilecek nokta whilde son sınır olarak belirlediğin sayı da olur. 10 a kadar dediysek sayı 10 u görürü ve yazdırılır.
    
    




