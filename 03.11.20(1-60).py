#VBO-03.11.20
#print kullanmazsan consoldagörünür ama ekrana basılmaz.
print("hello era")
hello era #invalis syntax hatası verir.
print('hello era')#strin de ister tek tırnak ister çift farkyok
#type fonksiyou:içine yazılan nesnein ne tür olduğunu söyler
type("hello")#str =string
type('hello era')#tek -çift  tırnağın farkı yok burda da stringr özel!
#tırnak ne işe mi yarar?
type(9) #type= int çıktı
type('9')#typr=str
type("9")#type=str
#string metodları(yani fonksiyonları)
#len() fonksiyonu:
    a="geleceği yazanlar"
b=19
len(a)#boyutunu söyledi yani harfleri ve boşlukları saydı
len(b)#error:integer in boyutnu olmadığını söylüyor.
#STRING METODLARI UPPER() AND LOWE():
a="geleceği yazanlar"
len(a)
type(a)
a.upper()#a da yazan stringi hepsini büyük harfe çevirir.
a.lower()#a da yzaan stringi küçük harfe çevirir.
#islower and isupper fonksiyonları:
    a.isupper()#a da yazanların hepsi büyük mü diye sorgular
    a.islower()#true veya false diye cevap verir.
    b = a.upper()
    b.isupper()#upper yaptığım a'yı b'ye atadım.ve sorguladım b yi 
    #REPLACE FONKSİYONU:
#yararlı bir method.string içindeki harfleri başka harflere çevirmeye yarar.
a="geleceği yazanlar"
a.replace("a","i")#a'ları i ile değiştir.
a#replace ettiğini atamadığın için başka bir ada a deyinci orjinali çıktı.
a.replace("e", "o")
b= a.replace("e", "o")#şimdi attım
b
#STRIP()FONKSİYONU:
    a=" geleceği yazanlar "
    a.strip()#başında ve sonundaboşluk vardı attı.parantezi içi boşluğu atsın diye boş
a
a="lgeleceği yazanlarl"
a.strip("l")#fonksiyonu uygulamak istedğin yazının başındaki ve sonundakileri atar.
#l yi atsın diye stripin parantezinin içinde l yazıyor.
a.strip("lg")
a.strip("el")#sadece başta ve sonda çalışır.
#SUBSTRINLER FONKSİYONU:
    a="geleceği yazanlar"
    a[0]
a[3]#o dan başlayıp sayarak 3.terimi söyler
a[0:3]#0.terimden başla 3. terime kadar(3. dahil değil) olnları yaz
a[3:7]# bu aradabundanbağımsız boşlukları da terim olarak say.
#TYPE DÖNÜŞÜMLERİ
sayı1=input()#kullanıcı girdi girsin diye inpt yaptık
sayı2=input()#sayı1=2,sayı2=3 olsun 
type(sayı1)#bunlara str diyor.
type(sayı2)#bunu da str olarak sayıyor ben 2 ve 3 dememe rağmen
sayı1+sayı2#ve bu işlem de 23 olarak yazıyor .yani stringmiş gib bireştiriyor.toplamıyor.
int(sayı1)+int(sayı2)#böyle yapınca topluyor.integer gibi
int(12.5)#12 yazdı naptı ondalığı yani floatı integere yani tamsayayı çevirdi.
float(12)#12.0 yazdı
str(12)#'12' yazdı
type(str(12))#strçıkar üsteki satır gibi
#
print()





















