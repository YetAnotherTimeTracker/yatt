def _date(bot, update):
    args = update.message.text
    date_line = re.findall(
        '\d{4}-\d{2}-\d{2}\s\d{2}\S{1}\d{2}|\d{2}.\d{2}.\d{4}\s\d{2}\S{1}\d{2}|\d{2}.\d{2}.\d{2}\s\d{2}\S{1}\d{2}',
        str(args))
    date_line = str(date_line[0])
    date_line = date_line.replace("-", '.')
    d = datetime.datetime.strptime(date_line, "%d.%m.%Y %H.%M")
    bot.send_message(chat_id=update.message.chat_id, text=str(d))
