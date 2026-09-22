import os
from telegram import (
    Update, ReplyKeyboardMarkup, KeyboardButton
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, ContextTypes
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi!")

GROUP_LINK = "https://t.me/+j0dfVujtjmwwODdi"

VIDEOS = [
    {
        "caption": "🎥 Certiport.uz sayti orqali ro'yxatdan o'tish",
        "file_id": "BAACAgEAAxkBAANOarFo6bW14K_y9D38Xp_8rxb35CYAAgkHAAIePThFaYNJPGKMtbk9BA",
    },
    {
        "caption": "🎥 Sertifikatni saytdan yuklab olish",
        "file_id": "BAACAgEAAxkBAANQarFo_XzM6XKrCLCv4vSlYobrPOIAAlsIAAJyofBFR_wrnzpFVG89BA",
    },
    {
        "caption": "🎥 Sertifikat havolasini yuklab olish",
        "file_id": "BAACAgEAAxkBAANSarFpBsoHMaDmLCF1Bq8AAYXSknnXAAJYCgACZTt4RRMR4KH9PeorPQQ",
    },
    {
        "caption": "🎥 ERP bazasiga IC3 sertifikatini kiritish",
        "file_id": "BAACAgIAAxkBAANUarFpGXmTtgABkiIMjnN1zHA91j2aAAIriQACDY2wSHkrrqPlGLNPPQQ",
    },
]

WELCOME_TEXT = """🎓 IC3 DIGITAL LITERACY
📘 GLOBAL STANDARD 6

✨ SIZNI IC3 GS6 KURSIMIZGA TAKLIF QILAMIZ!
🖥 OFFLINE + ONLINE
━━━━━━━━━━━━━━━━━━
📚 KURSDA SIZ:
🔹 Mavzularni to'liq o'rganasiz
🔹 Amaliy mashg'ulotlar bajarasiz
🔹 Testlar ishlaysiz
🔹 Testlarni tahlil qilasiz
🔹 Imtihonga tayyorgarlik ko'rasiz
━━━━━━━━━━━━━━━━━━
📅 Darslar: haftasiga 3 kun
⏳ Davomiyligi: 1 oy
🌐 Ta'lim tili: 🇬🇧 Ingliz / 🇷🇺 Rus tili
💰 Narxi: har bir Level — 500 000 so'm
━━━━━━━━━━━━━━━━━━
📖 O'QUV MANBALARI:
✅ Mualliflik savollari
✅ Ehtimoliy imtihon savollari
✅ IC3 GS6 kitobi
✅ Rus va ingliz tilidagi materiallar
━━━━━━━━━━━━━━━━━━
🚀 IC3 GS6 imtihoniga tayyorgarlikni bugundan boshlang!"""

ADMIN_TEXT = """👨‍💼 Admin bilan bog'lanish:

Quyidagi username yoki telefon raqami orqali bog'laning:

📩 @obidaxmedov
📞 +998 93 472 04 88"""

IMTIHON_TEXT = """📝 Imtihonda qatnashish yo'riqnomasi:

1️⃣ @certiport_uz kanalini kuzatib borish orqali keyingi imtihonlar haqida ma'lumot olishingiz mumkin.

2️⃣ Imtihonga ro'yxatdan o'tish uchun certiport.uz/uz/register saytiga tashrif buyuring. Ro'yxatdan o'tish vaqti esa Telegramdagi "Certiport Uzbekistan" kanalida avvaldan xabar beriladi.

3️⃣ Ro'yxatdan o'tgach, siz register vaqtida kiritgan gmailingizga e-mail boradi. Manashu e-mail orqali imtihonga to'lov qilasiz.

4️⃣ Yanada ko'proq ma'lumot olish uchun @obidaxmedov bilan bog'laning."""

KURS_TEXT = """📚 KURSDA SIZ:
🔹 Mavzularni to'liq o'rganasiz
🔹 Amaliy mashg'ulotlar bajarasiz
🔹 Testlar ishlaysiz
🔹 Testlarni tahlil qilasiz
🔹 Imtihonga tayyorgarlik ko'rasiz
━━━━━━━━━━━━━━━━━━
📅 Darslar: haftasiga 3 kun
⏳ Davomiyligi: 1 oy
🌐 Ta'lim tili: 🇬🇧 Ingliz / 🇷🇺 Rus tili
💰 Narxi: har bir Level — 500 000 so'm
━━━━━━━━━━━━━━━━━━
📖 O'QUV MANBALARI:
✅ Mualliflik savollari
✅ Ehtimoliy imtihon savollari
✅ IC3 GS6 kitobi
✅ Rus va ingliz tilidagi materiallar"""

BTN_ADMIN   = "👨‍💼 Admin Bilan Bog'lanmoqchiman"
BTN_IMTIHON = "📝 Imtihonda qanday qatnashsam bo'ladi?"
BTN_KURS    = "📚 Kursda nimalarni o'rganaman?"
BTN_GROUP   = "➕ Guruhga Qo'shilish"
BTN_VIDEOS  = "🎥 Foydali Videolar"


def main_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(BTN_ADMIN)],
            [KeyboardButton(BTN_IMTIHON)],
            [KeyboardButton(BTN_KURS)],
            [KeyboardButton(BTN_GROUP)],
            [KeyboardButton(BTN_VIDEOS)],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=main_keyboard(),
        disable_web_page_preview=True,
    )


async def handle_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == BTN_ADMIN:
        await update.message.reply_text(ADMIN_TEXT, disable_web_page_preview=True)
    elif text == BTN_IMTIHON:
        await update.message.reply_text(IMTIHON_TEXT, disable_web_page_preview=True)
    elif text == BTN_KURS:
        await update.message.reply_text(KURS_TEXT)
    elif text == BTN_GROUP:
        await update.message.reply_text(
            f"➕ Guruhga qo'shilish uchun quyidagi havolani bosing:\n\n👉 {GROUP_LINK}",
            disable_web_page_preview=False,
        )
    elif text == BTN_VIDEOS:
        await update.message.reply_text("🎥 Foydali videolar:")
        for v in VIDEOS:
            await update.message.reply_video(
                video=v["file_id"],
                caption=v["caption"],
            )
    else:
        await update.message.reply_text(
            "Iltimos, pastdagi tugmalardan birini tanlang 👇",
            reply_markup=main_keyboard(),
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    PORT = int(os.getenv("PORT", "10000"))
    RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")

    if RENDER_URL:
        WEBHOOK_PATH = BOT_TOKEN
        print(f"✅ Webhook rejimida: {RENDER_URL}/{WEBHOOK_PATH}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=WEBHOOK_PATH,
            webhook_url=f"{RENDER_URL}/{WEBHOOK_PATH}",
            drop_pending_updates=True,
        )
    else:
        print("✅ Polling rejimida...")
        app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
