from config.state_config import Language



message_source = {
    Language.ENG: {
        'write_me': 'Just write me something to create a new one :)',
        'no_tasks_yet': 'You don\'t have any tasks yet',
        'selected_lang': 'Selected English language',
        'your_tasks': "{}, here are your tasks",
        'task_created': 'task with id {} has been created',
        'cant_find_task': 'Sorry, can`t find task with id {}',
        'set_date': 'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',

        'btn.view_task.delete_task.label': 'Remove task',
        'btn.view_task.delete_task.result': 'Task removed',
        'btn.view_task.disable_notify.label': 'Disable notification',
        'btn.view_task.disable_notify.result': 'Notifications disabled',
        'btn.view_task.mark_as_done.label': 'Mark as done',
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
        'cant_find_task': 'Извините, не могу найти задачу с id {}',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}',

        'btn.view_task.delete_task.label': 'Удалить задачу',
        'btn.view_task.delete_task.result': 'Задача удалена',
        'btn.view_task.disable_notify.label': 'Выключить уведомления',
        'btn.view_task.disable_notify.result': 'Уведомления отключены',
        'btn.view_task.mark_as_done.label': 'Выполнено',
        'btn.view_task.mark_as_done.result': 'Задача выполнена',
        'btn.view_task.not_completed.label': 'Предстоящие задачи',
        'btn.view_task.all_tasks.label': 'Все задачи'
    }
}