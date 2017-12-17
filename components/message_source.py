from config.state_config import Language



message_source = {
    Language.ENG: {
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'task.upcoming': 'Upcoming',
        'task.completed': 'Completed',
        'task.muted': '(:no_bell: Muted)',

        'project.not_selected': ':question: Not selected',

        'filter.unknown': ':interrobang: Unknown command',

        'state.start_state.welcome': 'welcome to task tracking service!*\n'
                                     '\n'
                                     ':black_square_button: Number of *upcoming* tasks: {}\n'
                                     ':white_check_mark: Number of *completed* tasks: {}\n'
                                     ':scroll: *Created* tasks in total: {}\n'
                                     '\n'
                                     ':bulb: _You can proceed to tasks with buttons below_\n'
                                     ':bulb: _Or write me anything You want to track and I will create a new task for You_ :)\n'
                                     '\n'
                                     'Version: 0.{} Alpha\n',

        'state.view_task.inactive': ':pensive: Probably, this is not the task you are looking for.\n'
                                    '\n'
                                    ':bulb: _To update task list, use the buttons below that list. Task you are looking for could be removed_',
        'state.view_task.review': 'Task review',
        'state.view_task': ':pencil: *{}*\n'
                           '\n'
                           '      `{}`\n'  # task description
                           '\n'
                           'Remind date: *{}*\n'
                           'Create date: *{}*\n'
                           'Category: *{}*\n'
                           'Task status: *{}*\n'
                           'Task ID: {}\n'
                           '\n'
                           ':bulb: _Type /date and write datetime to set reminder (e.g. /date 21 dec 13-37)_',

        'state.new_task.created': 'New task has been created. Please, select category from the variants below',
        'state.new_task.not_created': ':pensive: Sorry, I could not create a task for some reason\n'
                                      'Can you try again, please?',

        'state.all_tasks.tasks.upcoming': 'here are your upcoming tasks:*\n',
        'state.all_tasks.tasks.completed': 'congratulations on completing these tasks:*\n',
        'state.all_tasks.tasks.all': 'here are all the tasks you have now:*\n',
        'state.all_tasks.no_tasks_yet': 'I could not find any tasks of that status*\n',
        'state.all_tasks.notes.no_tasks_yet': '\n:bulb: _To create a new task, just write me something_ :)\n',
        'state.all_tasks.notes': '\n:bulb: _To create a new task, just write me something_ :)\n'
                                 ':bulb: _Controls are on the bottom of the list_\n'
                                 ':bulb: _To refresh the list, click on one of the buttons below_',

        'state.select_lang': 'please, select language from the variants below*\n'
                             '\n'
                             ':bulb: _Current language is English_',

        'state.view_task.not_found': ':mag: Sorry, I could not find selected task',

        'btn.start_state.to_tasks.upcoming.label': ':black_square_button: Proceed to upcoming tasks',
        'btn.start_state.to_tasks.completed.label': ':white_check_mark: View completed tasks',
        'btn.start_state.to_tasks.all.label': ':scroll: View all tasks',
        'btn.start_state.select_lang.label': ':earth_africa: Select language',

        'btn.select_lang.eng.label': 'English',
        'btn.select_lang.eng.result': 'English language selected',
        'btn.select_lang.rus.label': 'Russian',
        'btn.select_lang.rus.result': 'Russian language selected',

        'btn.all_tasks.upcoming': ':black_square_button: Upcoming',
        'btn.all_tasks.completed': ':white_check_mark: Completed',
        'btn.all_tasks.refresh': ':arrows_counterclockwise: Refresh',
        'btn.all_tasks.home': ':house: Home',

        'btn.view_task.delete_task.label': ':x: Remove',
        'btn.view_task.delete_task.result': ':x: Task with ID "{}" has been removed',
        'btn.view_task.disable_notify.label': ':no_bell: Mute',
        'btn.view_task.disable_notify.result': ':no_bell: Notifications have been muted for task "*{}*"',
        'btn.view_task.enable_notify.label': ':bell: Unmute',
        'btn.view_task.enable_notify.result': ':bell: Notifications have been enabled for task "*{}*"',
        'btn.view_task.mark_as_done.label': ':white_check_mark: Done',
        'btn.view_task.mark_as_done.result': ':white_check_mark: Congratulations on completing the task! :clap:',
        'btn.view_task.mark_undone.label': ':black_square_button: Not done',
        'btn.view_task.mark_undone.result': ':black_square_button: Task has been marked as upcoming',
        'btn.view_task.upcoming.label': ':black_square_button: Upcoming',
        'btn.view_task.completed.label': ':white_check_mark: Completed',
        'btn.view_task.all.label': ':clipboard: All',

        'btn.new_task.project.prs.label': ':video_game: Personal',
        'btn.new_task.project.std.label': ':books: Study',
        'btn.new_task.project.wrk.label': ':briefcase: Work',
        'btn.new_task.project.oth.label': ':open_file_folder: Other'
    },

    Language.RUS: {
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'task.upcoming': 'Предстоящая',
        'task.completed': 'Выполненная',
        'task.muted': '(:no_bell: Уведомления выключены)',

        'project.not_selected': ':question: Не распределено',

        'filter.unknown': ':interrobang: Неизвестная команда',

        'state.start_state.welcome': 'добро пожаловать в сервис таск-трекинга!*\n'
                                     '\n'
                                     ':black_square_button: *Предстоящих* задач: {}\n'
                                     ':white_check_mark: *Выполнено* задач: {}\n'
                                     ':scroll: *Всего* задач создано за все время: {}\n'
                                     '\n'
                                     ':bulb: _Перейдите к задачам с помощью кнопок ниже_\n'
                                     ':bulb: _Чтобы создать задачу, просто напишите мне сообщение_ :)\n'
                                     '\n'
                                     'Версия: 0.{} Alpha\n',

        'state.view_task.inactive': ':pensive: Простите, не удалось найти выбранную задачу.\n'
                                    '\n'
                                    ':buld: _Чтобы обновить список задач, используйте кнопки в конце списка_',
        'state.view_task.review': 'Просмотр задачи',
        'state.view_task':  ':pencil: *{}*\n'   # New task has been created / Task review
                            '\n'
                            '      `{}`\n'  # task description
                            '\n'
                            'Время уведомления: *{}*\n'
                            'Задача создана: *{}*\n'
                            'Категория: *{}*\n'
                            'Статус задачи: *{}*\n'
                            'ID задачи: {}\n'
                            '\n'
                            ':bulb: _Введите /date и дату, чтобы включить уведомление (например, /date 21 дек 13-37)_',

        'state.new_task.created': 'Создана новая задача. Пожалуйста, выберите категорию из вариантов ниже',
        'state.new_task.not_created': ':pensive: Простите, не удалость создать задачу\n'
                                      'Попробуйте еще раз, пожайлуйста',

        'state.all_tasks.tasks.upcoming': 'список Ваших предстоящих задач:*\n',
        'state.all_tasks.tasks.completed': 'поздравляю с завршением этих задач:*\n',
        'state.all_tasks.tasks.all': 'список всех имеющихся у Вас задач на данный момент:*\n',
        'state.all_tasks.no_tasks_yet': 'Не найдено задач с выбранным статусом*\n',
        'state.all_tasks.notes.no_tasks_yet': '\n:bulb: _Чтобы создать задачу, просто напишите мне что-нибудь_ :)\n',
        'state.all_tasks.notes': '\n:bulb: _Чтобы создать задачу, просто напишите мне что-нибудь_ :)\n'
                                 ':bulb: _Кнопки управления расположены внизу списка_\n'
                                 ':bulb: _Чтобы обновить список, используйте кнопки ниже_',

        'state.select_lang': 'выберите, пожалуйста, язык из представленных вариантов*\n'
                             '\n'
                             ':bulb: Текущий язык: Русский',

        'state.view_task.not_found': ':mag: Не удалось найти выбранную задачу :(',

        'btn.start_state.to_tasks.upcoming.label': ':black_square_button: Открыть предстоящие задачи',
        'btn.start_state.to_tasks.completed.label': ':white_check_mark: Посмотреть выполненные задачи',
        'btn.start_state.to_tasks.all.label': ':scroll: Посмотреть весь список задач',
        'btn.start_state.select_lang.label': ':earth_africa: Сменить язык',

        'btn.select_lang.eng.label': 'Английский',
        'btn.select_lang.eng.result': 'Выбран английский язык',
        'btn.select_lang.rus.label': 'Русский',
        'btn.select_lang.rus.result': 'Выбран русский язык',

        'btn.all_tasks.upcoming': ':black_square_button: Предстоящие',
        'btn.all_tasks.completed': ':white_check_mark: Выполненные',
        'btn.all_tasks.refresh': ':arrows_counterclockwise: Обновить',
        'btn.all_tasks.home': ':house: Домой',

        'btn.view_task.delete_task.label': ':x: Удалить',
        'btn.view_task.delete_task.result': ':x: Задача с ID "{}" удалена',
        'btn.view_task.disable_notify.label': ':no_bell: Выкл. уведомл.',
        'btn.view_task.disable_notify.result': ':no_bell: Уведомления отключены для задачи "*{}*"',
        'btn.view_task.enable_notify.label': ':bell: Включить',
        'btn.view_task.enable_notify.result': ':bell: Уведомления для задачи "*{}*" включены',
        'btn.view_task.mark_as_done.label': ':white_check_mark: Выполнено',
        'btn.view_task.mark_as_done.result': ':white_check_mark: Поздравляю с выполнением задачи! :clap:',
        'btn.view_task.mark_undone.label': ':black_square_button: Отменить',
        'btn.view_task.mark_undone.result': ':black_square_button: Задача отмечена, как предстоящая',
        'btn.view_task.upcoming.label': ':black_square_button: Предстоящ.',
        'btn.view_task.completed.label': ':white_check_mark: Выполн.',
        'btn.view_task.all.label': ':clipboard: Все',

        'btn.new_task.project.prs.label': ':video_game: Личное',
        'btn.new_task.project.std.label': ':books: Учеба',
        'btn.new_task.project.wrk.label': ':briefcase: Работа',
        'btn.new_task.project.oth.label': ':open_file_folder: Другое'
    }
}