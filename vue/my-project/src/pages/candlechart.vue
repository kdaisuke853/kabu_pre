<template>
<div class="container">
  <div>
    <apexchart width='100%' type="candlestick" :options="chartOptions" :series="series"></apexchart>
  </div>
</div>
</template>

<script>
//import ApexCharts from 'apexcharts'
export default {
  data: function() {
    var datas = JSON.parse(localStorage.getItem('datalist'));
    return {
      chartOptions: {
        title: {
          text: datas.name+'の株価',
          align: 'center'
        },
        xaxis: {
          type: 'datetime'
        },
        yaxis: {
          tooltip: {
            enabled: true
          }
        }
      },

      series: [{
        data:[
            {
 "x":  datas.Date[0],
 "y": [datas.Open[0], datas.High[0], datas.Low[0], datas.Close[0]]
},
{
 "x":  datas.Date[1],
 "y": [datas.Open[1], datas.High[1], datas.Low[1], datas.Close[1]]
},
{
 "x":  datas.Date[2],
 "y": [datas.Open[2], datas.High[2], datas.Low[2], datas.Close[2]]
},
{
 "x":  datas.Date[3],
 "y": [datas.Open[3], datas.High[3], datas.Low[3], datas.Close[3]]
},
{
 "x":  datas.Date[4],
 "y": [datas.Open[4], datas.High[4], datas.Low[4], datas.Close[4]]
},
{
 "x":  datas.Date[5],
 "y": [datas.Open[5], datas.High[5], datas.Low[5], datas.Close[5]]
},
{
 "x":  datas.Date[6],
 "y": [datas.Open[6], datas.High[6], datas.Low[6], datas.Close[6]]
},
{
 "x":  datas.Date[7],
 "y": [datas.Open[7], datas.High[7], datas.Low[7], datas.Close[7]]
},
{
 "x":  datas.Date[8],
 "y": [datas.Open[8], datas.High[8], datas.Low[8], datas.Close[8]]
},
{
 "x":  datas.Date[9],
 "y": [datas.Open[9], datas.High[9], datas.Low[9], datas.Close[9]]
},
{
 "x":  datas.Date[10],
 "y": [datas.Open[10], datas.High[10], datas.Low[10], datas.Close[10]]
},
{
 "x":  datas.Date[11],
 "y": [datas.Open[11], datas.High[11], datas.Low[11], datas.Close[11]]
},
{
 "x":  datas.Date[12],
 "y": [datas.Open[12], datas.High[12], datas.Low[12], datas.Close[12]]
},
{
 "x":  datas.Date[13],
 "y": [datas.Open[13], datas.High[13], datas.Low[13], datas.Close[13]]
},
{
 "x":  datas.Date[14],
 "y": [datas.Open[14], datas.High[14], datas.Low[14], datas.Close[14]]
},
{
 "x":  datas.Date[15],
 "y": [datas.Open[15], datas.High[15], datas.Low[15], datas.Close[15]]
},
{
 "x":  datas.Date[16],
 "y": [datas.Open[16], datas.High[16], datas.Low[16], datas.Close[16]]
},
{
 "x":  datas.Date[17],
 "y": [datas.Open[17], datas.High[17], datas.Low[17], datas.Close[17]]
},
{
 "x":  datas.Date[18],
 "y": [datas.Open[18], datas.High[18], datas.Low[18], datas.Close[18]]
},
{
 "x":  datas.Date[19],
 "y": [datas.Open[19], datas.High[19], datas.Low[19], datas.Close[19]]
},
{
 "x":  datas.Date[20],
 "y": [datas.Open[20], datas.High[20], datas.Low[20], datas.Close[20]]
},
{
 "x":  datas.Date[21],
 "y": [datas.Open[21], datas.High[21], datas.Low[21], datas.Close[21]]
},
{
 "x":  datas.Date[22],
 "y": [datas.Open[22], datas.High[22], datas.Low[22], datas.Close[22]]
},
{
 "x":  datas.Date[23],
 "y": [datas.Open[23], datas.High[23], datas.Low[23], datas.Close[23]]
},
{
 "x":  datas.Date[24],
 "y": [datas.Open[24], datas.High[24], datas.Low[24], datas.Close[24]]
},
{
 "x":  datas.Date[25],
 "y": [datas.Open[25], datas.High[25], datas.Low[25], datas.Close[25]]
},
{
 "x":  datas.Date[26],
 "y": [datas.Open[26], datas.High[26], datas.Low[26], datas.Close[26]]
},
{
 "x":  datas.Date[27],
 "y": [datas.Open[27], datas.High[27], datas.Low[27], datas.Close[27]]
},
{
 "x":  datas.Date[28],
 "y": [datas.Open[28], datas.High[28], datas.Low[28], datas.Close[28]]
},
{
 "x":  datas.Date[29],
 "y": [datas.Open[29], datas.High[29], datas.Low[29], datas.Close[29]]
},
{
 "x":  datas.Date[30],
 "y": [datas.Open[30], datas.High[30], datas.Low[30], datas.Close[30]]
},
{
 "x":  datas.Date[31],
 "y": [datas.Open[31], datas.High[31], datas.Low[31], datas.Close[31]]
},
{
 "x":  datas.Date[32],
 "y": [datas.Open[32], datas.High[32], datas.Low[32], datas.Close[32]]
},
{
 "x":  datas.Date[33],
 "y": [datas.Open[33], datas.High[33], datas.Low[33], datas.Close[33]]
},
{
 "x":  datas.Date[34],
 "y": [datas.Open[34], datas.High[34], datas.Low[34], datas.Close[34]]
},
{
 "x":  datas.Date[35],
 "y": [datas.Open[35], datas.High[35], datas.Low[35], datas.Close[35]]
},
{
 "x":  datas.Date[36],
 "y": [datas.Open[36], datas.High[36], datas.Low[36], datas.Close[36]]
},
{
 "x":  datas.Date[37],
 "y": [datas.Open[37], datas.High[37], datas.Low[37], datas.Close[37]]
},
{
 "x":  datas.Date[38],
 "y": [datas.Open[38], datas.High[38], datas.Low[38], datas.Close[38]]
},
{
 "x":  datas.Date[39],
 "y": [datas.Open[39], datas.High[39], datas.Low[39], datas.Close[39]]
},
{
 "x":  datas.Date[40],
 "y": [datas.Open[40], datas.High[40], datas.Low[40], datas.Close[40]]
},
{
 "x":  datas.Date[41],
 "y": [datas.Open[41], datas.High[41], datas.Low[41], datas.Close[41]]
},
{
 "x":  datas.Date[42],
 "y": [datas.Open[42], datas.High[42], datas.Low[42], datas.Close[42]]
},
{
 "x":  datas.Date[43],
 "y": [datas.Open[43], datas.High[43], datas.Low[43], datas.Close[43]]
},
{
 "x":  datas.Date[44],
 "y": [datas.Open[44], datas.High[44], datas.Low[44], datas.Close[44]]
},
{
 "x":  datas.Date[45],
 "y": [datas.Open[45], datas.High[45], datas.Low[45], datas.Close[45]]
},
{
 "x":  datas.Date[46],
 "y": [datas.Open[46], datas.High[46], datas.Low[46], datas.Close[46]]
},
{
 "x":  datas.Date[47],
 "y": [datas.Open[47], datas.High[47], datas.Low[47], datas.Close[47]]
},
{
 "x":  datas.Date[48],
 "y": [datas.Open[48], datas.High[48], datas.Low[48], datas.Close[48]]
},
{
 "x":  datas.Date[49],
 "y": [datas.Open[49], datas.High[49], datas.Low[49], datas.Close[49]]
},
{
 "x":  datas.Date[50],
 "y": [datas.Open[50], datas.High[50], datas.Low[50], datas.Close[50]]
},
{
 "x":  datas.Date[51],
 "y": [datas.Open[51], datas.High[51], datas.Low[51], datas.Close[51]]
},
{
 "x":  datas.Date[52],
 "y": [datas.Open[52], datas.High[52], datas.Low[52], datas.Close[52]]
},
{
 "x":  datas.Date[53],
 "y": [datas.Open[53], datas.High[53], datas.Low[53], datas.Close[53]]
},
{
 "x":  datas.Date[54],
 "y": [datas.Open[54], datas.High[54], datas.Low[54], datas.Close[54]]
},
{
 "x":  datas.Date[55],
 "y": [datas.Open[55], datas.High[55], datas.Low[55], datas.Close[55]]
},
{
 "x":  datas.Date[56],
 "y": [datas.Open[56], datas.High[56], datas.Low[56], datas.Close[56]]
},
{
 "x":  datas.Date[57],
 "y": [datas.Open[57], datas.High[57], datas.Low[57], datas.Close[57]]
},
{
 "x":  datas.Date[58],
 "y": [datas.Open[58], datas.High[58], datas.Low[58], datas.Close[58]]
},
{
 "x":  datas.Date[59],
 "y": [datas.Open[59], datas.High[59], datas.Low[59], datas.Close[59]]
},
{
 "x":  datas.Date[60],
 "y": [datas.Open[60], datas.High[60], datas.Low[60], datas.Close[60]]
},
{
 "x":  datas.Date[61],
 "y": [datas.Open[61], datas.High[61], datas.Low[61], datas.Close[61]]
},
{
 "x":  datas.Date[62],
 "y": [datas.Open[62], datas.High[62], datas.Low[62], datas.Close[62]]
},
{
 "x":  datas.Date[63],
 "y": [datas.Open[63], datas.High[63], datas.Low[63], datas.Close[63]]
},
{
 "x":  datas.Date[64],
 "y": [datas.Open[64], datas.High[64], datas.Low[64], datas.Close[64]]
},
{
 "x":  datas.Date[65],
 "y": [datas.Open[65], datas.High[65], datas.Low[65], datas.Close[65]]
},
{
 "x":  datas.Date[66],
 "y": [datas.Open[66], datas.High[66], datas.Low[66], datas.Close[66]]
},
{
 "x":  datas.Date[67],
 "y": [datas.Open[67], datas.High[67], datas.Low[67], datas.Close[67]]
},
{
 "x":  datas.Date[68],
 "y": [datas.Open[68], datas.High[68], datas.Low[68], datas.Close[68]]
},
{
 "x":  datas.Date[69],
 "y": [datas.Open[69], datas.High[69], datas.Low[69], datas.Close[69]]
},
{
 "x":  datas.Date[70],
 "y": [datas.Open[70], datas.High[70], datas.Low[70], datas.Close[70]]
},
{
 "x":  datas.Date[71],
 "y": [datas.Open[71], datas.High[71], datas.Low[71], datas.Close[71]]
},
{
 "x":  datas.Date[72],
 "y": [datas.Open[72], datas.High[72], datas.Low[72], datas.Close[72]]
},
{
 "x":  datas.Date[73],
 "y": [datas.Open[73], datas.High[73], datas.Low[73], datas.Close[73]]
},
{
 "x":  datas.Date[74],
 "y": [datas.Open[74], datas.High[74], datas.Low[74], datas.Close[74]]
},
{
 "x":  datas.Date[75],
 "y": [datas.Open[75], datas.High[75], datas.Low[75], datas.Close[75]]
},
{
 "x":  datas.Date[76],
 "y": [datas.Open[76], datas.High[76], datas.Low[76], datas.Close[76]]
},
{
 "x":  datas.Date[77],
 "y": [datas.Open[77], datas.High[77], datas.Low[77], datas.Close[77]]
},
{
 "x":  datas.Date[78],
 "y": [datas.Open[78], datas.High[78], datas.Low[78], datas.Close[78]]
},
{
 "x":  datas.Date[79],
 "y": [datas.Open[79], datas.High[79], datas.Low[79], datas.Close[79]]
},
{
 "x":  datas.Date[80],
 "y": [datas.Open[80], datas.High[80], datas.Low[80], datas.Close[80]]
},
{
 "x":  datas.Date[81],
 "y": [datas.Open[81], datas.High[81], datas.Low[81], datas.Close[81]]
},
{
 "x":  datas.Date[82],
 "y": [datas.Open[82], datas.High[82], datas.Low[82], datas.Close[82]]
},
{
 "x":  datas.Date[83],
 "y": [datas.Open[83], datas.High[83], datas.Low[83], datas.Close[83]]
},
{
 "x":  datas.Date[84],
 "y": [datas.Open[84], datas.High[84], datas.Low[84], datas.Close[84]]
},
{
 "x":  datas.Date[85],
 "y": [datas.Open[85], datas.High[85], datas.Low[85], datas.Close[85]]
},
{
 "x":  datas.Date[86],
 "y": [datas.Open[86], datas.High[86], datas.Low[86], datas.Close[86]]
},
{
 "x":  datas.Date[87],
 "y": [datas.Open[87], datas.High[87], datas.Low[87], datas.Close[87]]
},
{
 "x":  datas.Date[88],
 "y": [datas.Open[88], datas.High[88], datas.Low[88], datas.Close[88]]
},
{
 "x":  datas.Date[89],
 "y": [datas.Open[89], datas.High[89], datas.Low[89], datas.Close[89]]
},
{
 "x":  datas.Date[90],
 "y": [datas.Open[90], datas.High[90], datas.Low[90], datas.Close[90]]
},
{
 "x":  datas.Date[91],
 "y": [datas.Open[91], datas.High[91], datas.Low[91], datas.Close[91]]
},
{
 "x":  datas.Date[92],
 "y": [datas.Open[92], datas.High[92], datas.Low[92], datas.Close[92]]
},
{
 "x":  datas.Date[93],
 "y": [datas.Open[93], datas.High[93], datas.Low[93], datas.Close[93]]
},
{
 "x":  datas.Date[94],
 "y": [datas.Open[94], datas.High[94], datas.Low[94], datas.Close[94]]
},
{
 "x":  datas.Date[95],
 "y": [datas.Open[95], datas.High[95], datas.Low[95], datas.Close[95]]
},
{
 "x":  datas.Date[96],
 "y": [datas.Open[96], datas.High[96], datas.Low[96], datas.Close[96]]
},
{
 "x":  datas.Date[97],
 "y": [datas.Open[97], datas.High[97], datas.Low[97], datas.Close[97]]
},
{
 "x":  datas.Date[98],
 "y": [datas.Open[98], datas.High[98], datas.Low[98], datas.Close[98]]
},
{
 "x":  datas.Date[99],
 "y": [datas.Open[99], datas.High[99], datas.Low[99], datas.Close[99]]
},
{
 "x":  datas.Date[100],
 "y": [datas.Open[100], datas.High[100], datas.Low[100], datas.Close[100]]
},
{
 "x":  datas.Date[101],
 "y": [datas.Open[101], datas.High[101], datas.Low[101], datas.Close[101]]
},
{
 "x":  datas.Date[102],
 "y": [datas.Open[102], datas.High[102], datas.Low[102], datas.Close[102]]
},
{
 "x":  datas.Date[103],
 "y": [datas.Open[103], datas.High[103], datas.Low[103], datas.Close[103]]
},
{
 "x":  datas.Date[104],
 "y": [datas.Open[104], datas.High[104], datas.Low[104], datas.Close[104]]
},
{
 "x":  datas.Date[105],
 "y": [datas.Open[105], datas.High[105], datas.Low[105], datas.Close[105]]
},
{
 "x":  datas.Date[106],
 "y": [datas.Open[106], datas.High[106], datas.Low[106], datas.Close[106]]
},
{
 "x":  datas.Date[107],
 "y": [datas.Open[107], datas.High[107], datas.Low[107], datas.Close[107]]
},
{
 "x":  datas.Date[108],
 "y": [datas.Open[108], datas.High[108], datas.Low[108], datas.Close[108]]
},
{
 "x":  datas.Date[109],
 "y": [datas.Open[109], datas.High[109], datas.Low[109], datas.Close[109]]
},
{
 "x":  datas.Date[110],
 "y": [datas.Open[110], datas.High[110], datas.Low[110], datas.Close[110]]
},
{
 "x":  datas.Date[111],
 "y": [datas.Open[111], datas.High[111], datas.Low[111], datas.Close[111]]
},
{
 "x":  datas.Date[112],
 "y": [datas.Open[112], datas.High[112], datas.Low[112], datas.Close[112]]
},
{
 "x":  datas.Date[113],
 "y": [datas.Open[113], datas.High[113], datas.Low[113], datas.Close[113]]
},
{
 "x":  datas.Date[114],
 "y": [datas.Open[114], datas.High[114], datas.Low[114], datas.Close[114]]
},
{
 "x":  datas.Date[115],
 "y": [datas.Open[115], datas.High[115], datas.Low[115], datas.Close[115]]
},
{
 "x":  datas.Date[116],
 "y": [datas.Open[116], datas.High[116], datas.Low[116], datas.Close[116]]
},
{
 "x":  datas.Date[117],
 "y": [datas.Open[117], datas.High[117], datas.Low[117], datas.Close[117]]
},
{
 "x":  datas.Date[118],
 "y": [datas.Open[118], datas.High[118], datas.Low[118], datas.Close[118]]
},
{
 "x":  datas.Date[119],
 "y": [datas.Open[119], datas.High[119], datas.Low[119], datas.Close[119]]
},
{
 "x":  datas.Date[120],
 "y": [datas.Open[120], datas.High[120], datas.Low[120], datas.Close[120]]
},
{
 "x":  datas.Date[121],
 "y": [datas.Open[121], datas.High[121], datas.Low[121], datas.Close[121]]
},
{
 "x":  datas.Date[122],
 "y": [datas.Open[122], datas.High[122], datas.Low[122], datas.Close[122]]
},
{
 "x":  datas.Date[123],
 "y": [datas.Open[123], datas.High[123], datas.Low[123], datas.Close[123]]
},
{
 "x":  datas.Date[124],
 "y": [datas.Open[124], datas.High[124], datas.Low[124], datas.Close[124]]
},
{
 "x":  datas.Date[125],
 "y": [datas.Open[125], datas.High[125], datas.Low[125], datas.Close[125]]
},
{
 "x":  datas.Date[126],
 "y": [datas.Open[126], datas.High[126], datas.Low[126], datas.Close[126]]
},
{
 "x":  datas.Date[127],
 "y": [datas.Open[127], datas.High[127], datas.Low[127], datas.Close[127]]
},
{
 "x":  datas.Date[128],
 "y": [datas.Open[128], datas.High[128], datas.Low[128], datas.Close[128]]
},
{
 "x":  datas.Date[129],
 "y": [datas.Open[129], datas.High[129], datas.Low[129], datas.Close[129]]
},
{
 "x":  datas.Date[130],
 "y": [datas.Open[130], datas.High[130], datas.Low[130], datas.Close[130]]
},
{
 "x":  datas.Date[131],
 "y": [datas.Open[131], datas.High[131], datas.Low[131], datas.Close[131]]
},
{
 "x":  datas.Date[132],
 "y": [datas.Open[132], datas.High[132], datas.Low[132], datas.Close[132]]
},
{
 "x":  datas.Date[133],
 "y": [datas.Open[133], datas.High[133], datas.Low[133], datas.Close[133]]
},
{
 "x":  datas.Date[134],
 "y": [datas.Open[134], datas.High[134], datas.Low[134], datas.Close[134]]
},
{
 "x":  datas.Date[135],
 "y": [datas.Open[135], datas.High[135], datas.Low[135], datas.Close[135]]
},
{
 "x":  datas.Date[136],
 "y": [datas.Open[136], datas.High[136], datas.Low[136], datas.Close[136]]
},
{
 "x":  datas.Date[137],
 "y": [datas.Open[137], datas.High[137], datas.Low[137], datas.Close[137]]
},
{
 "x":  datas.Date[138],
 "y": [datas.Open[138], datas.High[138], datas.Low[138], datas.Close[138]]
},
{
 "x":  datas.Date[139],
 "y": [datas.Open[139], datas.High[139], datas.Low[139], datas.Close[139]]
},
{
 "x":  datas.Date[140],
 "y": [datas.Open[140], datas.High[140], datas.Low[140], datas.Close[140]]
},
{
 "x":  datas.Date[141],
 "y": [datas.Open[141], datas.High[141], datas.Low[141], datas.Close[141]]
},
{
 "x":  datas.Date[142],
 "y": [datas.Open[142], datas.High[142], datas.Low[142], datas.Close[142]]
},
{
 "x":  datas.Date[143],
 "y": [datas.Open[143], datas.High[143], datas.Low[143], datas.Close[143]]
},
{
 "x":  datas.Date[144],
 "y": [datas.Open[144], datas.High[144], datas.Low[144], datas.Close[144]]
},
{
 "x":  datas.Date[145],
 "y": [datas.Open[145], datas.High[145], datas.Low[145], datas.Close[145]]
},
{
 "x":  datas.Date[146],
 "y": [datas.Open[146], datas.High[146], datas.Low[146], datas.Close[146]]
},
{
 "x":  datas.Date[147],
 "y": [datas.Open[147], datas.High[147], datas.Low[147], datas.Close[147]]
},
{
 "x":  datas.Date[148],
 "y": [datas.Open[148], datas.High[148], datas.Low[148], datas.Close[148]]
},
{
 "x":  datas.Date[149],
 "y": [datas.Open[149], datas.High[149], datas.Low[149], datas.Close[149]]
},
{
 "x":  datas.Date[150],
 "y": [datas.Open[150], datas.High[150], datas.Low[150], datas.Close[150]]
},
{
 "x":  datas.Date[151],
 "y": [datas.Open[151], datas.High[151], datas.Low[151], datas.Close[151]]
},
{
 "x":  datas.Date[152],
 "y": [datas.Open[152], datas.High[152], datas.Low[152], datas.Close[152]]
},
{
 "x":  datas.Date[153],
 "y": [datas.Open[153], datas.High[153], datas.Low[153], datas.Close[153]]
},
{
 "x":  datas.Date[154],
 "y": [datas.Open[154], datas.High[154], datas.Low[154], datas.Close[154]]
},
{
 "x":  datas.Date[155],
 "y": [datas.Open[155], datas.High[155], datas.Low[155], datas.Close[155]]
},
{
 "x":  datas.Date[156],
 "y": [datas.Open[156], datas.High[156], datas.Low[156], datas.Close[156]]
},
{
 "x":  datas.Date[157],
 "y": [datas.Open[157], datas.High[157], datas.Low[157], datas.Close[157]]
},
{
 "x":  datas.Date[158],
 "y": [datas.Open[158], datas.High[158], datas.Low[158], datas.Close[158]]
},
{
 "x":  datas.Date[159],
 "y": [datas.Open[159], datas.High[159], datas.Low[159], datas.Close[159]]
},
{
 "x":  datas.Date[160],
 "y": [datas.Open[160], datas.High[160], datas.Low[160], datas.Close[160]]
},
{
 "x":  datas.Date[161],
 "y": [datas.Open[161], datas.High[161], datas.Low[161], datas.Close[161]]
},
{
 "x":  datas.Date[162],
 "y": [datas.Open[162], datas.High[162], datas.Low[162], datas.Close[162]]
},
{
 "x":  datas.Date[163],
 "y": [datas.Open[163], datas.High[163], datas.Low[163], datas.Close[163]]
},
{
 "x":  datas.Date[164],
 "y": [datas.Open[164], datas.High[164], datas.Low[164], datas.Close[164]]
},
{
 "x":  datas.Date[165],
 "y": [datas.Open[165], datas.High[165], datas.Low[165], datas.Close[165]]
},
{
 "x":  datas.Date[166],
 "y": [datas.Open[166], datas.High[166], datas.Low[166], datas.Close[166]]
},
{
 "x":  datas.Date[167],
 "y": [datas.Open[167], datas.High[167], datas.Low[167], datas.Close[167]]
},
{
 "x":  datas.Date[168],
 "y": [datas.Open[168], datas.High[168], datas.Low[168], datas.Close[168]]
},
{
 "x":  datas.Date[169],
 "y": [datas.Open[169], datas.High[169], datas.Low[169], datas.Close[169]]
},
{
 "x":  datas.Date[170],
 "y": [datas.Open[170], datas.High[170], datas.Low[170], datas.Close[170]]
},
{
 "x":  datas.Date[171],
 "y": [datas.Open[171], datas.High[171], datas.Low[171], datas.Close[171]]
},
{
 "x":  datas.Date[172],
 "y": [datas.Open[172], datas.High[172], datas.Low[172], datas.Close[172]]
},
{
 "x":  datas.Date[173],
 "y": [datas.Open[173], datas.High[173], datas.Low[173], datas.Close[173]]
},
{
 "x":  datas.Date[174],
 "y": [datas.Open[174], datas.High[174], datas.Low[174], datas.Close[174]]
},
{
 "x":  datas.Date[175],
 "y": [datas.Open[175], datas.High[175], datas.Low[175], datas.Close[175]]
},
{
 "x":  datas.Date[176],
 "y": [datas.Open[176], datas.High[176], datas.Low[176], datas.Close[176]]
},
{
 "x":  datas.Date[177],
 "y": [datas.Open[177], datas.High[177], datas.Low[177], datas.Close[177]]
},
{
 "x":  datas.Date[178],
 "y": [datas.Open[178], datas.High[178], datas.Low[178], datas.Close[178]]
},
{
 "x":  datas.Date[179],
 "y": [datas.Open[179], datas.High[179], datas.Low[179], datas.Close[179]]
},
{
 "x":  datas.Date[180],
 "y": [datas.Open[180], datas.High[180], datas.Low[180], datas.Close[180]]
},
{
 "x":  datas.Date[181],
 "y": [datas.Open[181], datas.High[181], datas.Low[181], datas.Close[181]]
},
{
 "x":  datas.Date[182],
 "y": [datas.Open[182], datas.High[182], datas.Low[182], datas.Close[182]]
},
{
 "x":  datas.Date[183],
 "y": [datas.Open[183], datas.High[183], datas.Low[183], datas.Close[183]]
},
{
 "x":  datas.Date[184],
 "y": [datas.Open[184], datas.High[184], datas.Low[184], datas.Close[184]]
},
{
 "x":  datas.Date[185],
 "y": [datas.Open[185], datas.High[185], datas.Low[185], datas.Close[185]]
},
{
 "x":  datas.Date[186],
 "y": [datas.Open[186], datas.High[186], datas.Low[186], datas.Close[186]]
},
{
 "x":  datas.Date[187],
 "y": [datas.Open[187], datas.High[187], datas.Low[187], datas.Close[187]]
},
{
 "x":  datas.Date[188],
 "y": [datas.Open[188], datas.High[188], datas.Low[188], datas.Close[188]]
},
{
 "x":  datas.Date[189],
 "y": [datas.Open[189], datas.High[189], datas.Low[189], datas.Close[189]]
},
{
 "x":  datas.Date[190],
 "y": [datas.Open[190], datas.High[190], datas.Low[190], datas.Close[190]]
},
{
 "x":  datas.Date[191],
 "y": [datas.Open[191], datas.High[191], datas.Low[191], datas.Close[191]]
},
{
 "x":  datas.Date[192],
 "y": [datas.Open[192], datas.High[192], datas.Low[192], datas.Close[192]]
},
{
 "x":  datas.Date[193],
 "y": [datas.Open[193], datas.High[193], datas.Low[193], datas.Close[193]]
},
{
 "x":  datas.Date[194],
 "y": [datas.Open[194], datas.High[194], datas.Low[194], datas.Close[194]]
},
{
 "x":  datas.Date[195],
 "y": [datas.Open[195], datas.High[195], datas.Low[195], datas.Close[195]]
},
{
 "x":  datas.Date[196],
 "y": [datas.Open[196], datas.High[196], datas.Low[196], datas.Close[196]]
},
{
 "x":  datas.Date[197],
 "y": [datas.Open[197], datas.High[197], datas.Low[197], datas.Close[197]]
},
{
 "x":  datas.Date[198],
 "y": [datas.Open[198], datas.High[198], datas.Low[198], datas.Close[198]]
},
{
 "x":  datas.Date[199],
 "y": [datas.Open[199], datas.High[199], datas.Low[199], datas.Close[199]]
},
{
 "x":  datas.Date[200],
 "y": [datas.Open[200], datas.High[200], datas.Low[200], datas.Close[200]]
},
{
 "x":  datas.Date[201],
 "y": [datas.Open[201], datas.High[201], datas.Low[201], datas.Close[201]]
},
{
 "x":  datas.Date[202],
 "y": [datas.Open[202], datas.High[202], datas.Low[202], datas.Close[202]]
},
{
 "x":  datas.Date[203],
 "y": [datas.Open[203], datas.High[203], datas.Low[203], datas.Close[203]]
},
{
 "x":  datas.Date[204],
 "y": [datas.Open[204], datas.High[204], datas.Low[204], datas.Close[204]]
},
{
 "x":  datas.Date[205],
 "y": [datas.Open[205], datas.High[205], datas.Low[205], datas.Close[205]]
},
{
 "x":  datas.Date[206],
 "y": [datas.Open[206], datas.High[206], datas.Low[206], datas.Close[206]]
},
{
 "x":  datas.Date[207],
 "y": [datas.Open[207], datas.High[207], datas.Low[207], datas.Close[207]]
},
{
 "x":  datas.Date[208],
 "y": [datas.Open[208], datas.High[208], datas.Low[208], datas.Close[208]]
},
{
 "x":  datas.Date[209],
 "y": [datas.Open[209], datas.High[209], datas.Low[209], datas.Close[209]]
},
{
 "x":  datas.Date[210],
 "y": [datas.Open[210], datas.High[210], datas.Low[210], datas.Close[210]]
},
{
 "x":  datas.Date[211],
 "y": [datas.Open[211], datas.High[211], datas.Low[211], datas.Close[211]]
},
{
 "x":  datas.Date[212],
 "y": [datas.Open[212], datas.High[212], datas.Low[212], datas.Close[212]]
},
{
 "x":  datas.Date[213],
 "y": [datas.Open[213], datas.High[213], datas.Low[213], datas.Close[213]]
},
{
 "x":  datas.Date[214],
 "y": [datas.Open[214], datas.High[214], datas.Low[214], datas.Close[214]]
},
{
 "x":  datas.Date[215],
 "y": [datas.Open[215], datas.High[215], datas.Low[215], datas.Close[215]]
},
{
 "x":  datas.Date[216],
 "y": [datas.Open[216], datas.High[216], datas.Low[216], datas.Close[216]]
},
{
 "x":  datas.Date[217],
 "y": [datas.Open[217], datas.High[217], datas.Low[217], datas.Close[217]]
},
{
 "x":  datas.Date[218],
 "y": [datas.Open[218], datas.High[218], datas.Low[218], datas.Close[218]]
},
{
 "x":  datas.Date[219],
 "y": [datas.Open[219], datas.High[219], datas.Low[219], datas.Close[219]]
},
{
 "x":  datas.Date[220],
 "y": [datas.Open[220], datas.High[220], datas.Low[220], datas.Close[220]]
},
{
 "x":  datas.Date[221],
 "y": [datas.Open[221], datas.High[221], datas.Low[221], datas.Close[221]]
},
{
 "x":  datas.Date[222],
 "y": [datas.Open[222], datas.High[222], datas.Low[222], datas.Close[222]]
},
{
 "x":  datas.Date[223],
 "y": [datas.Open[223], datas.High[223], datas.Low[223], datas.Close[223]]
},
{
 "x":  datas.Date[224],
 "y": [datas.Open[224], datas.High[224], datas.Low[224], datas.Close[224]]
},
{
 "x":  datas.Date[225],
 "y": [datas.Open[225], datas.High[225], datas.Low[225], datas.Close[225]]
},
{
 "x":  datas.Date[226],
 "y": [datas.Open[226], datas.High[226], datas.Low[226], datas.Close[226]]
},
{
 "x":  datas.Date[227],
 "y": [datas.Open[227], datas.High[227], datas.Low[227], datas.Close[227]]
},
{
 "x":  datas.Date[228],
 "y": [datas.Open[228], datas.High[228], datas.Low[228], datas.Close[228]]
},
{
 "x":  datas.Date[229],
 "y": [datas.Open[229], datas.High[229], datas.Low[229], datas.Close[229]]
},
{
 "x":  datas.Date[230],
 "y": [datas.Open[230], datas.High[230], datas.Low[230], datas.Close[230]]
},
{
 "x":  datas.Date[231],
 "y": [datas.Open[231], datas.High[231], datas.Low[231], datas.Close[231]]
},
{
 "x":  datas.Date[232],
 "y": [datas.Open[232], datas.High[232], datas.Low[232], datas.Close[232]]
},
{
 "x":  datas.Date[233],
 "y": [datas.Open[233], datas.High[233], datas.Low[233], datas.Close[233]]
},
{
 "x":  datas.Date[234],
 "y": [datas.Open[234], datas.High[234], datas.Low[234], datas.Close[234]]
},
{
 "x":  datas.Date[235],
 "y": [datas.Open[235], datas.High[235], datas.Low[235], datas.Close[235]]
},
{
 "x":  datas.Date[236],
 "y": [datas.Open[236], datas.High[236], datas.Low[236], datas.Close[236]]
},
{
 "x":  datas.Date[237],
 "y": [datas.Open[237], datas.High[237], datas.Low[237], datas.Close[237]]
},
{
 "x":  datas.Date[238],
 "y": [datas.Open[238], datas.High[238], datas.Low[238], datas.Close[238]]
},
{
 "x":  datas.Date[239],
 "y": [datas.Open[239], datas.High[239], datas.Low[239], datas.Close[239]]
},
{
 "x":  datas.Date[240],
 "y": [datas.Open[240], datas.High[240], datas.Low[240], datas.Close[240]]
},
{
 "x":  datas.Date[241],
 "y": [datas.Open[241], datas.High[241], datas.Low[241], datas.Close[241]]
},
{
 "x":  datas.Date[242],
 "y": [datas.Open[242], datas.High[242], datas.Low[242], datas.Close[242]]
},
{
 "x":  datas.Date[243],
 "y": [datas.Open[243], datas.High[243], datas.Low[243], datas.Close[243]]
},
{
 "x":  datas.Date[244],
 "y": [datas.Open[244], datas.High[244], datas.Low[244], datas.Close[244]]
},
        ]
      }],
    }
  },
};
</script>