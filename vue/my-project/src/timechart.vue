<script>
import {Line, mixins} from 'vue-chartjs'
//import chartjsPluginColorschemes from 'chartjs-plugin-colorschemes'

export default {
  name: 'LineChart',
  extends: Line,
  mixins: [mixins.reactiveData],
  props: {
    data: null,
    options: null
  },
  mounted () {
    this.chartData = this.data
  },
  watch: {
      data: function() {
        this.chartData = this.data
      }
    }
}
</script>

<style>

</style>