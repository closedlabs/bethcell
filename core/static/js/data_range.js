  $('input[name="date_ranger"]').daterangepicker({
    "timePicker": false,
    "startDate": moment(),
    "endDate": moment(),
    "ranges": {
        'Hoje': [moment(), moment()],
        'Ontem': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
        'Ultimos 7 Dias': [moment().subtract(6, 'days'), moment()],
        'Ultimos 30 Dias': [moment().subtract(29, 'days'), moment()],
        'Esse Mês': [moment().startOf('month'), moment().endOf('month')],
        'Último Mês': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
     showDropdowns: true,
    "locale": {
    "format": "DD/MM/YYYY",
    "separator": " / ",
    "applyLabel": "Aplicar",
    "cancelLabel": "Cancelar",
    "fromLabel": "De",
    "toLabel": "Até",
    "customRangeLabel": "Customizado",
    "daysOfWeek": [
        "Dom",
        "Seg",
        "Ter",
        "Qua",
        "Qui",
        "Sex",
        "Sáb"
    ],
    "monthNames": [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
    ],
    "firstDay": 0
  }
}, function(start, end, label) {
  console.log("New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')");

});
