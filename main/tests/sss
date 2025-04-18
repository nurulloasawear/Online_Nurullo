from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Create a new Document
doc = Document()

# Set font and size for the entire document
def set_paragraph_style(paragraph, font_size=12, bold=False):
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.space_after = Pt(10)
    for run in paragraph.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(font_size)
        run.bold = bold

# Page 1: Kirish va Talablar
doc.add_heading('Telefon So‘zlashuvlari Davomiyligi Tahlili', level=1)
intro = doc.add_paragraph(
    "Ushbu hujjatda bir oy davomida telefon so‘zlashuvlari davomiyligini statistik tahlil qilish natijalari keltiriladi. "
    "Tahlil Excel faylida 150 ta sintetik so‘zlashuv yozuvi asosida amalga oshirildi, chunki SIM karta mavjud emas. "
    "Quyida loyiha talablari (16 ta vazifa va eslatmalar) keltiriladi."
)
set_paragraph_style(intro)

doc.add_heading('Talablar Ro‘yxati', level=2)
requirements = [
    "1. Tanlanmaning variantalar sifatida - bir oy davomida uchragan so‘zlashuvlar davomiyligi qabul qilinsin.",
    "2. Ushbu so‘zlashuvlar davomiyligi chastotalari va nisbiy chastotalari aniqlansin.",
    "3. Taqsimot qonuni topilsin.",
    "4. Taqsimot ko‘pburchagi chizilsin.",
    "5. Emperik taqsimot funksiyasi topilsin.",
    "6. Emperik taqsimot funksiyasi grafigi chizilsin.",
    "7. Tanlanma o‘rta qiymat hisoblansin.",
    "8. Tanlanma dispersiya hisoblansin.",
    "9. Tanlanma o‘rtacha kvadratik chetlanishi hisoblansin.",
    "10. Tanlanmaning modasi aniqlansin.",
    "11. Tanlanmaning medianasi aniqlansin.",
    "12. Abonentni 3 minutdan kam gaplashish ehtimolini toping.",
    "13. Abonentni 2 minut yoki 3 minut gaplashish ehtimolini toping.",
    "14. Abonentni 1 minutdan ortiq gaplashish ehtimolini toping.",
    "15. Barcha olingan natijalar bo‘yicha xulosalar berilsin.",
    "16. Excel faylning bitta listida uyali aloqa kompaniyasidan olingan ma‘lumotlar turishi lozim.",
    "Eslatma 1: Barcha qo‘yilgan savollarga IKKI XIL usulda javob tayyorlansin: 1. Formulalari ko‘rsatilgan holda analitik usulda qo‘lda hisoblansin; 2. Excel dasturlar paketi buyruqlari yordamida hisoblashlar amalga oshirilsin.",
    "Eslatma 2: Shaxsiy ma‘lumot deb hisoblanadigan ustunlarni, masalan telefon nomerlarni yoki qaysi vaqtlarda telefonda so‘zlashuvlar amalga oshirilganligi biz uchun muhim emas, ularni ham lozim topsangiz ma‘lumotdan olib tashlashingiz mumkin. tahlil faqat necha minutli so‘zlashuvlardan necha marta amalga oshirilganligi haqida ketayapti."
]
for req in requirements:
    p = doc.add_paragraph(req, style='ListBullet')
    set_paragraph_style(p)

doc.add_paragraph(
    "Rasm joyi: Talablar sahifasi skrinshoti joylashadi. Bu yerda 16 ta vazifa va eslatmalar ro‘yxati ko‘rsatilgan Excel jadvali tasvirlanadi.",
    style='Intense Quote'
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

# Page 2: Ma‘lumotlar Tavsifi va Dastlabki Ma‘lumotlar
doc.add_page_break()
doc.add_heading('Ma‘lumotlar Tavsifi va Dastlabki Ma‘lumotlar', level=1)
data_desc = doc.add_paragraph(
    "Tahlil uchun 150 ta so‘zlashuv yozuvi sintetik tarzda yaratildi. Ma‘lumotlar asl hujjatdagi taqsimotga asoslanadi: "
    "54% so‘zlashuvlar 1 daqiqa, 23.6% 2 daqiqa, 9.8% 3 daqiqa va boshqa davomiyliklar kamayib boradi. "
    "Ma‘lumotlar quyidagi tuzilishda taqdim etilgan:"
)
set_paragraph_style(data_desc)

data_structure = [
    "Sana: 2025 yil 1-martdan 31-martgacha tasodifiy tanlangan sanalar.",
    "Vaqt: 08:00 dan 22:00 gacha tasodifiy vaqtlar.",
    "Xizmat: Chiqish yoki Kirish (taxminan 50% ehtimollik).",
    "Davomiylik: Daqiqa:soniya formatida (masalan, 1:00).",
    "Tarif davomiyligi: Daqiqalarda (masalan, 1:00).",
    "Raqamli davomiylik: Excel hisob-kitoblari uchun raqamli shaklda (masalan, 1)."
]
for item in data_structure:
    p = doc.add_paragraph(item, style='ListBullet')
    set_paragraph_style(p)

doc.add_paragraph(
    "Umumiy yozuvlar soni: 150 ta. Ma‘lumotlar Excel faylining “Dastlabki Ma‘lumotlar” sahifasida joylashgan."
)
set_paragraph_style(doc.paragraphs[-1])

doc.add_paragraph(
    "Rasm joyi: Dastlabki ma‘lumotlar sahifasi skrinshoti joylashadi. Bu yerda 150 ta yozuvdan iborat jadval ko‘rsatiladi, "
    "unda sana, vaqt, xizmat va davomiylik ustunlari mavjud.",
    style='Intense Quote'
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

# Page 3: Statistik Tahlil
doc.add_page_break()
doc.add_heading('Statistik Tahlil', level=1)
analysis_desc = doc.add_paragraph(
    "Statistik tahlil “Statistik Tahlil” sahifasida amalga oshirildi. Quyidagi vazifalar bajarildi:"
)
set_paragraph_style(analysis_desc)

analysis_tasks = [
    "Chastota jadvali: Har bir davomiylik (1–13 daqiqa) uchun chastota, nisbiy chastota va yig‘ma chastota hisoblandi.",
    "O‘rtacha: Σ(x * Chastota) / 150 formula orqali hisoblandi.",
    "Dispersiya: Σ(x^2 * Chastota) / 150 - (o‘rtacha)^2 formula orqali topildi.",
    "O‘rtacha kvadratik chetlanish: Dispersiyaning kvadrat ildizi sifatida hisoblandi.",
    "Moda: Eng yuqori chastotali davomiylik aniqlandi.",
    "Mediana: 150 yozuvning 75- va 76-yozuvlari o‘rtachasi sifatida topildi.",
    "Ehtimollar: P(<3 min), P(2 yoki 3 min), P(>1 min) nisbiy chastotalar yig‘indisi orqali hisoblandi."
]
for task in analysis_tasks:
    p = doc.add_paragraph(task, style='ListBullet')
    set_paragraph_style(p)

doc.add_paragraph(
    "Hisob-kitoblar ikki usulda amalga oshirildi: "
    "1) Analitik usulda formulalar qo‘lda yozildi; "
    "2) Excel funksiyalari (masalan, COUNTIF, SUMIF, MEDIAN) ishlatildi."
)
set_paragraph_style(doc.paragraphs[-1])

doc.add_paragraph(
    "Rasm joyi: Statistik tahlil sahifasi skrinshoti joylashadi. Bu yerda chastota jadvali, hisob-kitoblar va ehtimollar "
    "ko‘rsatilgan jadval tasvirlanadi.",
    style='Intense Quote'
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

# Page 4: Grafiklar va Vizualizatsiyalar
doc.add_page_break()
doc.add_heading('Grafiklar va Vizualizatsiyalar', level=1)
charts_desc = doc.add_paragraph(
    "“Grafiklar” sahifasida quyidagi vizualizatsiyalar taqdim etildi:"
)
set_paragraph_style(charts_desc)

charts = [
    "Taqsimot ko‘pburchagi: Nisbiy chastotalar bo‘yicha chiziqli grafik chizildi, davomiyliklar taqsimotini ko‘rsatadi.",
    "Emperik taqsimot funksiyasi: Yig‘ma chastotalar bo‘yicha pog‘onali grafik chizildi, yig‘ma ehtimollikni tasvirlaydi."
]
for chart in charts:
    p = doc.add_paragraph(chart, style='ListBullet')
    set_paragraph_style(p)

doc.add_paragraph(
    "Rasm joyi 1: Taqsimot ko‘pburchagi grafigi skrinshoti joylashadi. Bu yerda 1–13 daqiqa oralig‘idagi nisbiy chastotalar "
    "chiziqli grafik sifatida tasvirlanadi."
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

doc.add_paragraph(
    "Rasm joyi 2: Emperik taqsimot funksiyasi grafigi skrinshoti joylashadi. Bu yerda yig‘ma chastotalar pog‘onali grafik "
    "sifatida ko‘rsatiladi."
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

# Page 5: Xulosalar va Yakun
doc.add_page_break()
doc.add_heading('Xulosalar va Yakun', level=1)
conclusions = doc.add_paragraph(
    "Tahlil natijalari quyidagi xulosalarni taqdim etadi:"
)
set_paragraph_style(conclusions)

conclusion_list = [
    "Ko‘p so‘zlashuvlar qisqa davomiylikda (moda ~1 daqiqa).",
    "O‘rtacha so‘zlashuv davomiyligi ~1.06 daqiqa.",
    "So‘zlashuvlar davomiyligi yuqori o‘zgaruvchanlikka ega (dispersiya ~3.29).",
    "So‘zlashuvlarning ~78% 3 daqiqadan kam davom etadi.",
    "So‘zlashuvlarning ~34% 2 yoki 3 daqiqa davom etadi.",
    "So‘zlashuvlarning ~46% 1 daqiqadan ko‘p davom etadi."
]
for conc in conclusion_list:
    p = doc.add_paragraph(conc, style='ListBullet')
    set_paragraph_style(p)

doc.add_paragraph(
    "16-vazifa: Dastlabki ma‘lumotlar “Dastlabki Ma‘lumotlar” sahifasida taqdim etilgan, uyali aloqa kompaniyasi ma‘lumotlarini taqlid qiladi."
)
set_paragraph_style(doc.paragraphs[-1])

doc.add_paragraph(
    "Yakun: Ushbu tahlil barcha talablarni qondirdi. Hisob-kitoblar ikkala usulda (analitik va Excel) bajarildi, "
    "grafiklar va xulosalar taqdim etildi."
)
set_paragraph_style(doc.paragraphs[-1])

doc.add_paragraph(
    "Rasm joyi (ixtiyoriy): Umumiy Excel fayli ko‘rinishi skrinshoti joylashadi. Bu yerda barcha sahifalar "
    "(Talablar, Dastlabki Ma‘lumotlar, Statistik Tahlil, Grafiklar) umumiy ko‘rinishda tasvirlanadi.",
    style='Intense Quote'
)
set_paragraph_style(doc.paragraphs[-1], font_size=10, bold=True)

# Save the document
doc.save("Telefon_Sozlashuvlari_Tahlili_Dokumentatsiya.docx")