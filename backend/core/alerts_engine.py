class AlertsEngine:
    """تولید هشدارها و توصیه‌های عملی"""

    def __init__(self, data_sources):
        self.data = data_sources

    def generate_weighted_alerts(self, ppm, data, ratios):
        """تولید هشدارهای دسته‌بندی‌شده (بحرانی/ملایم/اطلاع‌رسانی)"""
        alerts = {'critical': [], 'warning': [], 'info': []}

        # ===== بحرانی (Critical) =====
        if ppm.get('N', 0) < 130:
            alerts['critical'].append({
                'level': 'critical',
                'message': f'کمبود شدید نیتروژن ({ppm["N"]} ppm) - رشد متوقف می‌شود',
                'element': 'N',
                'value': ppm['N'],
                'threshold': 130,
                'reference': 'Bottoms et al. 2013 [2]'
            })

        if ppm.get('K', 0) < 350:
            alerts['critical'].append({
                'level': 'critical',
                'message': f'کمبود شدید پتاسیم ({ppm["K"]} ppm) - میوه‌ها کوچک می‌شوند',
                'element': 'K',
                'value': ppm['K'],
                'threshold': 350,
                'reference': 'Mashayekhi et al. 2013 [1]'
            })

        if data.get('temp_c', 0) > 32:
            alerts['critical'].append({
                'level': 'critical',
                'message': f'دمای بالای ۳۲ درجه - خطر تنش گرمایی شدید',
                'element': 'temp',
                'value': data['temp_c'],
                'threshold': 32,
                'reference': 'UF/IFAS Extension 2024 [3]'
            })

        k_ca = ratios.get('K_Ca', 0)
        if k_ca > 1.6:
            alerts['critical'].append({
                'level': 'critical',
                'message': f'نسبت K:Ca = {k_ca:.2f} (بیش از حد) - خطر پوسیدگی نوک میوه',
                'element': 'K_Ca',
                'value': k_ca,
                'threshold': 1.6,
                'reference': 'Yousefi et al. 2023 [4]'
            })

        ec = data.get('ec', 1.8)
        ph = data.get('ph', 6.0)

        if ec > 2.5:
            alerts['critical'].append({
                'level': 'critical',
                'message': f'EC = {ec} dS/m (بیش از حد) - تنش اسمزی، جذب عناصر مختل می‌شود',
                'element': 'EC',
                'value': ec,
                'threshold': 2.5,
                'reference': 'Gil-Marín et al. 2025 [7]'
            })

        if ph > 6.5:
            alerts['warning'].append({
                'level': 'warning',
                'message': f'pH = {ph} (بالا) - آهن و منگنز رسوب می‌کنند، بررسی کنید',
                'element': 'pH',
                'value': ph,
                'threshold': 6.5,
                'reference': 'UF/IFAS Extension 2024 [3]'
            })

        # ===== هشدار (Warning) =====
        if ppm.get('K', 0) < 380:
            alerts['warning'].append({
                'level': 'warning',
                'message': f'پتاسیم نزدیک به حد پایین ({ppm["K"]} ppm) - بررسی کنید',
                'element': 'K',
                'value': ppm['K'],
                'threshold': 380,
                'reference': 'Bottoms et al. 2013 [2]'
            })

        if ppm.get('Ca', 0) < 250:
            alerts['warning'].append({
                'level': 'warning',
                'message': f'کلسیم نزدیک به حد پایین ({ppm["Ca"]} ppm) - بررسی کنید',
                'element': 'Ca',
                'value': ppm['Ca'],
                'threshold': 250,
                'reference': 'Bottoms et al. 2013 [2]'
            })

        if ppm.get('Mg', 0) < 45:
            alerts['warning'].append({
                'level': 'warning',
                'message': f'منیزیم نزدیک به حد پایین ({ppm["Mg"]} ppm) - بررسی کنید',
                'element': 'Mg',
                'value': ppm['Mg'],
                'threshold': 45,
                'reference': 'UF/IFAS Extension 2024 [3]'
            })

        if data.get('fruits_per_plant', 0) > 8:
            alerts['warning'].append({
                'level': 'warning',
                'message': f'تعداد میوه زیاد ({data["fruits_per_plant"]} عدد) - نیاز به K و Ca افزایش یافته',
                'element': 'fruits',
                'value': data['fruits_per_plant'],
                'threshold': 8,
                'reference': 'Mashayekhi et al. 2013 [1]'
            })

        # ===== اطلاع‌رسانی (Info) =====
        if ppm.get('Fe', 0) > 2.8:
            alerts['info'].append({
                'level': 'info',
                'message': f'آهن کمی بالا است ({ppm["Fe"]} ppm) - در صورت ادامه، کاهش دهید',
                'element': 'Fe',
                'value': ppm['Fe'],
                'threshold': 2.8,
                'reference': 'EFSA 2023 [8]'
            })

        if data.get('weather') == 'cloudy':
            alerts['info'].append({
                'level': 'info',
                'message': 'هوای ابری - فتوسنتز کاهش یافته، نیتروژن را ۱۵٪ کاهش دهید',
                'element': 'weather',
                'value': 'cloudy',
                'threshold': None,
                'reference': 'Bottoms et al. 2013 [2]'
            })

        return alerts

    def generate_precise_recommendations(self, ppm, ec, ph, alerts):
        """تولید توصیه‌های دقیق و عملی"""
        recommendations = []

        for alert in alerts.get('critical', []):
            if alert['element'] == 'N':
                recommendations.append({
                    'action': 'افزایش نیتروژن',
                    'detail': f'نیتروژن را از {ppm["N"]} به ۱۶۰ ppm برسانید',
                    'method': 'افزودن نیترات کلسیم به محلول (۰.۵ گرم در لیتر)',
                    'priority': 'high',
                    'reference': 'Bottoms et al. 2013 [2]'
                })
            elif alert['element'] == 'K':
                recommendations.append({
                    'action': 'افزایش پتاسیم',
                    'detail': f'پتاسیم را از {ppm["K"]} به ۴۸۰ ppm برسانید',
                    'method': 'افزودن سولفات پتاسیم به محلول (۰.۳ گرم در لیتر)',
                    'priority': 'high',
                    'reference': 'Mashayekhi et al. 2013 [1]'
                })
            elif alert['element'] == 'temp':
                recommendations.append({
                    'action': 'کاهش دما',
                    'detail': f'دما را از {alert["value"]} به ۲۵-۲۸ درجه کاهش دهید',
                    'method': 'افزایش تهویه و آبیاری ۲۰٪',
                    'priority': 'high',
                    'reference': 'UF/IFAS Extension 2024 [3]'
                })
            elif alert['element'] == 'K_Ca':
                recommendations.append({
                    'action': 'تنظیم نسبت K:Ca',
                    'detail': f'نسبت K:Ca را از {alert["value"]:.2f} به ۱.۲-۱.۴ برسانید',
                    'method': 'محلول‌پاشی نیترات کلسیم (۰.۳٪) یک بار در هفته',
                    'priority': 'high',
                    'reference': 'Yousefi et al. 2023 [4]'
                })
            elif alert['element'] == 'EC':
                recommendations.append({
                    'action': 'کاهش EC',
                    'detail': f'EC از {ec} به ۱.۸-۲.۰ کاهش یابد',
                    'method': 'آب خالص به نسبت ۱:۴ اضافه کنید',
                    'priority': 'high',
                    'reference': 'Gil-Marín et al. 2025 [7]'
                })

        for alert in alerts.get('warning', []):
            if alert['element'] == 'K':
                recommendations.append({
                    'action': 'بررسی پتاسیم',
                    'detail': f'پتاسیم نزدیک به حد پایین ({ppm["K"]} ppm)',
                    'method': 'هفته آینده مجدداً اندازه‌گیری کنید',
                    'priority': 'medium',
                    'reference': 'Bottoms et al. 2013 [2]'
                })
            elif alert['element'] == 'Ca':
                recommendations.append({
                    'action': 'بررسی کلسیم',
                    'detail': f'کلسیم نزدیک به حد پایین ({ppm["Ca"]} ppm)',
                    'method': 'محلول‌پاشی کلسیم (۰.۲٪) در صورت ادامه',
                    'priority': 'medium',
                    'reference': 'Bottoms et al. 2013 [2]'
                })
            elif alert['element'] == 'Mg':
                recommendations.append({
                    'action': 'بررسی منیزیم',
                    'detail': f'منیزیم نزدیک به حد پایین ({ppm["Mg"]} ppm)',
                    'method': 'محلول‌پاشی سولفات منیزیم (۱٪) در صورت ادامه',
                    'priority': 'medium',
                    'reference': 'UF/IFAS Extension 2024 [3]'
                })
            elif alert['element'] == 'pH':
                recommendations.append({
                    'action': 'کاهش pH',
                    'detail': f'pH از {ph} به ۵.۸-۶.۲ کاهش یابد',
                    'method': 'اسید فسفریک ۰.۱ میلی‌لیتر در لیتر اضافه کنید',
                    'priority': 'high',
                    'reference': 'UF/IFAS Extension 2024 [3]'
                })

        # ===== توصیه‌های EC و pH (اگر قبلاً اضافه نشده باشند) =====
        has_ec = any(r.get('action') in ['کاهش EC', 'افزایش EC'] for r in recommendations)
        has_ph = any(r.get('action') in ['کاهش pH', 'افزایش pH'] for r in recommendations)

        if ec > 2.5 and not has_ec:
            recommendations.append({
                'action': 'کاهش EC',
                'detail': f'EC از {ec} به ۱.۸-۲.۰ کاهش یابد',
                'method': 'آب خالص به نسبت ۱:۴ اضافه کنید',
                'priority': 'high',
                'reference': 'Gil-Marín et al. 2025 [7]'
            })
        elif ec < 1.0:
            recommendations.append({
                'action': 'افزایش EC',
                'detail': f'EC از {ec} به ۱.۸-۲.۰ افزایش یابد',
                'method': 'کوددهی را ۲۰٪ افزایش دهید',
                'priority': 'high',
                'reference': 'Gil-Marín et al. 2025 [7]'
            })

        if ph > 6.5 and not has_ph:
            recommendations.append({
                'action': 'کاهش pH',
                'detail': f'pH از {ph} به ۵.۸-۶.۲ کاهش یابد',
                'method': 'اسید فسفریک ۰.۱ میلی‌لیتر در لیتر اضافه کنید',
                'priority': 'high',
                'reference': 'UF/IFAS Extension 2024 [3]'
            })
        elif ph < 5.5:
            recommendations.append({
                'action': 'افزایش pH',
                'detail': f'pH از {ph} به ۵.۸-۶.۲ افزایش یابد',
                'method': 'پتاسیم هیدروکسید ۰.۱ میلی‌لیتر در لیتر اضافه کنید',
                'priority': 'high',
                'reference': 'UF/IFAS Extension 2024 [3]'
            })

        if not recommendations:
            recommendations.append({
                'action': 'وضعیت مطلوب',
                'detail': 'همه چیز در وضعیت ایده‌آل است',
                'method': 'برنامه فعلی را ادامه دهید',
                'priority': 'low',
                'reference': 'Bottoms et al. 2013 [2]'
            })

        return recommendations

    def determine_health_status(self, alerts):
        """تعیین وضعیت سلامت بر اساس وزن هشدارها"""
        critical_count = len(alerts.get('critical', []))
        warning_count = len(alerts.get('warning', []))

        if critical_count == 0 and warning_count == 0:
            return 'Excellent'
        elif critical_count == 0 and warning_count <= 2:
            return 'Good'
        elif critical_count == 0 and warning_count > 2:
            return 'Needs Attention'
        elif critical_count <= 2:
            return 'Attention Required'
        else:
            return 'Critical'
