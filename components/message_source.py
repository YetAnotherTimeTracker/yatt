from config.state_config import Language



message_source = {
    Language.ENG: {
        'task_created': 'task with id {} has been created',
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'filter.unknown': ':interrobang: Unknown command',

        'state.start_state.welcome': 'welcome to task tracking service!*\n'
                                     '\n'
                                     ':black_square_button: Number of *upcoming* tasks: {}\n'
                                     ':white_check_mark: Number of tasks You\'ve already *completed*: {}\n'
                                     ':scroll: Overall number of tasks *created*: {}\n'
                                     '\n\n'
                                     ':bulb: You can *proceed to tasks* with buttons below\n'
                                     ':bulb: Or write me anything You want to track and I will *create a new task* for You :)\n'
                                     '\n'
                                     'Bot version: 0.{} Alpha\n',

        'state.all_tasks.tasks.upcoming': 'here are your upcoming tasks:*\n\n',
        'state.all_tasks.tasks.completed': 'congratulations on completing these tasks:*\n\n',
        'state.all_tasks.tasks.all': 'here are all the tasks you have now:*\n\n',
        'state.all_tasks.no_tasks_yet': 'I could not find any tasks of provided category*\n\n',
        'state.all_tasks.notes': ':bulb: To *create a new task*, just write me something :)\n'
                                 ':bulb: Controls are on the bottom of the list\n',

        'state.select_lang': 'please, select language from the variants below*\n'
                             '\n'
                             ':bulb: Current language is English',

        'state.view_task.not_found': ':mag: Sorry, I could not find selected task',

        'btn.start_state.to_tasks.upcoming.label': ':black_square_button: Proceed to upcoming tasks',
        'btn.start_state.to_tasks.completed.label': ':white_check_mark: View completed tasks',
        'btn.start_state.to_tasks.all.label': ':scroll: View all tasks',
        'btn.start_state.select_lang.label': ':earth_africa: Select language',

        'btn.select_lang.eng.label': 'English',
        'btn.select_lang.eng.result': 'English language selected',
        'btn.select_lang.rus.label': 'Russian',
        'btn.select_lang.rus.result': 'Russian language selected',

        'btn.view_task.delete_task.label': ':x: Remove',
        'btn.view_task.delete_task.result': 'Task removed',
        'btn.view_task.disable_notify.label': ':no_bell: Mute',
        'btn.view_task.disable_notify.result': 'Notifications muted',
        'btn.view_task.mark_as_done.label': ' :white_check_mark: Done',
        'btn.view_task.mark_as_done.result': 'Task completed',
        'btn.view_task.upcoming.label': ':black_square_button: Upcoming',
        'btn.view_task.completed.label': ':white_check_mark: Completed',
        'btn.view_task.all.label': ':clipboard: All',

        'btn.new_task.project.personal.label': ':video_game: Personal',
        'btn.new_task.project.study.label': ':books: Study',
        'btn.new_task.project.work.label': ':briefcase: Work',
        'btn.new_task.project.other.label': ':open_file_folder: Other'
    },

    Language.RUS: {
        'task_created': 'задача с id {} была создана',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'filter.unknown': ':interrobang: Неизвестная команда',

        'state.start_state.welcome': 'добро пожаловать в сервис таск-трекинга!*\n'
                                     '\n'
                                     ':black_square_button: *Предстоящих* задач: {}\n'
                                     ':white_check_mark: *Выполнено* задач за все время: {}\n'
                                     ':scroll: *Всего* задач создано за все время: {}\n'
                                     '\n\n'
                                     ':bulb: *Перейдите к задачам* с помощью кнопок ниже\n'
                                     ':bulb: Чтобы *создать задачу*, просто напишите мне сообщение!\n'
                                     '\n'
                                     'Версия бота: 0.{} Alpha\n',

        'state.all_tasks.tasks.upcoming': 'список Ваших предстоящих задач:*\n',
        'state.all_tasks.tasks.completed': 'поздравляю с завршением этих задач:*\n',
        'state.all_tasks.tasks.all': 'список всех имеющихся у Вас задач на данный момент:*\n',
        'state.all_tasks.no_tasks_yet': 'задач выбранной категории не найдено*\n',
        'state.all_tasks.notes': '\n:bulb: Чтобы *создать задачу*, просто напишите мне что-нибудь :)\n'
                                 ':bulb: Кнопки управления расположены внизу списка\n',

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

        'btn.view_task.delete_task.label': ':x: Удалить',
        'btn.view_task.delete_task.result': 'Задача удалена',
        'btn.view_task.disable_notify.label': ':no_bell: Выкл. уведомл.',
        'btn.view_task.disable_notify.result': 'Уведомления отключены',
        'btn.view_task.mark_as_done.label': ':white_check_mark: Выполнено',
        'btn.view_task.mark_as_done.result': 'Задача выполнена',
        'btn.view_task.upcoming.label': ':black_square_button: Предстоящ.',
        'btn.view_task.completed.label': ':white_check_mark: Выполн.',
        'btn.view_task.all.label': ':clipboard: Все',

        'btn.new_task.project.personal.label': ':video_game: Личное',
        'btn.new_task.project.university.label': ':books: Учеба',
        'btn.new_task.project.work.label': ':briefcase: Работа',
        'btn.new_task.project.other.label': ':open_file_folder: Другое'
    }
}