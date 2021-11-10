# Server
Server консоль
![img.png](img/img.png)
client консоль 
![](img/img_1.png)
### Контрольные вопросы на «TCP-клиент и эхо-сервер»
1. Чем отличаются клиентские и серверные сокеты?
>*Ответ: Их главное отличие в том, что к серверным сокетам могут подключаться несколько клиентов, а клиентские сокеты могут подключаться к своим конкретным серверным сокетам.*
2. Как можно передать через сокеты текстовую информацию?
>*Ответ: Превратить в байт код и передать при помощи функции send() или sendto()*
3. Какие операции с сокетами блокируют выполнение программы?
>*Ответ: Это (на клиенте) получение информации от сервера, (на сервере) получение информации от клиента*
4. Что такое неблокирующие сокеты?
>*Ответ: Это сокеты, которые не блокируют програму ожидая получения или отправки клиентских данных,
а проверяют на наличие этих данных в буфере и в случае если есть - сразу возвращают,а если нет, не преывает работу программы а возврашает 0 байт прочитанного кода или исключение*
5. В чем преимущества и недостатки использования TCP по сравнению с UDP?
>*Ответ:TCP позволяет обеспечить полную и корректную передачу данных но уступает UDP в скорости передачи*
6. Какие вызовы, связанные с сокетами используются только на стороне сервера?
>*Ответ: bind()-Привязывает сокет к адресу address (инициализирует IP-адрес и порт),\
> accept()-Принимает соединение и блокирует приложение в ожидании сообщения от клиента*
7. На каком уровне модели OSI работают сокеты?
>*Ответ: Транспортный 4-й уровень*