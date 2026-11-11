from vid import build
URL="trading-force.onrender.com"
# 1) How to join
build("how_to_join",[
 (0,3,"<div class='ar'>تشترك في VIP<br><span class='grad'>في دقيقتين</span></div><div class='ar2' style='margin-top:30px'>٤ خطوات بس 👇</div>"),
 (3,6,"<div class='num'>1</div><div class='ar'>اضغط اللينك<br>اللي في البايو</div><div class='url'>"+URL+"</div>"),
 (6,9,"<div class='num'>2</div><div class='ar'>اضغط الزرار الأزرق</div><div class='btnm'>Get VIP access · $30 →</div>"),
 (9,12,"<div class='num'>3</div><div class='ar'>اختار USDT وادفع</div><div class='ar2' style='margin-top:30px'>نفس المبلغ اللي مكتوب بالظبط</div>"),
 (12,15,"<div class='num'>4</div><div class='ar'>البوت يبعتلك<br>لينك القناة 🎉</div><div class='btnm' style='background:linear-gradient(90deg,#0f9d74,var(--win))'>Get my invite →</div>"),
 (15,19,"<div class='ar'>مش معاك USDT؟<br><span class='grad'>متقلقش</span></div><div class='ar2' style='margin-top:30px'>ابعتلنا <span class='gold'>«ذهب»</span> في الخاص<br>وهنشرحلك خطوة بخطوة</div>")],19,
 risk="الدفع من الموقع بس · محدش مننا هيكلمك الأول")
# 2) 3 mistakes
build("three_mistakes",[
 (0,3,"<div class='ar'>٣ غلطات<br><span class='grad'>بتضيّع حسابات الدهب</span></div><div class='ar2' style='margin-top:30px'>إنت بتعمل كام واحدة منهم؟</div>"),
 (3,7,"<div class='num numr'>1</div><div class='ar'>تدخل من غير<br>وقف خسارة</div><div class='ar2' style='margin-top:30px'>حركة واحدة عكسك تمسح مكسب أسابيع</div>"),
 (7,11,"<div class='num numr'>2</div><div class='ar'>تخاطر بمبلغ كبير</div><div class='ar2' style='margin-top:30px'>خليها ١-٢٪ من حسابك بس</div>"),
 (11,15,"<div class='num numr'>3</div><div class='ar'>تتداول وقت<br>الأخبار الأمريكية</div><div class='ar2' style='margin-top:30px'>السعر بينط والسبريد بيوسع. استنى</div>"),
 (15,19,"<div class='ar'>احفظ الفيديو 📌</div><div class='ar2' style='margin-top:30px'>وتابعنا لدروس وصفقات الدهب كل يوم</div><div class='ar2 gold'>ابعتلنا «ذهب» لو عندك سؤال</div>")],19)
# 3) Sessions
build("gold_sessions",[
 (0,3,"<div class='ar'>الدهب بيتحرك<br><span class='grad'>إمتى أكتر؟</span></div><div class='ar2' style='margin-top:30px'>بتوقيت القاهرة 🇪🇬</div>"),
 (3,6.5,"<div class='time' style='color:var(--muted)'>01:00</div><div class='ar' style='margin-top:30px'>الجلسة الآسيوية</div><div class='ar2'>هادية ونطاقات صغيرة</div>"),
 (6.5,10,"<div class='time' style='color:var(--blue-2)'>10:00</div><div class='ar' style='margin-top:30px'>افتتاح لندن</div><div class='ar2'>أول حركة قوية في اليوم</div>"),
 (10,13.5,"<div class='time' style='color:var(--loss)'>15:30</div><div class='ar' style='margin-top:30px'>الأخبار الأمريكية</div><div class='ar2'>أعلى تقلب، خلي بالك هنا</div>"),
 (13.5,17,"<div class='time' style='color:var(--blue-2)'>16:30</div><div class='ar' style='margin-top:30px'>افتتاح نيويورك</div><div class='ar2'>موجة قوية تانية</div>"),
 (17,20,"<div class='ar'>احفظ الفيديو 📌</div><div class='ar2' style='margin-top:30px'>معظم صفقاتنا بتيجي وقت لندن ونيويورك</div><div class='ar2 gold'>تابعنا عشان تاخدها لايف</div>")],20,
 risk="التداول فيه مخاطرة · المواعيد بتوقيت أمريكا الشتوي")
print("ok")
