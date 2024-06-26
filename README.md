# برنامه مدیریت محصولات

این یک برنامه وب برای مدیریت محصولات است که به کاربران اجازه می‌دهد تا اطلاعات محصولات را اضافه، جستجو، مرتب‌سازی، ویرایش و حذف کنند. همچنین قابلیت‌هایی برای آپلود و بازیابی محصولات از فایل اکسل و صادرات محصولات به فایل اکسل فراهم می‌کند.

## ویژگی‌ها

- **اضافه کردن محصول**: اضافه کردن محصولات جدید با ویژگی‌های مختلف.
- **آپلود فایل**: آپلود فایل اکسل حاوی داده‌های محصول.
- **صادرات محصولات به اکسل**: صادرات لیست محصولات به فایل اکسل.
- **بازیابی محصولات از اکسل**: بازیابی داده‌های محصولات از فایل اکسل آپلود شده.
- **جستجوی محصولات**: جستجوی محصولات بر اساس یک کوئری.
- **مرتب‌سازی محصولات**: مرتب‌سازی محصولات بر اساس ویژگی‌های مختلف مانند کد، گروه، مکان، طبقه و غیره.
- **ویرایش محصول**: ویرایش اطلاعات محصولات موجود.
- **حذف محصول**: حذف محصولات از لیست.

## پیش‌نیازها

- پایتون 3.x
- جنگو 3.x یا بالاتر
- بسته‌های مورد نیاز پایتون (قابل نصب از طریق `requirements.txt`)

## نصب

1. مخزن را کلون کنید:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

استفاده
مرورگر وب خود را باز کرده و به http://127.0.0.1:8000 بروید.
با مشخصات ابرکاربر که قبلاً ایجاد کرده‌اید، وارد شوید.
از لینک‌های ناوبری برای اضافه کردن محصولات، آپلود فایل‌ها، صادرات به اکسل و بازیابی از اکسل استفاده کنید.
از فرم جستجو برای جستجوی محصولات و مرتب‌سازی آن‌ها با استفاده از دکمه‌های مرتب‌سازی موجود استفاده کنید.