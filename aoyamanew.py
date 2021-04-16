#-*-coding:utf-8-*-
import amino 
client = amino.Client() 
email=input("Почта от аккаунта:") 
password=input("Пароль от аккаунта:") 
client.login(email=email, password=password)
print('\nБот вошел на ваш аккаунт')
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
    print(f"{name}: {id}")
comid = input("Выберите id: ")
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nБот ищет id')
chatInfo = sub_client.get_chat_threads(size=1000)
for title, chatId in zip(chatInfo.title, chatInfo.chatId):
	print(f"{title}: {chatId}")
chatid=input("Введите чат id:")
message=''
print("Выводит сообщение")
while True:
	try:
		sub_client.send_message(message=message, chatId=chatid, messageType=110)
	except:
		print('Не удалось отправить сообщение')
