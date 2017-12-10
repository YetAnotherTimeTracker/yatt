from config.state_config import Language



message_source = {
    Language.ENG: {
        'write_me': 'Just write me something to create a new one :)',
        'no_tasks_yet': 'You don\'t have any tasks yet',
        'selected_lang': 'Selected English language',
        'your_tasks': "{}, here are your tasks",
        'task_created': 'task with id {} has been created',
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'filter.unknown': 'Unknown command',

        'state.select_lang': 'please, select language',

        'state.view_task.not_found': 'Sorry, I could not find selected task',

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
        'btn.view_task.not_completed.label': 'View not completed',
        'btn.view_task.all_tasks.label': 'View all'
    },

    Language.RUS: {
        'write_me': 'Просто напишите мне что-нибудь, чтобы создать :)',
        'no_tasks_yet': 'у вас еще нет задач',
        'selected_lang': 'Выбран русский язык',
        'your_tasks': "{}, Ваши задачи:\n",
        'task_created': 'задача с id {} была создана',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'filter.unknown': 'Неизвестная команда',

        'state.select_lang': 'выберите, пожалуйста, язык',

        'state.view_task.not_found': 'Не удалось найти выбранную задачу :(',

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
        'btn.view_task.not_completed.label': 'Предстоящие дела',
        'btn.view_task.all_tasks.label': 'Все дела'
    }
}