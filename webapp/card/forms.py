from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField, SelectField, IntegerField, FloatField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired
from webapp import db_session


class CardForm(FlaskForm):
  zhaloby = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
  anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
  general_assessment = SelectField("Общее состояние", choices=[("Удовлетворительное", "Удовлетворительное"), ("Средней степени тяжести", "Средней степени тяжести"), ("Тяжелое", "Тяжелое"), ("Терминальное", "Терминальное")], default=("Удовлетворительное"))
  сonsciousness = SelectField("Сознание", choices=[("Ясное", "Ясное"), ("Оглушение", "Оглушение"), ("Сопор", "Сопор"), ("Кома", "Кома")])
  glasgow_scale = IntegerField("Шкала Глазго",default=15)
  body_position = SelectField("Положение тела", choices=[("Активное", "Активное"), ("Пассивное", "Пассивное"), ("Вынужденное", "Вынужденное")], default=("Активное"))
  temperature_before = FloatField("Температура тела", default=36.6)
  respiratory_rate_before = IntegerField("ЧДД",default=16)
  saturation_before = IntegerField("SpO2", default=98)
  heartbite_before = IntegerField("ЧСС", default=60)
  pulse_before = IntegerField("Пульс", default=60)
  blood_pressure_systolic_before = IntegerField("Систолическое давление", default=120)
  blood_pressure_diastolic_before = IntegerField("Диастолическое давление", default=80)
  normal_blood_pressure_systolic = IntegerField("Систолическое давление", default=120)
  normal_blood_pressure_diastolic = IntegerField("Диастолическое давление", default=80)
  blood_glucose_before = FloatField("Сахар крови", default=4)
  dry_skin = SelectField("Кожные покровы", choices=[("Сухие", "Сухие"), ("Влажные", "Влажные")], default="Сухие")
  color_skin = SelectField("Цвет", choices=[("Обычной окраски", "Обычные"), ("Бледные", "Бледные"), ("Гиперемированные", "Гиперемированные"), ("Цианоз", "Цианоз")], default=("Обычные"))
  jaundice = StringField("Желтушность", default="Нет")
  rash = SelectField("Сыпь", choices=[("Нет", "Нет"), ("Петехиальная", "Петехиальная"), ("Пустулёзная", "Пустулёзная"), ("Везикулярная", "Везикулярная"), ("Узелковая", "Узелковая"), ("Другое", "Другое")], default=("Нет"))
  throat = SelectField("Зев", choices=[("Спокоен", "Спокоен"), ("Гиперемирован", "Гиперемирован")], default=("Спокоен"))
  tonsils = StringField("Миндалины", default="Не увеличинены")
  lymph_nodes = StringField("Лимфоузлы", default="Не увеличинены")
  swelling = SelectMultipleField("Отеки", choices=[("Нет", "Нет"), ("Голени", "Голени"), ("Лицо", "Лицо"), ("Туловище", "Туловище"), ("Руки", "Руки")], default=("Нет", "Нет"))
  
  #breathing system
  respiratory_type = SelectField("Тип дыхания", choices=[("Везикулярное", "Везикулярное"), ("Жёсткое", "Жёсткое"), ("Бронхиальное", "Бронхиальное"), ("Пуэриальное", "Пуэрильное"), ("Ослабленное", "Ослабленное"), ("Отсутствует", "Отсутствует")], default=("Везикулярное", "Везикулярное"))
  wheezing = SelectField("Хрипы", choices=[("Нет", "Нет"), ("Влажные", "Влажные"), ("Сухие", "Сухие")], default=("Нет", "Нет"))
  wheezing_localisation = StringField("Локализация хрипов", default="Нет хрипов")
  dyspnea = SelectField("Одышка", choices=[("Нет", "Нет"), ("Инспираторная", "Инспираторная"), ("Экспираторная", "Экспираторная"), ("Смешанная", "Смешанная")], default=("Нет", "Нет"))
  
  #cardiovascular system
  """ heart_sounds = SelectField("Тоны сердца", choices=[("Ритмичные", "Ритмичные"), ("Аритмичные", "Аритмичные")], default=("Ритмичные", "Ритмичные")) """
  tone_of_heart = SelectField("Тоны сердца", choices=[("Ясные", "Ясные"), ("Глухие", "Глухие"), ("Приглушены", "Приглушены"), ("Отсутствуют", "Отсутствуют")], default=("Ясные", "Ясные"))
  murmur = SelectMultipleField("Шум", choices=[("Нет", "Нет"), ("Систолический", "Систолический"),("Диастолический", "Диастолический"), ("Трения перикарда", "Трения перикарда"), ("Другое", "Другое")], default=("Нет", "Нет"))
  rhythmic_tone = SelectField("Ритм тона", choices=[("Ритмичный", "Ритмичный"), ("Аритмичный", "Аритмичный")], default=("Ритмичный", "Ритмичный"))
  rhythmic_pulse = SelectField("Ритм пульса", choices=[("Ритмичный", "Ритмичный"), ("Аритмичный", "Аритмичный")], default=("Ритмичный", "Ритмичный"))
  characteristic_pulse = SelectMultipleField("Пульс", choices=[("Нормальный", "Нормальный"),("Слабого наполнения", "Слабого наполнения"), ("Напряжённый", "Напряжённый"), ("Нитевидный", "Нитевидный"), ("Отсутствует", "Отсутствует")], default=("Нормальный", "Нормальный"))
  heart_rate_deficit = BooleanField("Дефицит пульса", default=(""))
  heart_tone_accent = StringField("Акцент тона", default=("Нет"))
  
  
  #abdominal
  pain_stomach = SelectField("Живот", choices=[("Безболезненный", "Безболезненный"), ("Болезненный", "Болезненный")], default=(("Безболезненный", "Безболезненный")))
  characteristic_stomach = SelectField("Живот", choices=[("Мягкий", "Мягкий"), ("Напряжён", "Напряжён"), ("Вздут", "Вздут")], default=(("Безболезненный", "Безболезненный")))
  involved_in_the_act_of_breathing = BooleanField(label="Участвует в акте дыхания", default=True)
  is_shchetkin_blumberg = BooleanField(label="Щёткина-Блюмберга", default=False)
  is_voskresensky = BooleanField(label="Воскресенского", default=False)
  is_ortner = BooleanField(label="Ортнера", default=False)
  is_rovzinga = BooleanField(label="Ровзинга", default=False)
  is_pasternatsky = BooleanField(label="Пастернацкого", default=False)
  is_sitkovsky = BooleanField(label="Ситковкого", default=False)
  is_obraztsova = BooleanField(label="Образцова", default=False)
  is_murphy = BooleanField(label="Мёрфи", default=False)
  """ other_perritonial_symptoms = StringField("Другие симптомы", default=("Нет")) """
  liver = StringField("Печень", default=("Не увеличена"))
  formed_type_stool = SelectField("Стул", choices=[("Оформлен", "Оформлен"), ("Разжижен", "Разжижен"), ("Жидкий", "Жидкий"), ("Отсутсвует", "Отсутствует")], default=[("Оформлен", "Оформлен")])
  regular_stool = SelectField("Реглярность", choices=[("Регулярный", "Регулярный"), ("Нерегулярный", "Нерегулярный"), ("отсутствует", "Отсутствует")], default=("Регулярный", "Регулярный"))
  rate_stool = IntegerField("Частота стула", default=1)
  
  #nervous system
  behaviour = SelectField("Поведение", choices=[("Спокойное", "Спокойное"), ("Возбуждённое", "Возбуждённое"), ("Агрессивное", "Агрессивное"), ("Депрессивное", "Депрессивное")], default=[("Спокойное", "Спокойное")])
  none_symptoms = BooleanField(label="Нет менингиальных симптомов:", default=False)
  nuchal_rigidity = BooleanField(label="Ригидность затылочных мыщц:", default=False)
  is_kernig_symptom = BooleanField(label="Синдром Кернинга:", default=False)
  is_brudzinski_symptom = BooleanField(label="Синдром Брудзинского:", default=False) 
  reaction_to_light = BooleanField("Реакция на свет:", default="Есть")
  pupils_of_the_eyes = SelectField("Зрачки", choices=[("Нормальные", "Нормальные"), ("Широкие", "Широкие"), ("Узкие", "Узкие")], default=[("Нормальные", "Нормальные")])
  anisocoria = BooleanField("Анизокория:", default=False)
  nystagmus = BooleanField("Нистагм:", default=False)
  focal_signs =  BooleanField("Очаговые симптомы:", default=True)
  speech = SelectField("Речь", choices=[("Внятная", "Внятная"), ("Афазия", "Афазия"), ("Дизартрия", "Дизартрия")], default=[("Внятная", "Внятная")])
  paralysis = SelectField("Параличи, парезы", choices=[("Нет", "Нет"), ("Справа", "Справа"), ("Слева", "Слева")], default=("Нет", "Нет"))
  sensitive = SelectMultipleField("Чувствительность", choices=[("Сохранена", "Сохранена"), ("Отсутствует", "Отсутствует"), ("Снижена", "Снижена"), ("Слева", "Слева"), ("Справа", "Справа")], default=("Сохранена", "Сохранена"))
  
  #urogenital system
  painless_urination = SelectField("Мочеимспускание:", choices=[("Безболезненное", "Безболезненное"), ("Болезненное", "Болезненное")], default=("Безболезненное", "Безболезненное"))
  characteristic_urination =  SelectMultipleField("Мочеиспускание", choices=[("Свободное", "Свободное"), ("Затруднено", "Затруднено"), ("Отсутствует", "Отсутствует")], default=("Свободное", "Свободное"))
  kidney_punch = SelectField("Симптом поколачивания", choices=[("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"), ("Положительный слева", "Положительный слева"), ("Положительный справа", "Положительный справа"), ("Положительный с обеих сторон", "Положительный с обеих сторон"), ("Слабоположительный слева", "Слабоположительный слева"), ("Слабоположительный справа", "Слабоположительный справа"), ("Слабоположительный с обеих сторон", "Слабоположительный с обеих сторон")], default=("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"))
  characteristic_urine = SelectMultipleField("Моча", choices=[("Светло-жёлтая", "Светло-жёлтая"), ("Мутная", "Мутная"), ("С включениями", "С включениями"), ("С осадком", "С осадком")], default=("Светло-жёлтая", "Светло-жёлтая"))
  
  #local status
  status_localis = TextAreaField("Локальный статус", render_kw={"class": "form-control", "placeholder" : "Локальный статус..."})

  #aid
  ecg_before =  TextAreaField("ЭКГ до оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ до оказания помощи..."})
  ecg_after =  TextAreaField("ЭКГ после оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ после оказания помощи..."})
  aid = TextAreaField("Оказанная помощь", render_kw={"class": "form-control", "placeholder" : "Оказанная помощь..."})
  temperature_after = FloatField("Температура тела", default=36.6)
  respiratory_rate_after = IntegerField("ЧДД", default=0)
  saturation_after = IntegerField("SpO2", default=0)
  heartbite_after = IntegerField("ЧСС", default=0)
  pulse_after = IntegerField("Пульс", default=0)
  blood_pressure_systolic_after = IntegerField("Систолическое давление", default=120)
  blood_pressure_diastolic_after = IntegerField("Диастолическое давление", default=80)
  blood_glucose_after = FloatField("Сахар крови", default=4)
  
  #diagnosis
  diagnosis = TextAreaField("Диагноз", render_kw={"class": "form-control", "placeholder" : "Диагноз..."})
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})
