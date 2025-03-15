# SIFT Object Detection

## 📌 معرفی پروژه
این پروژه از الگوریتم **SIFT (Scale-Invariant Feature Transform)** برای شناسایی و تطبیق ویژگی‌های دو تصویر استفاده می‌کند. با استفاده از این روش، می‌توان اشیای مشابه را در دو تصویر مختلف شناسایی کرد.

## 🚀 ویژگی‌ها
- شناسایی ویژگی‌های کلیدی در تصاویر
- مقایسه و تطبیق ویژگی‌های تصاویر ورودی
- نمایش بصری ویژگی‌های استخراج‌شده و تطبیق‌ها
- مدیریت استثناها در صورت بارگذاری ناموفق تصاویر

## 🛠️ پیش‌نیازها
قبل از اجرای پروژه، مطمئن شوید که کتابخانه‌های زیر را نصب کرده‌اید:

```bash
pip install opencv-python numpy matplotlib
```

## 📂 نحوه اجرا
1. دو تصویر موردنظر را در کنار فایل اصلی قرار دهید.
2. نام فایل‌های تصویر را در کد تنظیم کنید:

```python
# بارگذاری تصاویر
i1 = cv2.imread('box.png')
i2 = cv2.imread('box_in_scene.png')
```
3. کد را اجرا کنید:

```bash
python sift_object_detection.py
```

## 🖼️ نمونه خروجی
پس از اجرای کد، پنج تصویر به شما نمایش داده می‌شود:
1. تصویر اول (Query Image)
2. تصویر دوم (Train Image)
3. تطبیق ویژگی‌ها
4. ویژگی‌های تصویر اول
5. ویژگی‌های تصویر دوم

## 📜 توضیحات کد
- استفاده از **SIFT** برای استخراج نقاط کلیدی و توصیفگرها
- مقایسه ویژگی‌های دو تصویر با استفاده از **BFMatcher**
- مرتب‌سازی ویژگی‌های تطبیق‌شده بر اساس کمترین فاصله
- نمایش نتایج با استفاده از **Matplotlib**

## 📧 ارتباط با ما
در صورت داشتن هرگونه سوال یا پیشنهاد، لطفاً با من تماس بگیرید یا یک Issue در **GitHub** ایجاد کنید.

---
😊 موفق باشید!

