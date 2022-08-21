import time
from plyer import notification
if __name__ == '__main__':
    while(True):
        notification.notify(
            title= '***Drink water now',
            message = 'Drinking water can prevent dehydration, a condition that can cause unclear thinking, cause your body to overheat, and lead to constipation and kidney stones.',
            app_icon = r'C:\Users\hksai\OneDrive\Desktop\my codes\programmes\icon.ico',
            timeout = 10
        )
        time.sleep(60*60)
