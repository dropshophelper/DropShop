import telebot
#import vk

##session = vk.AuthSession('6489941', '', 'pass')
##vk_api = vk.API(session)

token = "614529863:AAG8TrT9t1HqsXSloPgKoa0jep6qwi3WQAg"

dataBaseUri = 'mongodb://bot:bot228@ds133550.mlab.com:33550/dropshop'

welcomeKeyBoard = telebot.types.ReplyKeyboardMarkup(True,True)
welcomeKeyBoard.row('поставщик')
welcomeKeyBoard.row('продавец')

# getNumberKeyBoard = telebot.types.ReplyKeyboardMarkup(True,False)
# getNumberKeyBoard.row('/number')

lookingKeyBoard = telebot.types.ReplyKeyboardMarkup(True,True)
lookingKeyBoard.row('ищу')

# sellingKeyBoard = telebot.types.ReplyKeyboardMarkup(True,False)
# sellingKeyBoard.row('/selling')


hideKeyBoard = telebot.types.ReplyKeyboardRemove()