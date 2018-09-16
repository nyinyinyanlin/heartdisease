from django import forms

class RecordForm(forms.Form):
	age = forms.FloatField(
		label='Age',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'10-120',
				'step':'1'
				}),
		min_value=0.0,
		max_value=120.0)

	sex = forms.TypedChoiceField(
		label='Sex',
		choices=(
			('0','Female'),
			('1','Male'),
		),
		initial='0',
		coerce=float)

	cp = forms.TypedChoiceField(
		label='Chest Pain Type',
		choices=(
			('1','Typical Angina'),
			('2','Atypical Angina'),
			('3','Non-anginal Pain'),
			('4','Asymptomatic'),
		),
		initial='1',
		coerce=float)

	trestbps = forms.FloatField(
		label='Resting Blood Pressure - Lower',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'mmHg',
				'step':'1'
				}),
		min_value=0.0,
		max_value=500.0)

	trestbps_upr = forms.FloatField(
		label='Resting Blood Pressure - Upper',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'mmHg',
				'step':'1'
				}),
		min_value=0.0,
		max_value=500.0)

	chol = forms.FloatField(
		label='Serum Cholestrol',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'mg/dl',
				'step':'1'
				}),
		min_value=0.0,
		max_value=500.0)

	fbs = forms.TypedChoiceField(
		label='Fasting Blood Sugar',
		choices=(
			('0','FBS < 120mg/dl'),
			('1','FBS > 120mg/dl'),
		),
		initial='0',
		coerce=float)

	restecg = forms.TypedChoiceField(
		label='Resting Electrocardiographic Results',
		choices=(
			('0','Normal'),
			('1','ST-T Wave Abnormality'),
			('2','Left Ventricular Hypertrophy'),
		),
		initial='0',
		coerce=float)

	thalach = forms.FloatField(
		label='Maximum Heart Rate Achieved',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'bpm',
				'step':'1'
				}),
		min_value=0.0,
		max_value=300.0)

	exang = forms.TypedChoiceField(
		label='Exercise Induced Angina',
		choices=(
			('0','No'),
			('1','Yes'),
		),
		initial='0',
		coerce=float)

	oldpeak = forms.FloatField(
		label='ST Depression Induced by Exercise Relative to Rest',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'',
				'step':'1'
				}),
		min_value=0.0,
		max_value=120.0)

	slope = forms.TypedChoiceField(
		label='Slope of Peak Exercise ST Segment',
		choices=(
			('1','Downsloping'),
			('2','Flat'),
			('3','Upsloping'),
		),
		initial='2',
		coerce=float)

	ca = forms.FloatField(
		label='No. of Major Vessels Colored by Flourosopy',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'0-3',
				'step':'1'
				}),
		min_value=0.0,
		max_value=3.0)

	thal = forms.TypedChoiceField(
		label='Thallium Heart Scan',
		choices=(
			('3','Normal'),
			('6','Fixed Defect'),
			('7','Reversible Defect'),
		),
		initial='0',
		coerce=float)
