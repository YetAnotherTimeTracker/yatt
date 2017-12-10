from config.state_config import Language



message_source = {
    Language.ENG: {
        'task_created': 'task with id {} has been created',
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'filter.unknown': 'Unknown command',

        'state.start_state.welcome': 'welcome to task tracking service!',

        'state.all_tasks.your_tasks': 'here are Your tasks:',
        'state.all_tasks.no_tasks_yet': 'You don\'t have any tasks yet\n'
                                        'Just write me something to create a new one :)',

        'state.select_lang': 'please, select language',

        'state.view_task.not_found': 'Sorry, I could not find selected task',

        'btn.start_state.to_tasks.upcoming': 'Proceed to upcoming tasks',
        'btn.start_state.to_tasks.all': 'Proceed to all tasks',
        'btn.start_state.select_lang': 'Select language',

        'btn.select_lang.eng.label': 'English',
        'btn.select_lang.eng.result': 'English language selected',
        'btn.select_lang.rus.label': 'Russian',
        'btn.select_lang.rus.result': 'Russian language selected',

        'btn.view_task.delete_task.label': 'Remove',
        'btn.view_task.delete_task.result': 'Task removed',
        'btn.view_task.disable_notify.label': 'Mute',
        'btn.view_task.disable_notify.result': 'Notifications muted',
        'btn.view_task.mark_as_done.label': 'Done',
        'btn.view_task.mark_as_done.result': 'Task completed',
        'btn.view_task.upcoming.label': 'Upcoming',
        'btn.view_task.completed.label': 'Completed',
        'btn.view_task.all.label': 'All'
    },

    Language.RUS: {
        'task_created': 'задача с id {} была создана',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'filter.unknown': 'Неизвестная команда',

        'state.start_state.welcome': 'добро пожаловать в сервис таск-трекинга',

        'state.all_tasks.your_tasks': 'ваши задачи:',
        'state.all_tasks.no_tasks_yet': 'У Вас нет невыполненных задач\n'
                                        'Просто напишите мне что-нибудь, чтобы создать задачу',

        'state.select_lang': 'выберите, пожалуйста, язык',

        'state.view_task.not_found': 'Не удалось найти выбранную задачу :(',

        'btn.start_state.to_tasks.upcoming': 'Перейти к предстоящим делам',
        'btn.start_state.to_tasks.all': 'Перейти ко всему списку задач',
        'btn.start_state.select_lang': 'Сменить язык',

        'btn.select_lang.eng.label': 'Английский',
        'btn.select_lang.eng.result': 'Выбран английский язык',
        'btn.select_lang.rus.label': 'Русский',
        'btn.select_lang.rus.result': 'Выбран русский язык',

        'btn.view_task.delete_task.label': 'Удалить',
        'btn.view_task.delete_task.result': 'Задача удалена',
        'btn.view_task.disable_notify.label': 'Выкл. уведомления',
        'btn.view_task.disable_notify.result': 'Уведомления отключены',
        'btn.view_task.mark_as_done.label': 'Выполнено',
        'btn.view_task.mark_as_done.result': 'Задача выполнена',
        'btn.view_task.upcoming.label': 'Предстоящие',
        'btn.view_task.completed.label': 'Выполненные',
        'btn.view_task.all.label': 'Все'
    }
}