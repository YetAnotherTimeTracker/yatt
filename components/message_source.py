from config.state_config import Language



message_source = {
    Language.ENG: {
        'task_created': 'task with id {} has been created',
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'filter.unknown': ':interrobang: Unknown command',

        'state.start_state.welcome': 'welcome to task tracking service!',

        'state.all_tasks.your_tasks': 'here are Your tasks:',
        'state.all_tasks.no_tasks_yet': 'You don\'t have any tasks yet\n'
                                        'Just write me something to create a new one :)',

        'state.select_lang': 'please, select language',

        'state.view_task.not_found': ':mag: Sorry, I could not find selected task',

        'btn.start_state.to_tasks.upcoming.label': ':black_square_button: Proceed to upcoming tasks',
        'btn.start_state.to_tasks.completed.label': ':white_check_mark: View completed tasks',
        'btn.start_state.to_tasks.all.label': ':clipboard: Proceed to all tasks',
        'btn.start_state.select_lang.label': ':wrench: Select language',

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
        'btn.view_task.all.label': ':clipboard: All'
    },

    Language.RUS: {
        'task_created': 'задача с id {} была создана',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'filter.unknown': ':interrobang: Неизвестная команда',

        'state.start_state.welcome': 'добро пожаловать в сервис таск-трекинга!',

        'state.all_tasks.your_tasks': 'ваши задачи:',
        'state.all_tasks.no_tasks_yet': 'У Вас нет невыполненных задач\n'
                                        'Просто напишите мне что-нибудь, чтобы создать задачу',

        'state.select_lang': 'выберите, пожалуйста, язык',

        'state.view_task.not_found': ':mag: Не удалось найти выбранную задачу :(',

        'btn.start_state.to_tasks.upcoming.label': ':black_square_button: Перейти к предстоящим делам',
        'btn.start_state.to_tasks.completed.label': ':white_check_mark: Посмотреть уже выполненные дела',
        'btn.start_state.to_tasks.all.label': ':clipboard: Перейти ко всему списку задач',
        'btn.start_state.select_lang.label': ':wrench: Сменить язык',

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
        'btn.view_task.all.label': ':clipboard: Все'
    }
}