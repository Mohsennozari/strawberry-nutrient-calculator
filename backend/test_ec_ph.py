from physiology_engine import PhysiologyEngine

def test_full_system():
    engine = PhysiologyEngine()

    print("=" * 60)
    print("🧪 تست کامل سیستم با اصلاحات")
    print("=" * 60)

    # داده‌های پایه (مرحله باردهی)
    base_data = {
        'crown_diameter': 15,
        'plant_height': 25,
        'petiole_length': 15,
        'leaf_length': 7,
        'leaf_width': 5.5,
        'fruit_size': 6,
        'age_days': 60,
        'fruits_per_plant': 6,
        'temp_c': 25,
        'weather': 'sunny',
        'cultivar': 'Albion'
    }

    # ===== تست ۱: شرایط بهینه =====
    data_optimal = base_data.copy()
    data_optimal['ec'] = 1.8
    data_optimal['ph'] = 6.0

    result = engine.calculate(data_optimal)
    print("\n✅ شرایط بهینه (EC=1.8, pH=6.0):")
    print(f"   مرحله رشد: {result['stage']}")
    print(f"   N: {result['ppm']['N']} (انتظار: ۱۶۵)")
    print(f"   K: {result['ppm']['K']} (انتظار: ۴۸۰)")
    print(f"   Fe: {result['ppm']['Fe']} (انتظار: ۲.۸)")
    print(f"   وضعیت سلامت: {result['health_status']}")
    print(f"   تعداد هشدارها: {len(result['alerts']['critical'])} بحرانی, {len(result['alerts']['warning'])} هشدار")

    # ===== تست ۲: pH بالا =====
    data_high_ph = base_data.copy()
    data_high_ph['ec'] = 1.8
    data_high_ph['ph'] = 6.8

    result = engine.calculate(data_high_ph)
    print("\n🟡 pH بالا (6.8):")
    print(f"   Fe: {result['ppm']['Fe']} (انتظار: > 3.6) ← افزایش یافته")
    print(f"   Mn: {result['ppm']['Mn']} (انتظار: > 1.1) ← افزایش یافته")
    print(f"   Ca: {result['ppm']['Ca']} (انتظار: ~۳۴۰) ← تغییر نکرده")

    # ===== تست ۳: EC بالا =====
    data_high_ec = base_data.copy()
    data_high_ec['ec'] = 2.8
    data_high_ec['ph'] = 6.0

    result = engine.calculate(data_high_ec)
    print("\n🟠 EC بالا (2.8):")
    print(f"   N: {result['ppm']['N']} (انتظار: ~۱۷۸) ← افزایش یافته")
    print(f"   K: {result['ppm']['K']} (انتظار: ~۵۱۸) ← افزایش یافته")
    print(f"   Ca: {result['ppm']['Ca']} (انتظار: ~۳۶۷) ← افزایش یافته")

    # ===== تست ۴: هر دو مشکل =====
    data_both = base_data.copy()
    data_both['ec'] = 2.8
    data_both['ph'] = 6.8

    result = engine.calculate(data_both)
    print("\n🔴 EC بالا + pH بالا:")
    print(f"   Fe: {result['ppm']['Fe']} (انتظار: > 3.8) ← افزایش دوگانه")
    print(f"   N: {result['ppm']['N']} (انتظار: ~۱۷۸) ← افزایش از EC")
    print(f"   وضعیت سلامت: {result['health_status']}")

    # ===== تست ۵: اعتبارسنجی ورودی =====
    invalid_data = base_data.copy()
    invalid_data['crown_diameter'] = -5
    invalid_data['age_days'] = 10000
    invalid_data['weather'] = 'rainy'

    result = engine.calculate(invalid_data)
    if 'errors' in result:
        print("\n❌ اعتبارسنجی ورودی:")
        for error in result['errors']:
            print(f"   - {error}")

    # ===== تست ۶: منابع علمی =====
    result = engine.calculate(data_optimal)
    print("\n📚 منابع علمی:")
    for element, source in result.get('nutrient_sources', {}).items():
        print(f"   {element}: {source['value']} ppm از {source['source']}")

    print("\n" + "=" * 60)
    print("✅ تست کامل شد!")

if __name__ == '__main__':
    test_full_system()
