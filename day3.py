# مرح - مهندسة تحكم آلي
# اليوم الثالث: حساب معدل درجات طلاب

print("--- برنامج حساب المعدل ---")

# قائمة فاضية لتخزين الدرجات
grades = []

# عدد الطلاب
num_students = int(input("كم عدد الطلاب؟ "))

# حلقة لإدخال درجات كل طالب
for i in range(num_students):
    grade = float(input(f"أدخلي درجة الطالب {i+1}: "))
    grades.append(grade)

print("\n--- النتائج ---")
print(f"الدرجات: {grades}")

# حساب المعدل
total = sum(grades)
average = total / len(grades)
print(f"المعدل: {average:.2f}")

# تحديد الحالة
if average >= 50:
    print("✅ المعدل مقبول. الطلاب ناجحون.")
else:
    print("⚠️ المعدل ضعيف. يحتاجون إلى دعم إضافي.")

# طباعة درجات كل طالب مع حالته
print("\n--- تفاصيل الطلاب ---")
for idx, g in enumerate(grades, start=1):
    status = "ناجح" if g >= 50 else "راسب"
    print(f"الطالب {idx}: {g} - {status}")