#04.11.20 LİSTE OLUŞTURMA,VERİ YAPILARI

liste1=[1,2,3,4]#eşittir koymayı unutma
type(liste1)
liste2=["a",5,6,7]
buyuklist=["a",5,6,7,liste1]#başka listyei de böyle ekleyebililyoruz
type(buyuklist)
len(buyuklist)#5 çıkıyor
buyuklist2=["a",1,2,[4,5,]]
buyuklist2[3][0]#buyuklist listesinin 3. teriminin 0. terimini yaz adedik.bunu liste içimde liste olduğu için yaptık.
len(buyuklist2)
#buyuklist3=["a",1,2, ,[4,5,]]
#len(buyuklist3)#boşluk olmıcak invalis syntax  hatası alırsın
#liteleri  nasıl birleştiririz:
    listetum=["a",90,liste1, liste2,buyuklist2]
    len(listetum)#5 çıkıyor
    type(listetum)
#listenin elemanlarına erişme:
   listetum[0] 
listetum[0:2]#o. ve 1. elemanları yaz diyor
listetum[0:]#0. elelmandan başla son elemam kadar yaz diyor.
#bu listetum da elemanlar hem liste hem tek tek karışık.
listetum[:2]#0. elemmandan başla 2. eleman kadar (dahil değil)yaz diyor.
del listetum
listetum#yukarad del yaptığın için artık listetum diye bir liste yok diyor
#eleman değiştirme:değiştirilen eleman ilinir onun yerine gelir
    liste=["ali","veli",49,50]
liste[2]
liste[2]="mahmut"#2. elemanını mahut olarak değştirme
liste
liste[0:2]="ayşe","elif"#0. ve 1. elamanı ayşe ve elif diye değiltirme
liste
#eklemek istediğin elemanıistediğin yere ekleme ve silmeden:insert ve pop methodları ile
liste=["elma","armut","ayva"]
liste
liste.insert(2, "karpuz")#2. eleman olarak karpuz eklendi
liste
liste.insert(4, 999)#listenin son elemanı olsun siye.eleman sayısından bir afzla olarak yazdım(4)
liste
#peki son eleman olarak eklemek için hep böyle elemanlarını  saymıcakasın:len kullanıcakasın
    liste.insert(len(liste), "papaya")
liste

#eleman ekleme:sınuna ekler
liste=liste+["fatma",21]
liste
#eleman çıkarma
del liste[2]#999 silindi.aynı şekild 2. opsiyon var:
    liste
    liste.pop(0)#armut çıktı
liste
dir(liste)#liste ile ne fonksiyonlar yapabileceğini gösterir.
#liste veya hangi adla yapıyosan . koy ctrl+boşluk yap.yukardaki gibi yapabileceğin kısayollar cıkacak.
#append ve remove methodlarrı
liste.append("berk")#parantez ziçine yazdığını ekler
liste
liste.remove("ayşe")#parantez içine yazdığını siler
liste


#diğer liste methodları:
    #count
    listem=["ocak","şubat","mart","nisan","ocak","mart",2,3,4,2,2]
    listem.count("ocak")#count fonsk:parantez içine yazadığınşey nekadar tane varsa listed onu gösterir.
listem.count(2)
listem

#copy
yedeklistem=listem.copy()
yedeklistem

#extend:listeye ekemeler yapmak
listem.extend(["elma","armut","kelmahmut"])
listem

#index:girilen ifadenin  kaçıncı terim olduğunun söyler
listem.index(2)
7#reverse methodu: listeyi tersten  yazar
listem.reverse()
listem

#sort methodu:listedekileri küçükten büyüğe yazar.,ntegerle bir liste şartı var tabi
    listen=[1,100,21,2,3,]
listen.sort()
listen

#clear methodu:listeyi siler (elemanalrı)
listem.clear()
listem


#VERİ YAPILARI:TUPLE:listey benzer ama liste gibi değişme işlemi yapılmaz.eleman eklenmez ,çıkmaz,değiştirilemez.**kapsayıcı ,sıralı,değiştirilemez
#listeler:kapsayıcı,sıralı,değiştirelbilir
#tuple oluşturma: 2 yazma şekli var
t=("ali","veli",1,2,3,[4,5])
t="ali","veli",1,2,3,[4,5]
type(t)#tuple olduğunu söyler
t="ali",
type(t)#str çıkıyor.tuple çıkması için yanına virgül koydk.

# veri yapıları:DICTIONARY:kapsayıcı,sırasız ,değiştirilebilir
#sözlük oluşturma:
    
    
     sözlük={"elma" : 10,
        "armut":20 , 
         "karpuz":30}

sözlük       #KEY      VALUE
 sözlük={ "elma":["kırmızı",10],
          "armut" :["sarı",20],
         "karpuz":["yeşil",30]}    
    sözlük


#sözlük elemanalrı çekme

sözlük={"a":"alfabenin ilk harfi",#virgü öenmli.hatverir
        "b":"alfabenin ikinci harfi",
        "c":"lfabenin üçüncü harfi"}    
    sözlük["a"]#afabenin ilk harfi olarak gösterdi
    #sözlükte ekleme,değiştirme:
   sözlük={"a":"alfabenin ilk harfi",#virgü öenmli.hatverir
        "b":"alfabenin ikinci harfi",
        "c":"lfabenin üçüncü harfi"}  
sözlük["d"] ="alfabenin dördüncü harfidir"
sözlük     #d eklenmiş oldu
sözlük["a"]="alfabenin ilk harfi değildir"
sözlük    #a için value değişmiş oldu.
    

#SETLER (KÜMELER):
    #sırasızdır/indexsiz),eşsizdir yani her teridmen bir tane olur,değiştirilebilir
    liste=[1,3,4,"ali"]#liste oluşturalım
s=set(liste)
s    #bak senin listeni küme elemanı gibi yazdı.yani küme yaptı
tuple=("a","b")#hadi tuple oluşturalım
s=set(tuple)    
s    #tupleyi kümey çevirdi

meltem="durdane meltem tuğran "
type(meltem)#srting olduğunu görüyoruz.
    s=set(meltem)
s    #naptı: girdiğim stringi küme olarak yazdı.boşluk da bir terimdir. küme olduğu için tekrar edneleri 1 kere yazdı sadec.

#setler indexsiz demiştik:yani sete bie 0. elemanını ver diyemeyiz
liste=[1,2,2,34,5]
liste[0]    #bana 1 veriyor çünkü listeler indexlidir
s=set(liste)
s
s[0]#type erroe verir.çünkü setler indexsizdir.
s.add("murt")#set içerisine eleman eklemek
s
s.remove("murt")#setten silmek için 
s
#discard fonksiyonu:
    #şimdi senin silmek istediğin terim yok diyelim sette sen de remove kullanarak sil deidn .ama olmadığı için error verdi noldu böylece tüüüm kodunu çalıştırdığında akışda hata  oldu.bu hata olmasın ama yine de sen silmek istediğin şeyi yaz.eğer sette yoksa error vermeden yoluna devam etsin.
   s.discard("murt") 
s    

#setlerde fark işelmleri:
  set1=set([1,2,3,4,6])  
  set2=set([1,2,4,5])
  set1.difference(set2)#set1 deolup set2 de olmayan ları gösterir.
   set1-set2# bu da aynı işelvi yapar.set1 ve set2 yi yer değiştirebilirsin.
   
   #ikisinde deolmayanları göstersin
   set1.symmetric_difference(set2)#bu a\b nin ve b\a nın birleşimidir.
   set1.intersection(set2)#kesişimlerini verir.
   set1.intersection_update(set2)#kesişimleri  set1 e atar.
set1   
set2.intersection_update(set1)
set2   
 set1 & set2# bu da kesişim alır. 
kesişim=set1&set2
kesişim
set1=set([1,2,3,4,5,7,8,9,])
set2=set([1,2,3,4,5,6,7])
set1.isdisjoint(set2)#set1 ve set2 nin kesişimi boş mu diye soruladı.boş olmadıiçin fasle döndü.
set1.issubset(set2)#set1 set2 nin alt kümesi mi diye sorgular.

set1.issuperset(set2)#set1 ,set2yi kapsıyor mu 
set1.union(set2)















