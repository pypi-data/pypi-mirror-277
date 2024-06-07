import win32com.client
from datetime import datetime
from pathlib import Path

def create_daily_task(task_name, executable_path, start_time):
    print(f"Scheduling task..... {task_name}..............")

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Create a trigger
    trigger = task_def.Triggers.Create(2)  # 2 means a daily trigger
    trigger.StartBoundary = start_time.strftime('%Y-%m-%dT%H:%M:%S')
    trigger.Repetition.Interval = "P1D"  # Repeat every day
    trigger.Repetition.Duration = "P1D"  # Repeat indefinitely

    # Create the action to run the executable
    action = task_def.Actions.Create(0)  # 0 means execute action
    action.Path = executable_path

    # Set task parameters
    task_def.RegistrationInfo.Description = f'{task_name} - Run daily at {start_time.strftime("%H:%M")}'
    task_def.Settings.Enabled = True
    task_def.Settings.StartWhenAvailable = True  # Ensures the task runs if missed
    task_def.Settings.Hidden = False
    task_def.Settings.DisallowStartIfOnBatteries = False
    task_def.Settings.StopIfGoingOnBatteries = False
    task_def.Settings.WakeToRun = True  # Wake the computer to run the task

    # Register the task
    root_folder.RegisterTaskDefinition(
        task_name,
        task_def,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # No user
        None,  # No password
        3,  # TASK_LOGON_INTERACTIVE_TOKEN
        None
    )
    print(f"Scheduled task '{task_name}' to run {executable_path} daily at {start_time.strftime('%H:%M')}.")

if __name__ == "__main__":
    executable_path = config_path = Path(__file__).resolve().parent.parent.parent / 'Scripts' / 'markatt.exe'
    print(f'Executable path: {executable_path}')
    start_time = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)

    create_daily_task('GL_Attendance_12PM', executable_path, start_time)

    start_time = datetime.now().replace(hour=15, minute=0, second=0, microsecond=0)
    create_daily_task('GL_Attendance_03PM', executable_path, start_time)
