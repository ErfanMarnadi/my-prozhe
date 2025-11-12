import re

msg = input("reshteye khodra vared konid: ")

print("payam asli:")
print("*" * (len(msg) + 4))
print(f"* {msg} *")
print("*" * (len(msg) + 4))

msg_upper = msg.upper()
msg_lower = msg.lower()
print("\n🔹be harfe bozorg: ")
print(msg_upper)
print("🔹be harfe kochak: ")
print(msg_lower)


words = msg.split()
print("\n🔹list kalamat:", words)
print("🔹 tedade kalamat:", len(words))

is_alnum = msg.isalnum()
print("\n🔹 آیا فقط شامل حروف و عدد است؟", is_alnum)
print("🔹 حدس: اگر فقط شامل حروف (A-Z,a-z) یا اعداد باشد → True برمی‌گرداند، در غیر اینصورت (مثلاً فاصله یا !؟) → False")


msg_replaced = msg.replace("Python", "Java")
msg_clean = re.sub(r'[.,!?;:]', '', msg_replaced)
print("\n🔹 بعد از جایگزینی و حذف علائم:")
print(msg_clean)


translation_table = str.maketrans('', '', '@#')
msg_translated = msg_clean.translate(translation_table)
print("\n🔹 بعد از translate (حذف @ و #):")
print(msg_translated)

final_message = " | ".join(msg_translated.split())
print("\n🔹 پیام نهایی با جداکننده | :")
print(final_message)

tab_msg = "Python\tis\tawesome!"
print("\n🔹 رشته با تب:", repr(tab_msg))
expanded_msg = tab_msg.expandtabs(12)
print("🔹 بعد از expandtabs(12):", repr(expanded_msg))
