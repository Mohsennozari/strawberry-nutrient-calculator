# ============================================================
# 📚 منابع علمی اصلی
# ============================================================
# [1] Mashayekhi, K., et al. (2013). Hydroponic N, P, K study.
# [2] Bottoms, T.G., et al. (2013). DRIS California.
# [3] UF/IFAS Extension (2024). Petiole Sap Testing.
# [4] Yousefi, S., et al. (2023). K/N ratios on 'Camarosa'.
# [5] Frontiers in Plant Science (2024). SPT Phenotyping.
# [6] University of Delaware Extension. Sufficiency Ranges.
# [7] Gil-Marín, J.A., et al. (2025). EC levels on yield.
# [8] EFSA (2023). Iron concentration in hydroponics.
# [9] Ebrahimi, R., & Abadía, J. (2023). Iron in crops.
# ============================================================

class DataSources:
    """داده‌های پایه و منابع علمی سیستم"""

    def __init__(self):
        # PPM پایه برای ۱۳ عنصر بر اساس مرحله رشد + منبع علمی
        self.nutrient_sources = {
            'N': {
                'vegetative': {'value': 160, 'range': (156, 172), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'flowering': {'value': 150, 'range': (144, 158), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'fruiting': {'value': 165, 'range': (156, 172), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'maturity': {'value': 140, 'range': (130, 150), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'P': {
                'vegetative': {'value': 55, 'range': (54, 63), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'flowering': {'value': 58, 'range': (54, 63), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'fruiting': {'value': 58, 'range': (54, 63), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'maturity': {'value': 50, 'range': (48, 55), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'K': {
                'vegetative': {'value': 420, 'range': (400, 450), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'flowering': {'value': 470, 'range': (450, 500), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'fruiting': {'value': 480, 'range': (450, 510), 'source': 'DRIS + Mashayekhi 2013 [1, 2]'},
                'maturity': {'value': 420, 'range': (400, 450), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Ca': {
                'vegetative': {'value': 280, 'range': (244, 449), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'flowering': {'value': 320, 'range': (280, 449), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'fruiting': {'value': 340, 'range': (280, 449), 'source': 'Bottoms et al. 2013 (DRIS) [2]'},
                'maturity': {'value': 320, 'range': (280, 449), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Mg': {
                'vegetative': {'value': 60, 'range': (40, 70), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 65, 'range': (40, 70), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 70, 'range': (40, 70), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 60, 'range': (40, 70), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'S': {
                'vegetative': {'value': 45, 'range': (30, 60), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 50, 'range': (30, 60), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 55, 'range': (30, 60), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 45, 'range': (30, 60), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Fe': {
                'vegetative': {'value': 2.2, 'range': (1.5, 3.0), 'source': 'EFSA + Ebrahimi 2023 [8, 9]'},
                'flowering': {'value': 2.5, 'range': (1.5, 3.0), 'source': 'EFSA + Ebrahimi 2023 [8, 9]'},
                'fruiting': {'value': 2.8, 'range': (1.5, 3.0), 'source': 'EFSA + Ebrahimi 2023 [8, 9]'},
                'maturity': {'value': 2.0, 'range': (1.5, 3.0), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Zn': {
                'vegetative': {'value': 0.45, 'range': (0.3, 0.6), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 0.50, 'range': (0.3, 0.6), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 0.55, 'range': (0.3, 0.6), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 0.40, 'range': (0.3, 0.6), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Mn': {
                'vegetative': {'value': 0.75, 'range': (0.5, 1.0), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 0.85, 'range': (0.5, 1.0), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 0.90, 'range': (0.5, 1.0), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 0.70, 'range': (0.5, 1.0), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Cu': {
                'vegetative': {'value': 0.20, 'range': (0.1, 0.3), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 0.25, 'range': (0.1, 0.3), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 0.25, 'range': (0.1, 0.3), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 0.20, 'range': (0.1, 0.3), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'B': {
                'vegetative': {'value': 0.35, 'range': (0.2, 0.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 0.40, 'range': (0.2, 0.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 0.45, 'range': (0.2, 0.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 0.30, 'range': (0.2, 0.5), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Mo': {
                'vegetative': {'value': 0.03, 'range': (0.01, 0.05), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 0.04, 'range': (0.01, 0.05), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 0.04, 'range': (0.01, 0.05), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 0.03, 'range': (0.01, 0.05), 'source': 'UF/IFAS Extension 2024 [3]'}
            },
            'Cl': {
                'vegetative': {'value': 1.0, 'range': (0.5, 1.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'flowering': {'value': 1.2, 'range': (0.5, 1.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'fruiting': {'value': 1.3, 'range': (0.5, 1.5), 'source': 'UF/IFAS Extension 2024 [3]'},
                'maturity': {'value': 1.0, 'range': (0.5, 1.5), 'source': 'UF/IFAS Extension 2024 [3]'}
            }
        }

        # محدوده‌های بهینه برای ۱۳ عنصر
        self.optimal_ranges = {
            'N': {'min': 156, 'max': 172, 'source': 'Bottoms et al. 2013 [2]'},
            'P': {'min': 54, 'max': 63, 'source': 'Bottoms et al. 2013 [2]'},
            'K': {'min': 400, 'max': 543, 'source': 'Bottoms et al. 2013 [2]'},
            'Ca': {'min': 244, 'max': 449, 'source': 'Bottoms et al. 2013 [2]'},
            'Mg': {'min': 40, 'max': 70, 'source': 'UF/IFAS Extension 2024 [3]'},
            'S': {'min': 30, 'max': 60, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Fe': {'min': 1.5, 'max': 3.0, 'source': 'EFSA & Ebrahimi 2023 [8, 9]'},
            'Zn': {'min': 0.3, 'max': 0.6, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Mn': {'min': 0.5, 'max': 1.0, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Cu': {'min': 0.1, 'max': 0.3, 'source': 'UF/IFAS Extension 2024 [3]'},
            'B': {'min': 0.2, 'max': 0.5, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Mo': {'min': 0.01, 'max': 0.05, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Cl': {'min': 0.5, 'max': 1.5, 'source': 'UF/IFAS Extension 2024 [3]'}
        }

        # نسبت‌های کلیدی عناصر
        self.optimal_ratios = {
            'K_Ca': {'min': 1.2, 'max': 1.4, 'source': 'Yousefi et al. 2023 [4]'},
            'K_Mg': {'min': 3.0, 'max': 4.0, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Ca_Mg': {'min': 2.5, 'max': 3.5, 'source': 'UF/IFAS Extension 2024 [3]'},
            'N_K': {'min': 0.3, 'max': 0.4, 'source': 'Yousefi et al. 2023 [4]'},
            'K_S': {'min': 8.0, 'max': 10.0, 'source': 'UF/IFAS Extension 2024 [3]'},
            'Fe_Mn': {'min': 2.0, 'max': 3.0, 'source': 'EFSA 2023 [8]'},
            'B_Ca': {'min': 0.001, 'max': 0.002, 'source': 'UF/IFAS Extension 2024 [3]'}
        }

        # محدوده‌های مجاز EC و pH
        self.optimal_ec_ph = {
            'EC': {
                'min': 1.0, 'max': 2.5,
                'optimal_min': 1.5, 'optimal_max': 2.0,
                'source': 'Gil-Marín et al. 2025 [7]'
            },
            'pH': {
                'min': 5.5, 'max': 6.5,
                'optimal_min': 5.8, 'optimal_max': 6.2,
                'source': 'UF/IFAS Extension 2024 [3]'
            }
        }

        # پروفایل ارقام مختلف
        self.cultivar_profiles = {
            'Albion': {
                'source': 'Bottoms et al. 2013 (DRIS) [2]',
                'N': {'vegetative': 160, 'flowering': 150, 'fruiting': 165, 'maturity': 140},
                'K': {'vegetative': 420, 'flowering': 470, 'fruiting': 480, 'maturity': 420},
                'Ca': {'vegetative': 280, 'flowering': 320, 'fruiting': 340, 'maturity': 320},
                'Mg': {'vegetative': 60, 'flowering': 65, 'fruiting': 70, 'maturity': 60},
                'Fe': {'vegetative': 2.2, 'flowering': 2.5, 'fruiting': 2.8, 'maturity': 2.0}
            },
            'Camarosa': {
                'source': 'Yousefi et al. 2023 (K/N Ratio) [4]',
                'N': {'vegetative': 155, 'flowering': 145, 'fruiting': 158, 'maturity': 135},
                'K': {'vegetative': 400, 'flowering': 450, 'fruiting': 460, 'maturity': 400},
                'Ca': {'vegetative': 290, 'flowering': 310, 'fruiting': 330, 'maturity': 300},
                'Mg': {'vegetative': 58, 'flowering': 62, 'fruiting': 65, 'maturity': 55},
                'Fe': {'vegetative': 2.0, 'flowering': 2.3, 'fruiting': 2.6, 'maturity': 1.8}
            },
            'Sweet Charlie': {
                'source': 'Mashayekhi et al. 2013 (Hydroponic) [1]',
                'N': {'vegetative': 150, 'flowering': 140, 'fruiting': 155, 'maturity': 130},
                'K': {'vegetative': 390, 'flowering': 430, 'fruiting': 450, 'maturity': 390},
                'Ca': {'vegetative': 270, 'flowering': 300, 'fruiting': 320, 'maturity': 290},
                'Mg': {'vegetative': 55, 'flowering': 60, 'fruiting': 62, 'maturity': 52},
                'Fe': {'vegetative': 1.9, 'flowering': 2.2, 'fruiting': 2.5, 'maturity': 1.7}
            }
        }

    def get_ppm_with_source(self, element, stage):
        """دریافت ppm و منبع برای یک عنصر در مرحله مشخص"""
        if element in self.nutrient_sources:
            return self.nutrient_sources[element].get(stage, self.nutrient_sources[element]['vegetative'])
        return None

    def get_nutrient_sources(self, stage):
        """دریافت منابع علمی برای نمایش در خروجی"""
        sources = {}
        for element in self.nutrient_sources:
            source_data = self.get_ppm_with_source(element, stage)
            if source_data:
                sources[element] = {
                    'value': source_data['value'],
                    'range': source_data['range'],
                    'source': source_data['source']
                }
        return sources
