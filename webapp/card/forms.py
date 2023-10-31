from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField, SelectField, IntegerField, FloatField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired
from webapp import db_session


class CardForm(FlaskForm):
  complaints = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
  anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
  general_assessment = SelectField("Общее состояние", choices=[("Удовлетворительное", "Удовлетворительное"), ("Средней степени тяжести", "Средней степени тяжести"), ("Тяжелое", "Тяжелое"), ("Терминальное", "Терминальное")], default=("Удовлетворительное"))
  сonsciousness = SelectField("Сознание", choices=[("Ясное", "Ясное"), ("Оглушение", "Оглушение"), ("Сопор", "Сопор"), ("Кома", "Кома")])
  glazgow_scale = IntegerField("Шкала Глазго",default=15)
  body_position = SelectField("Положение тела", choices=[("Активное", "Активное"), ("Пассивное", "Пассивное"), ("Вынужденное", "Вынужденное")], default=("Активное"))
  t_body = FloatField("Температура тела", default=36.6)
  respiratory_rate = IntegerField("ЧДД")
  oxygen_saturation = IntegerField("SpO2")
  heartbite = IntegerField("ЧСС")
  pulse = IntegerField("Пульс")
  blood_pressure_systolic = IntegerField("Систолическое давление")
  blood_pressure_diastolic = IntegerField("Диастолическое давление")
  normal_blood_pressure_systolic = IntegerField("Систолическое давление")
  normal_blood_pressure_diastolic = IntegerField("Диастолическое давление")
  blood_glucose = FloatField("Сахар крови")
  dry_skin = SelectField("Кожные покровы", choices=[("Сухие", "Сухие"), ("Влажные", "Влажные")], default="Сухие")
  colour_skin = SelectField("Цвет", choices=[("Обычной окраски", "Обычные"), ("Бледные", "Бледные"), ("Гиперемированные", "Гиперемированные"), ("Цианоз", "Цианоз")], default=("Обычные"))
  jaundice = StringField("Желтушность", default="Нет")
  skin_rash = SelectField("Сыпь", choices=[("Нет", "Нет"), ("Петехиальная", "Петехиальная"), ("Пустулёзная", "Пустулёзная"), ("Везикулярная", "Везикулярная"), ("Узелковая", "Узелковая"), ("Другое", "Другое")], default=("Нет"))
  throat = SelectField("Зев", choices=[("Спокоен", "Спокоен"), ("Гиперемирован", "Гиперемирован")], default=("Спокоен"))
  tonsils = StringField("Миндfлины", default="Не увеличинены")
  lymph_nodes = StringField("Лимфоузлы", default="Не увеличинены")
  swelling = SelectMultipleField("Отеки", choices=[("Нет", "Нет"), ("Голени", "Голени"), ("Лицо", "Лицо"), ("Туловище", "Туловище"), ("Руки", "Руки")], default=("Нет"))
  
  #breathing system
  respiratory_type = SelectField("Тип дыхания", choices=[("Везикулярное", "Везикулярное"), ("Жёсткое", "Жёсткое"), ("Бронхиальное", "Бронхиальное"), ("Пуэриальное", "Пуэрильное"), ("Ослабленное", "Ослабленное"), ("Отсутствует", "Отсутствует")], default=("Везикулярное", "Везикулярное"))
  wheezing = SelectField("Хрипы", choices=[("Нет", "Нет"), ("Влажные", "Влажные"), ("Сухие", "Сухие")], default=("Нет", "Нет"))
  wheezing_localisation = StringField("Локализация хрипов", default="Нет хрипов")
  breath_dyspnea = SelectField("Одышка", choices=[("Нет", "Нет"), ("Инспираторная", "Инспираторная"), ("Экспираторная", "Экспираторная"), ("Смешанная", "Смешанная")], default=("Нет", "Нет"))
  
  #cardiovascular system
  heart_sounds = SelectField("Тоны сердца", choices=[("Ритмичные", "Ритмичные"), ("Аритмичные", "Аритмичные")], default=("Ритмичные", "Ритмичные"))
  heart_sounds_type = SelectField("Тоны сердца", choices=[("Ясные", "Ясные"), ("Глухие", "Глухие"), ("Приглушены", "Приглушены"), ("Отсутствуют", "Отсутствуют")], default=("Ясные", "Ясные"))
  heart_murmur = SelectMultipleField("Шум", choices=[("Нет", "Нет"), ("Систолический", "Систолический"),("Диастолический", "Диастолический"), ("Трения перикарда", "Трения перикарда"), ("Другое", "Другое")], default=("Нет", "Нет"))
  pulse_rhythm = SelectField("Ритм пульса", choices=[("Ритмичный", "Ритмичный"), ("Аритмичный", "Аритмичный")], default=("Ритмичный", "Ритмичный"))
  heart_pulse = SelectMultipleField("Пульс", choices=[("Нормальный", "Нормальный"),("Слабого наполнения", "Слабого наполнения"), ("Напряжённый", "Напряжённый"), ("Нитевидный", "Нитевидный"), ("Отсутствует", "Отсутствует")], default=[("Нормальный", "Нормальный")])
  heart_rate_deficit = BooleanField("Дефицит пульса", default=(""))
  heart_accent_tone = StringField("Акцент тона", default=("Нет хрипов"))
  
  
  #abdominal
  stomach_general = SelectField("Живот", choices=[("Болезненный", "Болезненный"), ("Безболезненный", "Безболезненный")], default=(("Безболезненный", "Безболезненный")))
  stomach_charasteristics = SelectField("Живот", choices=[("Мягкий", "Мягкий"), ("Напряжён", "Напряжён"), ("Вздут", "Вздут")], default=(("Безболезненный", "Безболезненный")))
  stomach_participation_in_breathing = BooleanField(label="Участвует в акте дыхания", default="")
  sypmtom_shchetkin_blumberg = BooleanField(label="Щёткина-Блюмберга", default="")
  symptom_voskresensky = BooleanField(label="Воскресенского", default="")
  symptom_ortner = BooleanField(label="Ортнера", default="")
  symptom_rovzing = BooleanField(label="Ровзинга", default="")
  symptom_pasternatsky = BooleanField(label="Пастернацкого", default="")
  symptom_sitkovsky = BooleanField(label="Ситковкого", default="")
  symptom_obraztsov = BooleanField(label="Образцова", default="")
  symptom_murphy = BooleanField(label="Мёрфи", default="")
  other_perritonial_symptoms = StringField("Другие симптомы", default=("Нет"))
  liver = StringField("Печень", default=("Не увеличена"))
  stool_type = SelectField("Стул", choices=[("Оформлен", "Оформлен"), ("Разжижен", "Разжижен"), ("Жидкий", "Жидкий"), ("Отсутсвует", "Отсутствует")], default=[("Оформлен", "Оформлен")])
  stool_frequence_general = SelectField("Реглярность", choices=[("Регулярный", "Регулярный"), ("Нерегулярный", "Нерегулярный"), ("отсутствует", "Отсутствует")], default=("Регулярный", "Регулярный"))
  frequency_of_bowel_movement = IntegerField("Частота стула")
  
  #nervous system
  behaviour = SelectField("Поведение", choices=[("Спокойное", "Спокойное"), ("Возбуждённое", "Возбуждённое"), ("Агрессивное", "Агрессивное"), ("Депрессивное", "Депрессивное")], default=[("Спокойное", "Спокойное")])
  no_meningeal_symptoms = BooleanField(label="Нет менингиальных симптомов:", default=(''))
  nuchal_rigidity = BooleanField(label="Ригидность затылочных мыщц:", default=(''))
  symptom_kerning = BooleanField(label="Синдром Кернинга:", default=(''))
  symptom_brudzinski = BooleanField(label="Синдром Брудзинского:", default=('')) 
  reaction_to_light = BooleanField("Реакция на свет:", default=("Есть"))
  pupils = SelectField("Зрачки", choices=[("Нормальные", "Нормальные"), ("Широкие", "Широкие"), ("Узкие", "Узкие")], default=[("Нормальные", "Нормальные")])
  anisocoria = BooleanField("Анизокория:", default=("Есть"))
  nystagmus = BooleanField("Нистагм:", default=("Есть"))
  focal_signs =  BooleanField("Очаговые симптомы:", default=("Есть"))
  speech = SelectField("Речь", choices=[("Внятная", "Внятная"), ("Афазия", "Афазия"), ("Дизартрия", "Дизартрия")], default=[("Внятная", "Внятная")])
  paralysis = SelectField("Параличи, парезы", choices=[("Нет", "Нет"), ("Справа", "Справа"), ("Слева", "Слева")], default=[("Нет", "Нет")])
  sensitivity = SelectMultipleField("Чувствительность", choices=[("Сохранена", "Сохранена"), ("Отсутствует", "Отсутствует"), ("Снижена", "Снижена"), ("Слева", "Слева"), ("Справа", "Справа")], default=[("Сохранена", "Сохранена")])
  
  #urogenital system
  painless_urination = SelectField("Мочеимспускание:", choices=[("Безболезненное", "Безболезненное"), ("Болезненное", "Болезненное")], default=("Безболезненное", "Безболезненное"))
  urination =  SelectMultipleField("Мочеиспускание", choices=[("Свободное", "Свободное"), ("Затруднено", "Затруднено"), ("Отсутствует", "Отсутствует")], default=[("Свободное", "Свободное")])
  kidney_punch = SelectField("Симптом поколачивания", choices=[("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"), ("Положительный слева", "Положительный слева"), ("Положительный справа", "Положительный справа"), ("Положительный с обеих сторон", "Положительный с обеих сторон"), ("Слабоположительный слева", "Слабоположительный слева"), ("Слабоположительный справа", "Слабоположительный справа"), ("Слабоположительный с обеих сторон", "Слабоположительный с обеих сторон")], default=("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"))
  urine = SelectMultipleField("Моча", choices=[("Светло-жёлтая", "Светло-жёлтая"), ("Мутная", "Мутная"), ("С включениями", "С включениями"), ("С осадком", "С осадком")])
  
  #local status
  status_localis = TextAreaField("Локальный статус", render_kw={"class": "form-control", "placeholder" : "Локальный статус..."})

  #aid
  ecg_before_aid =  TextAreaField("ЭКГ до оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ до оказания помощи..."})
  ecg_after_aid =  TextAreaField("ЭКГ после оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ после оказания помощи..."})
  aid_provided = TextAreaField("Оказанная помощь", render_kw={"class": "form-control", "placeholder" : "Оказанная помощь..."})
  temperature_after_aid = FloatField("Температура тела", default=36.6)
  respiratory_rate_after_aid = IntegerField("ЧДД")
  oxygen_saturation_after_aid = IntegerField("SpO2")
  heartbite_after_aid = IntegerField("ЧСС")
  pulse_after_aid = IntegerField("Пульс")
  blood_pressure_systolic_after_aid = IntegerField("Систолическое давление")
  blood_pressure_diastolic_after_aid = IntegerField("Диастолическое давление")
  blood_glucose_after_aid = FloatField("Сахар крови")
  
  #diagnosis
  diagnosis = TextAreaField("Диагноз", render_kw={"class": "form-control", "placeholder" : "Диагноз..."})
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})
