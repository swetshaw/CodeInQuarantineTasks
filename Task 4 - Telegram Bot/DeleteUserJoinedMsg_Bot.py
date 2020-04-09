import logging
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


updater = Updater(token='1242043599:AAH2nvWyQGofDc6saknLcwM8Gih47hKETq4', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def handle_new_chat_members(update, context):
        msg = update.effective_message
        try:
            context.bot.delete_message(
                chat_id=msg.chat.id,
                message_id=msg.message_id,
            )
        except Exception as ex:
            if 'Message to delete not found' in str(ex):
                logging.error('Failed to delete msg: %s', ex)
                return
            elif "Message can't be deleted" in str(ex):
                logging.error('Failed to delete msg: %s', ex)
                return
            else:
                raise

newMember_handler = MessageHandler(Filters.status_update.new_chat_members, handle_new_chat_members)
dispatcher.add_handler(newMember_handler)

updater.start_polling()
updater.idle()
