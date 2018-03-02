// Theme custom js methods
$(document).ready(function(){

  var addYearSelectorCustomLabels = function(){
    var str2017 = {
      'es': 'prorrogado',
    };

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var val = $(this).html();
      if (val === '2016' || val === '2017' || val === '2018'){
        $(this).html(val + '<br/><small><i> ('+ str2017[ $('html').attr('lang') ] +')</i></small>');
      }
    });
  };

  addYearSelectorCustomLabels();
});
