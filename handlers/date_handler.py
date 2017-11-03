def _date(bot, update):
    args = update.message.text
    print(args)
    date_line = re.findall(
        '\d{2}\s\d{2}\s\d{4}\s\d{2}\S{1}\d{2}|\d{2}\s\d{2}\s\d{2}\S{1}\d{2}|\d{2}\s\w{3}\s\d{2}\S{1}\d{2}',
        str(args))
    #print(date_line)
    date_line = str(date_line[0])
    date_line =  str(datetime.date.today().year)+ " " +date_line
    date_line = date_line.replace(" ", '.')
    date_line = date_line.replace("-", '.')

    if 'янв' in date_line:
        date_line = date_line.replace("янв", '01')
    if 'фев' in date_line:
        date_line = date_line.replace("фев", '02')
    if 'мар' in date_line:
        date_line = date_line.replace("мар", '03')
    if 'апр' in date_line:
        date_line = date_line.replace("апр", '04')
    if 'мая' in date_line:
        date_line = date_line.replace("мая", '05')
    if 'июн' in date_line:
        date_line = date_line.replace("июн", '06')
    if 'июл' in date_line:
        date_line = date_line.replace("июл", '07')
    if 'авг' in date_line:
        date_line = date_line.replace("авг", '08')
    if 'сен' in date_line:
        date_line = date_line.replace("сен", '09')
    if 'окт' in date_line:
        date_line = date_line.replace("окт", '10')
    if 'ноя' in date_line:
        date_line = date_line.replace("ноя", '11')
    if 'дек' in date_line:
        date_line = date_line.replace("дек", '12')

    #print(date_line)
    d = datetime.datetime.strptime(date_line, "%Y.%d.%m.%H.%M")
    #d.year=datetime.date.today().year
    bot.send_message(chat_id=update.message.chat_id, text=str(d))
