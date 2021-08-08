### This example Python-Asyncio;

Asynchronous frameworks need a scheduler usually called an event loop. <br>
This event loop keeps track of all the running tasks and when a function suspended it returns control to the event loop which then will find another function to start or resume and this is called cooperative multitasking. <br>
Async IO provides a framework an asynchronous framework that's centered on this event loop and it efficiently handles input/output events an application interacts with the event loop explicitly it registers code to be run and then it lets the event loop the scheduler make the necessary calls into application code when the resources are available. So, if a network server open sockets and then registers them to be told when input events occur on them the event loop will alert the server code when there's a new incoming connection or when there's data to be read. If there's no more data to be read from a socket than the server then yields control back to the event loop.

The mechanism from yielding control back to the event loop depends on co-routines co-routines are a language construct designed for concurrent operation. <br>
The co-routine can pause execution using the awake keyword with another co-routine and while it's paused the co-routine state is maintained allowing it to resume where it left off one co-routine can start another and then wait for the results and this makes it easier to decompose a task into reusable parts.

# TURKCE

Asenkron çerçeveler, genellikle olay döngüsü adı verilen bir zamanlayıcıya ihtiyaç duyar. Bu olay döngüsü, çalışan tüm görevlerin kaydını tutar ve bir işlev askıya alındığında kontrolü, başlatılacak veya devam ettirilecek başka bir işlev bulan olay döngüsüne geri döndürür ve buna ortak çoklu görev denir. <br>
Async IO, bir çerçeveye, bu olay döngüsüne odaklanan eşzamansız bir çerçeve sağlar ve bir uygulamanın olay döngüsüyle etkileşime girdiği giriş/çıkış olaylarını verimli bir şekilde işler, çalıştırılacak kodu kaydeder ve olay döngüsünün zamanlayıcının gerekli çağrıları yapmasına izin verir. <br>
kaynaklar mevcut olduğunda uygulama kodu. Bu nedenle, bir ağ sunucusu soketleri açarsa ve daha sonra üzerlerinde giriş olayları meydana geldiğinde söylenmesi için onları kaydederse, olay döngüsü yeni bir gelen bağlantı olduğunda veya okunacak veri olduğunda sunucu kodunu uyarır. Bir soketten sunucudan daha fazla okunacak veri yoksa, kontrol olay döngüsüne geri döner.

Kontrolden olay döngüsüne geri dönen mekanizma, ortak rutinlere bağlıdır. Eş rutinler, eşzamanlı işlem için tasarlanmış bir dil yapısıdır. <br>
Eş-yordam, başka bir eş-yordam ile uyanık anahtar sözcüğünü kullanarak yürütmeyi duraklatabilir ve duraklatıldığında, eş-rutin durumu, kaldığı yerden devam etmesine izin vererek, bir eş-rutin bir başkasını başlatabilir ve ardından sonuçları bekleyebilir ve bu bir görevi yeniden kullanılabilir parçalara ayırmayı kolaylaştırır.
