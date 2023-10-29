from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField, SelectField, IntegerField, FloatField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired
from webapp import db_session

class CardFormGeneral(FlaskForm):
  complaints = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
  anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
  condition = SelectField("Общее состояние", choices=[("Удовлетворительное", "Удовлетворительное"), ("Средней степени тяжести", "Средней степени тяжести"), ("Тяжелое", "Тяжелое"), ("Терминальное", "Терминальное")], default=("Удовлетворительное"))
  conscience = SelectField("Сознание", choices=[("Ясное", "Ясное"), ("Оглушение", "Оглушение"), ("Сопор", "Сопор"), ("Кома", "Кома")])
  glazgow_scale = IntegerField("Шкала Глазго",default=15)
  body_position = SelectField("Положение тела", choices=[("Активное", "Активное"), ("Пассивное", "Пассивное"), ("Вынужденное", "Вынужденное")], default=("Активное"))
  t_body = FloatField("Температура тела", default=36.6)
  respiratory_rate = IntegerField("ЧДД")
  oxygen_saturation = IntegerField("SpO2")
  heart_rate = IntegerField("ЧСС")
  pulse = IntegerField("Пульс")
  pressure_systolic = IntegerField("Систолическое давление")
  pressure_diastolic = IntegerField("Диастолическое давление")
  blood_glucose = FloatField("Сахар крови")
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class SkinForm(FlaskForm):
  skin_dryness = SelectField("Кожные покровы", choices=[("Сухие", "Сухие"), ("Влажные", "Влажные")], default=("Сухие", "Сухие"))
  skin_colour = SelectField("Цвет", choices=[("Обычной окраски", "Обычные"), ("Бледные", "Бледные"), ("Гиперемированные", "Гиперемированные"), ("Цианоз", "Цианоз")], default=("Обычные"))
  skin_yellowness = StringField("Желтушность", default="Нет")
  skin_rash = SelectField("Сыпь", choices=[("Нет", "Нет"), ("Петехиальная", "Петехиальная"), ("Пустулёзная", "Пустулёзная"), ("Везикулярная", "Везикулярная"), ("Узелковая", "Узелковая"), ("Другое", "Другое")], default=("Нет"))
  skin_throat = SelectField("Зев", choices=[("Спокоен", "Спокоен"), ("Гиперемирован", "Гиперемирован")], default=("Спокоен"))
  skin_tonsils = StringField("Миндfлины", default="Не увеличинены")
  skin_lymph_nodes = StringField("Лимфоузлы", default="Не увеличинены")
  skin_swelling = SelectMultipleField("Отеки", choices=[("Нет", "Нет"), ("Голени", "Голени"), ("Лицо", "Лицо"), ("Туловище", "Туловище"), ("Руки", "Руки")], default=("Нет"))
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})
  
class BreathingSysthem(FlaskForm):
  respiratory_type = SelectField("Тип дыхания", choices=[("Везикулярное", "Везикулярное"), ("Жёсткое", "Жёсткое"), ("Бронхиальное", "Бронхиальное"), ("Пуэриальное", "Пуэрильное"), ("Ослабленное", "Ослабленное"), ("Отсутствует", "Отсутствует")], default=("Везикулярное", "Везикулярное"))
  breath_wheezing = SelectField("Хрипы", choices=[("Нет", "Нет"), ("Влажные", "Влажные"), ("Сухие", "Сухие")], default=("Нет", "Нет"))
  breath_wheezing_localisation = StringField("Локализация хрипов", default="Нет хрипов")
  breath_dyspnea = SelectField("Одышка", choices=[("Нет", "Нет"), ("Инспираторная", "Инспираторная"), ("Экспираторная", "Экспираторная"), ("Смешанная", "Смешанная")], default=("Нет", "Нет"))
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})
  
class HeartForm(FlaskForm):
  heart_sounds = SelectField("Тоны сердца", choices=[("Ритмичные", "Ритмичные"), ("Аритмичные", "Аритмичные")], default=("Ритмичные", "Ритмичные"))
  heart_sounds_type = SelectField("Тоны сердца", choices=[("Ясные", "Ясные"), ("Глухие", "Глухие"), ("Приглушены", "Приглушены"), ("Отсутствуют", "Отсутствуют")], default=("Ясные", "Ясные"))
  heart_murmur = SelectMultipleField("Шум", choices=[("Нет", "Нет"), ("Систолический", "Систолический"),("Диастолический", "Диастолический"), ("Трения перикарда", "Трения перикарда"), ("Другое", "Другое")], default=("Нет", "Нет"))
  pulse_rhythm = SelectField("Ритм пульса", choices=[("Ритмичный", "Ритмичный"), ("Аритмичный", "Аритмичный")], default=("Ритмичный", "Ритмичный"))
  heart_pulse = SelectMultipleField("Пульс", choices=[("Нормальный", "Нормальный"),("Слабого наполнения", "Слабого наполнения"), ("Напряжённый", "Напряжённый"), ("Нитевидный", "Нитевидный"), ("Отсутствует", "Отсутствует")], default=[("Нормальный", "Нормальный")])
  heart_rate_deficit = BooleanField("Дефицит пульса", default=(""))
  heart_accent_tone = StringField("Акцент тона", default=("Нет хрипов"))
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class DisgestionSystem(FlaskForm):
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
  stool_frequence_specific = IntegerField("Частота стула")
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class NervousSystemForm(FlaskForm):
  behaviour = SelectField("Поведение", choices=[("Спокойное", "Спокойное"), ("Возбуждённое", "Возбуждённое"), ("Агрессивное", "Агрессивное"), ("Депрессивное", "Депрессивное")], default=[("Спокойное", "Спокойное")])
  no_meningeal_symptoms = BooleanField(label="Нет менингиальных симптомов:", default=(''))
  symptom_rigidity = BooleanField(label="Ригидность затылочных мыщц:", default=(''))
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
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class UrogentitalSystem(FlaskForm):
  #разбить: болезненное и безболезненное
  #свободно, затруднено отсутствует
  urination =  SelectMultipleField("Мочеиспускание", choices=[("Безболезненное", "Безболезненное"), ("Свободное", "Свободное"), ("Болезненное", "Болезненное"), ("Затруднено", "Затруднено"), ("Отсутствует", "Отсутствует")], default=[("Безболезненное", "Безболезненное"), ("Свободное", "Свободное")])
  pounding_symptom = SelectField("Симптом поколачивания", choices=[("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"), ("Положительный слева", "Положительный слева"), ("Положительный справа", "Положительный справа"), ("Положительный с обеих сторон", "Положительный с обеих сторон"), ("Слабоположительный слева", "Слабоположительный слева"), ("Слабоположительный справа", "Слабоположительный справа"), ("Слабоположительный с обеих сторон", "Слабоположительный с обеих сторон")], default=("Отрицательный с обеих сторон", "Отрицательный с обеих сторон"))
  urine = SelectMultipleField("Моча", choices=[("Светло-жёлтая", "Светло-жёлтая"), ("Мутная", "Мутная"), ("С включениями", "С включениями"), ("С осадком", "С осадком")])
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class StatusLocalisForm(FlaskForm):
  status_localis = TextAreaField("Локальный статус", render_kw={"class": "form-control", "placeholder" : "Локальный статус..."})
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class AidForm(FlaskForm):
  ecg_before_aid =  TextAreaField("ЭКГ до оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ до оказания помощи..."})
  ecg_after_aid =  TextAreaField("ЭКГ после оказания помощи", render_kw={"class": "form-control", "placeholder" : "ЭКГ после оказания помощи..."})
  aid_provided = TextAreaField("Оказанная помощь", render_kw={"class": "form-control", "placeholder" : "Оказанная помощь..."})
  t_body_after_aid = FloatField("Температура тела", default=36.6)
  respiratory_rate_after_aid = IntegerField("ЧДД")
  oxygen_saturation_after_aid = IntegerField("SpO2")
  heart_rate_after_aid = IntegerField("ЧСС")
  pulse_after_aid = IntegerField("Пульс")
  blood_glucose_after_aid = FloatField("Сахар крови")
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})

class DiagnosisForm(FlaskForm):
  diagnosis = TextAreaField("Диагноз", render_kw={"class": "form-control", "placeholder" : "Диагноз..."})
  submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})
