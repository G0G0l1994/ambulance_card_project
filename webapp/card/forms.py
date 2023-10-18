from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TextAreaField, SelectField, IntegerField, FloatField, IntegerRangeField
from wtforms.validators import DataRequired

class CardForm(FlaskForm):
    complaints = TextAreaField("Жалобы", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Жалобы пациента..."})
    anamnesis = TextAreaField("Анамнез", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Анамнез..."})
    condition = SelectField("Общее состояние", choices=[("Удовлетворительное", "Удовлетворительное"), ("Средней степени тяжести", "Средней степени тяжести"), ("Тяжелое", "Тяжелое"), ("Терминальное", "Терминальное")], default=("Удовлетворительное", "Удовлетворительное"))
    conscience = SelectField("Сознание", choices=[("Ясное", "Ясное"), ("Оглушение", "Оглушение"), ("Сопор", "Сопор"), ("Кома", "Кома")])
    glazgo_scale = IntegerField("Шкала Глазго",default=15)
    body_position = SelectField("Положение тела", choices=[("Активное", "Активное"), ("Пассивное", "Пассивное"), ("Вынужденное", "Вынужденное")], default=("Активное", "Активное"))
    t_body = FloatField("Температура тела", default=36.6)
    breath_frequence = IntegerField("ЧДД")
    oxygen_saturation = IntegerField("SpO2")
    heart_rate = IntegerField("ЧСС")
    pulse = IntegerField("Пульс")
    sugar = FloatField("Сахар крови")
    submit = SubmitField("Готово!", render_kw={"class": "btn btn-primary"})