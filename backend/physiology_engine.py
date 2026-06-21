class PhysiologyEngine:
    def __init__(self):
        self.base_ppm = {
            'vegetative': {
                'N': 160, 'P': 55, 'K': 420, 'Ca': 280, 'Mg': 60,
                'S': 45, 'Fe': 2.2, 'Zn': 0.45, 'Mn': 0.75, 'Cu': 0.20,
                'B': 0.35, 'Mo': 0.03, 'Cl': 1.0
            },
            'flowering': {
                'N': 150, 'P': 58, 'K': 470, 'Ca': 320, 'Mg': 65,
                'S': 50, 'Fe': 2.5, 'Zn': 0.50, 'Mn': 0.85, 'Cu': 0.25,
                'B': 0.40, 'Mo': 0.04, 'Cl': 1.2
            },
            'fruiting': {
                'N': 165, 'P': 58, 'K': 480, 'Ca': 340, 'Mg': 70,
                'S': 55, 'Fe': 2.8, 'Zn': 0.55, 'Mn': 0.90, 'Cu': 0.25,
                'B': 0.45, 'Mo': 0.04, 'Cl': 1.3
            },
            'maturity': {
                'N': 140, 'P': 50, 'K': 420, 'Ca': 320, 'Mg': 60,
                'S': 45, 'Fe': 2.0, 'Zn': 0.40, 'Mn': 0.70, 'Cu': 0.20,
                'B': 0.30, 'Mo': 0.03, 'Cl': 1.0
            }
        }

        self.optimal_ranges = {
            'N': {'min': 156, 'max': 172},
            'P': {'min': 54, 'max': 63},
            'K': {'min': 400, 'max': 543},
            'Ca': {'min': 244, 'max': 449},
            'Mg': {'min': 40, 'max': 70},
            'S': {'min': 30, 'max': 60},
            'Fe': {'min': 1.5, 'max': 3.0},
            'Zn': {'min': 0.3, 'max': 0.6},
            'Mn': {'min': 0.5, 'max': 1.0},
            'Cu': {'min': 0.1, 'max': 0.3},
            'B': {'min': 0.2, 'max': 0.5},
            'Mo': {'min': 0.01, 'max': 0.05},
            'Cl': {'min': 0.5, 'max': 1.5}
        }

        self.optimal_ratios = {
            'K_Ca': {'min': 1.2, 'max': 1.4},
            'K_Mg': {'min': 3.0, 'max': 4.0},
            'Ca_Mg': {'min': 2.5, 'max': 3.5},
            'N_K': {'min': 0.3, 'max': 0.4},
            'K_S': {'min': 8.0, 'max': 10.0},
            'Fe_Mn': {'min': 2.0, 'max': 3.0},
            'B_Ca': {'min': 0.001, 'max': 0.002}
        }

        self.optimal_ec_ph = {
            'EC': {'min': 1.0, 'max': 2.5, 'optimal_min': 1.5, 'optimal_max': 2.0},
            'pH': {'min': 5.5, 'max': 6.5, 'optimal_min': 5.8, 'optimal_max': 6.2}
        }

    def _safe_float(self, data, key, default=0):
        try:
            return float(data.get(key, default))
        except (TypeError, ValueError):
            return default

    def calculate(self, data):
        if not isinstance(data, dict):
            raise ValueError('ورودی باید یک دیکشنری باشد')

        stage = self.determine_stage(data)
        ppm = self.base_ppm[stage].copy()
        ppm = self.apply_corrections(ppm, data)
        ratios = self.calculate_ratios(ppm)
        fruit_weight = self.predict_fruit_weight(self._safe_float(data, 'fruit_size', 0))
        alerts = self.generate_alerts(ppm, data, ratios)
        recommendations = self.generate_recommendations(ppm, data, alerts)
        health_status = self.determine_health_status(alerts)
        ec_ph = self.get_ec_ph_status(data)

        return {
            'stage': stage,
            'ppm': {k: round(v, 2) for k, v in ppm.items()},
            'ratios': {k: round(v, 2) for k, v in ratios.items()},
            'ec_ph': ec_ph,
            'fruit_weight_prediction': round(fruit_weight, 1),
            'alerts': alerts,
            'recommendations': recommendations,
            'health_status': health_status
        }

    def determine_stage(self, data):
        crown = self._safe_float(data, 'crown_diameter', 0)
        age = self._safe_float(data, 'age_days', 0)

        if crown < 12 or age < 30:
            return 'vegetative'
        elif 12 <= crown < 14 or (30 <= age < 60):
            return 'flowering'
        elif 14 <= crown < 17 or (60 <= age < 120):
            return 'fruiting'
        else:
            return 'maturity'

    def apply_corrections(self, ppm, data):
        corrected = ppm.copy()

        temp = self._safe_float(data, 'temp_c', 25)
        if temp > 28:
            corrected['Ca'] *= 1.10
            corrected['K'] *= 1.05

        if data.get('weather') == 'cloudy':
            corrected['N'] *= 0.85

        if self._safe_float(data, 'fruits_per_plant', 0) > 6:
            corrected['K'] *= 1.10
            corrected['Ca'] *= 1.10

        return corrected

    def calculate_ratios(self, ppm):
        return {
            'K_Ca': ppm['K'] / ppm['Ca'] if ppm['Ca'] > 0 else 0,
            'K_Mg': ppm['K'] / ppm['Mg'] if ppm['Mg'] > 0 else 0,
            'Ca_Mg': ppm['Ca'] / ppm['Mg'] if ppm['Mg'] > 0 else 0,
            'N_K': ppm['N'] / ppm['K'] if ppm['K'] > 0 else 0,
            'K_S': ppm['K'] / ppm['S'] if ppm['S'] > 0 else 0,
            'Fe_Mn': ppm['Fe'] / ppm['Mn'] if ppm['Mn'] > 0 else 0,
            'B_Ca': ppm['B'] / ppm['Ca'] if ppm['Ca'] > 0 else 0
        }

    def predict_fruit_weight(self, fruit_size_cm2):
        if fruit_size_cm2 <= 0:
            return 0
        return 0.87 * fruit_size_cm2 + 1.2

    def get_ec_ph_status(self, data):
        ec = self._safe_float(data, 'ec', 1.8)
        ph = self._safe_float(data, 'ph', 6.0)

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
                'optimal': f"{opt['EC']['optimal_min']} - {opt['EC']['optimal_max']} dS/m"
            },
            'pH': {
                'value': ph,
                'status': get_status(ph, opt['pH']),
                'range': f"{opt['pH']['min']} - {opt['pH']['max']}",
                'optimal': f"{opt['pH']['optimal_min']} - {opt['pH']['optimal_max']}"
            }
        }

    def generate_alerts(self, ppm, data, ratios):
        alerts = []

        for name, ratio in ratios.items():
            if name in self.optimal_ratios:
                opt = self.optimal_ratios[name]
                if ratio > opt['max']:
                    alerts.append(f"\u26a0\ufe0f نسبت {name.replace('_', ':')} = {ratio:.2f} بالاست (بهینه: {opt['min']}-{opt['max']})")
                elif ratio < opt['min']:
                    alerts.append(f"\u26a0\ufe0f نسبت {name.replace('_', ':')} = {ratio:.2f} پایین است (بهینه: {opt['min']}-{opt['max']})")

        for element, value in ppm.items():
            if element in self.optimal_ranges:
                opt = self.optimal_ranges[element]
                if value < opt['min']:
                    alerts.append(f"\u26a0\ufe0f {element} = {value:.2f} ppm پایین است (بهینه: {opt['min']}-{opt['max']})")
                elif value > opt['max']:
                    alerts.append(f"\u26a0\ufe0f {element} = {value:.2f} ppm بالاست (بهینه: {opt['min']}-{opt['max']})")

        temp = self._safe_float(data, 'temp_c', 25)
        if temp > 30:
            alerts.append("\u26a0\ufe0f دمای بالای ۳۰ درجه! خطر تنش گرمایی")
        elif temp < 15:
            alerts.append("\u26a0\ufe0f دمای زیر ۱۵ درجه! رشد گیاه کند می‌شود")

        if self._safe_float(data, 'fruits_per_plant', 0) > 8:
            alerts.append("\u26a0\ufe0f تعداد میوه زیاد است! نیاز به K و Ca افزایش یافته")

        return alerts

    def generate_recommendations(self, ppm, data, alerts):
        recs = []

        for alert in alerts:
            if 'K:Ca' in alert:
                recs.append("\ud83d\udca1 یک بار محلول‌پاشی نیترات کلسیم (۰.۳٪) انجام دهید.")
            elif 'K:Mg' in alert:
                recs.append("\ud83d\udca1 محلول‌پاشی سولفات منیزیم (۱٪) انجام دهید.")
            elif 'N:K' in alert:
                recs.append("\ud83d\udca1 نسبت N:K را با افزایش N یا کاهش K تنظیم کنید.")
            elif 'دما' in alert:
                recs.append("\ud83d\udca1 آبیاری را ۱۰-۱۵٪ افزایش دهید.")

        if data.get('weather') == 'cloudy':
            recs.append("\ud83d\udca1 هوای ابری است. کوددهی N را ۱۵٪ کاهش دهید.")

        if not recs:
            recs.append("\u2705 همه چیز در وضعیت مطلوب است. ادامه دهید.")

        return list(set(recs))

    def determine_health_status(self, alerts):
        if len(alerts) == 0:
            return 'Excellent'
        elif len(alerts) <= 2:
            return 'Good'
        elif len(alerts) <= 4:
            return 'Needs Attention'
        else:
            return 'Critical'
