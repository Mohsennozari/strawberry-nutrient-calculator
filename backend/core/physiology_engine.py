from .data_sources import DataSources
from .alerts_engine import AlertsEngine

class PhysiologyEngine:
    """موتور اصلی محاسبات فیزیولوژیکی توت‌فرنگی"""

    def __init__(self):
        self.data = DataSources()
        self.alerts = AlertsEngine(self.data)
        self.optimal_ec_ph = self.data.optimal_ec_ph

    def validate_inputs(self, data):
        """اعتبارسنجی کامل ورودی‌ها"""
        errors = []

        validations = {
            'crown_diameter': (5, 25, 'میلی‌متر'),
            'plant_height': (10, 40, 'سانتی‌متر'),
            'petiole_length': (5, 25, 'سانتی‌متر'),
            'leaf_length': (3, 12, 'سانتی‌متر'),
            'leaf_width': (2, 8, 'سانتی‌متر'),
            'fruit_size': (1, 15, 'سانتی‌متر مربع'),
            'age_days': (0, 200, 'روز'),
            'fruits_per_plant': (0, 15, 'عدد'),
            'temp_c': (0, 45, 'درجه سانتی‌گراد'),
            'ec': (0, 5.0, 'dS/m'),
            'ph': (0, 14, '')
        }

        for field, (min_val, max_val, unit) in validations.items():
            value = data.get(field, 0)
            if value < min_val or value > max_val:
                errors.append(f'{field} باید بین {min_val} تا {max_val} {unit} باشد (دریافت: {value})')

        weather = data.get('weather', '')
        if weather and weather not in ['sunny', 'cloudy', 'partly_cloudy']:
            errors.append(f'وضعیت هوا باید sunny, cloudy یا partly_cloudy باشد (دریافت: {weather})')

        return errors

    def determine_stage(self, data):
        """تشخیص مرحله رشد بر اساس قطر طوقه و سن"""
        crown = data.get('crown_diameter', 0)
        age = data.get('age_days', 0)

        if crown < 12 or age < 30:
            return 'vegetative'
        elif 12 <= crown < 14 or (30 <= age < 60):
            return 'flowering'
        elif 14 <= crown < 17 or (60 <= age < 120):
            return 'fruiting'
        else:
            return 'maturity'

    def apply_corrections(self, ppm, data):
        """اعمال ضرایب اصلاحی (دما، هوا، تعداد میوه)"""
        corrected = ppm.copy()

        temp = data.get('temp_c', 25)
        if temp > 28:
            corrected['Ca'] = round(corrected['Ca'] * 1.10, 2)
            corrected['K'] = round(corrected['K'] * 1.05, 2)

        if data.get('weather') == 'cloudy':
            corrected['N'] = round(corrected['N'] * 0.85, 2)

        if data.get('fruits_per_plant', 0) > 6:
            corrected['K'] = round(corrected['K'] * 1.10, 2)
            corrected['Ca'] = round(corrected['Ca'] * 1.10, 2)

        return corrected

    def apply_ec_ph_corrections(self, ppm, ec, ph):
        """
        اعمال اصلاحات بر اساس EC و pH
        - pH بالا (۶.۵+) → آهن و منگنز رسوب می‌کنند → افزایش Fe و Mn
        - pH پایین (۵.۵-) → کلسیم و منیزیم جذب نمی‌شوند → افزایش Ca و Mg
        - EC بالا (۲.۵+) → تنش اسمزی → افزایش همه عناصر
        - EC پایین (۱.۰-) → جذب بیش‌ازحد → کاهش همه عناصر
        """
        corrected = ppm.copy()

        if ph > 6.5:
            corrected['Fe'] = round(ppm['Fe'] * 1.3, 2)
            corrected['Mn'] = round(ppm['Mn'] * 1.3, 2)
            corrected['Zn'] = round(ppm['Zn'] * 1.2, 2)
            corrected['Cu'] = round(ppm['Cu'] * 1.2, 2)
        elif ph < 5.5:
            corrected['Ca'] = round(ppm['Ca'] * 1.2, 2)
            corrected['Mg'] = round(ppm['Mg'] * 1.2, 2)
            corrected['P'] = round(ppm['P'] * 1.15, 2)
            corrected['K'] = round(ppm['K'] * 1.05, 2)

        if ec > 2.5:
            for key in corrected:
                corrected[key] = round(corrected[key] * 1.08, 2)
        elif ec < 1.0:
            for key in corrected:
                corrected[key] = round(corrected[key] * 0.92, 2)

        return corrected

    def calculate_ratios(self, ppm):
        """محاسبه ۷ نسبت کلیدی"""
        return {
            'K_Ca': ppm['K'] / ppm['Ca'] if ppm['Ca'] > 0 else 0,
            'K_Mg': ppm['K'] / ppm['Mg'] if ppm['Mg'] > 0 else 0,
            'Ca_Mg': ppm['Ca'] / ppm['Mg'] if ppm['Mg'] > 0 else 0,
            'N_K': ppm['N'] / ppm['K'] if ppm['K'] > 0 else 0,
            'K_S': ppm['K'] / ppm['S'] if ppm['S'] > 0 else 0,
            'Fe_Mn': ppm['Fe'] / ppm['Mn'] if ppm['Mn'] > 0 else 0,
            'B_Ca': ppm['B'] / ppm['Ca'] if ppm['Ca'] > 0 else 0
        }

    def predict_fruit_weight(self, fruit_size_cm2, stage, cultivar='Albion'):
        """پیش‌بینی وزن میوه با مدل غیرخطی (Frontiers 2024)"""
        if fruit_size_cm2 <= 0:
            return 0

        if stage == 'fruiting':
            weight = 1.2 * (fruit_size_cm2 ** 0.85) + 0.8
        elif stage == 'maturity':
            weight = 1.1 * (fruit_size_cm2 ** 0.90) + 0.5
        elif stage == 'flowering':
            weight = 0.9 * (fruit_size_cm2 ** 0.95) + 0.3
        else:
            weight = 0.8 * (fruit_size_cm2 ** 0.95) + 0.2

        cultivar_factor = {
            'Albion': 1.0,
            'Camarosa': 0.95,
            'Sweet Charlie': 0.90
        }

        return weight * cultivar_factor.get(cultivar, 1.0)

    def get_ec_ph_status(self, data):
        """تعیین وضعیت EC و pH"""
        ec = data.get('ec', 1.8)
        ph = data.get('ph', 6.0)
        opt = self.optimal_ec_ph

        def get_status(value, ranges):
            if value < ranges['min']:
                return 'low'
            elif value > ranges['max']:
                return 'high'
            elif ranges['optimal_min'] <= value <= ranges['optimal_max']:
                return 'optimal'
            else:
                return 'acceptable'

        return {
            'EC': {
                'value': ec,
                'status': get_status(ec, opt['EC']),
                'range': f"{opt['EC']['min']} - {opt['EC']['max']} dS/m",
                'optimal': f"{opt['EC']['optimal_min']} - {opt['EC']['optimal_max']} dS/m",
                'source': opt['EC']['source']
            },
            'pH': {
                'value': ph,
                'status': get_status(ph, opt['pH']),
                'range': f"{opt['pH']['min']} - {opt['pH']['max']}",
                'optimal': f"{opt['pH']['optimal_min']} - {opt['pH']['optimal_max']}",
                'source': opt['pH']['source']
            }
        }

    def calculate(self, data):
        """محاسبه اصلی سیستم"""
        # ۱. اعتبارسنجی
        errors = self.validate_inputs(data)
        if errors:
            return {'errors': errors}

        # ۲. تشخیص مرحله رشد
        stage = self.determine_stage(data)

        # ۳. دریافت PPM پایه
        ppm = {}
        for element in self.data.nutrient_sources:
            source_data = self.data.get_ppm_with_source(element, stage)
            if source_data:
                ppm[element] = source_data['value']

        # ۴. اعمال اصلاحات محیطی
        ppm = self.apply_corrections(ppm, data)

        # ۵. اعمال اصلاحات EC و pH
        ec = data.get('ec', 1.8)
        ph = data.get('ph', 6.0)
        ppm = self.apply_ec_ph_corrections(ppm, ec, ph)

        # ۶. محاسبه نسبت‌ها
        ratios = self.calculate_ratios(ppm)

        # ۷. پیش‌بینی وزن میوه
        fruit_weight = self.predict_fruit_weight(
            data.get('fruit_size', 0),
            stage,
            data.get('cultivar', 'Albion')
        )

        # ۸. تولید هشدارها
        alerts = self.alerts.generate_weighted_alerts(ppm, data, ratios)

        # ۹. تولید توصیه‌ها
        recommendations = self.alerts.generate_precise_recommendations(ppm, ec, ph, alerts)

        # ۱۰. وضعیت سلامت
        health_status = self.alerts.determine_health_status(alerts)

        # ۱۱. وضعیت EC و pH
        ec_ph = self.get_ec_ph_status(data)

        return {
            'stage': stage,
            'ppm': {k: round(v, 2) for k, v in ppm.items()},
            'ratios': {k: round(v, 2) for k, v in ratios.items()},
            'ec_ph': ec_ph,
            'fruit_weight_prediction': round(fruit_weight, 1),
            'alerts': alerts,
            'recommendations': recommendations,
            'health_status': health_status,
            'nutrient_sources': self.data.get_nutrient_sources(stage)
        }
