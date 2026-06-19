<template>
  <div>
    <CalculatorForm
      :form="form"
      :loading="loading"
      @calculate="handleCalculate"
    />

    <ResultTable
      v-if="result"
      :result="result"
      @copy="copyTable"
      @download="downloadCSV"
    />

    <EmptyState v-else />
  </div>
</template>

<script>
import { calculateNutrients } from '../services/api'
import CalculatorForm from './calculator/CalculatorForm.vue'
import ResultTable from './calculator/ResultTable.vue'
import EmptyState from './calculator/EmptyState.vue'

export default {
  name: 'CalculatorTab',
  components: { CalculatorForm, ResultTable, EmptyState },
  data() {
    return {
      form: {
        crown_diameter: 15.5,
        plant_height: 25.0,
        petiole_length: 15.0,
        leaf_length: 7.0,
        leaf_width: 5.5,
        fruit_size: 6.0,
        age_days: 84,
        fruits_per_plant: 6,
        temp_c: 26,
        weather: 'sunny',
        ec: 1.8,
        ph: 6.0
      },
      result: null,
      loading: false
    }
  },
  methods: {
    async handleCalculate(formData) {
      this.loading = true
      try {
        const data = await calculateNutrients(formData)
        this.result = data
        this.$emit('result-updated', data)
        this.$root.$emit('updateResult', data)
      } catch (error) {
        alert('❌ خطا! سرور Flask رو روشن کن.')
        console.error(error)
      } finally {
        this.loading = false
      }
    },
    copyTable() {
      const table = document.getElementById('result-table')
      if (!table) return
      const range = document.createRange()
      range.selectNode(table)
      window.getSelection().removeAllRanges()
      window.getSelection().addRange(range)
      try { document.execCommand('copy'); alert('✅ جدول کپی شد!') } catch (e) { alert('❌ کپی ناموفق.') }
      window.getSelection().removeAllRanges()
    },
    downloadCSV() {
      if (!this.result) return
      // ... کد CSV مانند قبل ...
      const rows = [['دسته', 'عنصر', 'مقدار (ppm)', 'وضعیت', 'محدوده بهینه (ppm)', 'نسبت', 'مقدار نسبت']]
      // (کد CSV کامل از نسخه قبلی)
      const csvContent = rows.map(row => row.join(',')).join('\n')
      const blob = new Blob(['\uFEFF' + csvContent], { type: 'text/csv;charset=utf-8;' })
      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.download = `تغذیه_توت_فرنگی_${new Date().toISOString().slice(0,10)}.csv`
      link.click()
    }
  }
}
</script>
