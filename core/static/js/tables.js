$(document).ready(function() {
    $('#datatables').DataTable({
        "pagingType": "full_numbers",
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        responsive: true,
        searching: false, 
        paginate: false,
        info: false,
        "language": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   " _MENU_ ",
          "sZeroRecords":  "<b><center>Não foram encontrados resultados</center><b>",
          "info": "Pág _PAGE_ de _PAGES_",
          "sInfoEmpty":    "",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "Busca",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "",
              "sNext":     "",
              "sLast":     "Último"
          }
      }
  });


    var table = $('#datatables').DataTable();

        // Edit record
        table.on( 'click', '.edit', function () {
            $tr = $(this).closest('tr');

            var data = table.row($tr).data();
            alert( 'You press on Row: ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\'s row.' );
        } );

        // Delete a record
        table.on( 'click', '.remove', function (e) {
            $tr = $(this).closest('tr');
            table.row($tr).remove().draw();
            e.preventDefault();
        } );

        //Like record
        table.on( 'click', '.like', function () {
            alert('You clicked on Like button');
        });

        $('.card .material-datatables label').addClass('form-group');
    });

///// SCRIPT REMOVER

$("#remover").click(function(){
            swal({
                type: 'warning',  
                title: 'Deseja Realmente deletar?',
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                cancelButtonText: "Cancelar",
                confirmButtonText: "Sim, Deletar!",
                }).then(function (result) {
                swal({
                    type: 'success',
                    html: 'Deletado com sucesso'
                })
            })
        }); 

///// TABLE G12 DASHBOARD MAN
$(document).ready(function() {
    $('#g12_man').DataTable({
        "pagingType": "full_numbers",
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        responsive: true,
        searching: false, 
        paginate: false,
        info: false,
        "language": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   " _MENU_ ",
          "sZeroRecords":  "<b><center>Não foram encontrados resultados</center><b>",
          "info": "Pág _PAGE_ de _PAGES_",
          "sInfoEmpty":    "",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "Busca",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "",
              "sNext":     "",
              "sLast":     "Último"
          }
      }
  });


    var table = $('#g12_man').DataTable();

        // Edit record
        table.on( 'click', '.edit', function () {
            $tr = $(this).closest('tr');

            var data = table.row($tr).data();
            alert( 'You press on Row: ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\'s row.' );
        } );

        // Delete a record
        table.on( 'click', '.remove', function (e) {
            $tr = $(this).closest('tr');
            table.row($tr).remove().draw();
            e.preventDefault();
        } );

        //Like record
        table.on( 'click', '.like', function () {
            alert('You clicked on Like button');
        });

        $('.card .material-datatables label').addClass('form-group');
    });
///// TABLE G12 DASHBOARD WOMAN
$(document).ready(function() {
    $('#g12_woman').DataTable({
        "pagingType": "full_numbers",
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        responsive: true,
        searching: false, 
        paginate: false,
        info: false,
        "language": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   " _MENU_ ",
          "sZeroRecords":  "<b><center>Não foram encontrados resultados</center><b>",
          "info": "Pág _PAGE_ de _PAGES_",
          "sInfoEmpty":    "",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "Busca",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "",
              "sNext":     "",
              "sLast":     "Último"
          }
      }
  });


    var table = $('#g12_woman').DataTable();

        // Edit record
        table.on( 'click', '.edit', function () {
            $tr = $(this).closest('tr');

            var data = table.row($tr).data();
            alert( 'You press on Row: ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\'s row.' );
        } );

        // Delete a record
        table.on( 'click', '.remove', function (e) {
            $tr = $(this).closest('tr');
            table.row($tr).remove().draw();
            e.preventDefault();
        } );

        //Like record
        table.on( 'click', '.like', function () {
            alert('You clicked on Like button');
        });

        $('.card .material-datatables label').addClass('form-group');
    });

    ///// TABLE TOP 12 DASHBOARD 
    $(document).ready(function() {
    $('#g12_top').DataTable({
        "pagingType": "full_numbers",
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        responsive: true,
        searching: false, 
        paginate: false,
        info: false,
        "language": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   " _MENU_ ",
          "sZeroRecords":  "<b><center>Não foram encontrados resultados</center><b>",
          "info": "Pág _PAGE_ de _PAGES_",
          "sInfoEmpty":    "",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "Busca",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "",
              "sNext":     "",
              "sLast":     "Último"
          }
      }
  });


    var table = $('#g12_top').DataTable();

        // Edit record
        table.on( 'click', '.edit', function () {
            $tr = $(this).closest('tr');

            var data = table.row($tr).data();
            alert( 'You press on Row: ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\'s row.' );
        } );

        // Delete a record
        table.on( 'click', '.remove', function (e) {
            $tr = $(this).closest('tr');
            table.row($tr).remove().draw();
            e.preventDefault();
        } );

        //Like record
        table.on( 'click', '.like', function () {
            alert('You clicked on Like button');
        });

        $('.card .material-datatables label').addClass('form-group');
    });


 ///// Calendario birth leader
$(document).ready(function() {

$('#id_birth').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  "locale": {
    "format": "DD/MM/YYYY",
    "separator": " - ",
    "applyLabel": "Aplicar",
    "cancelLabel": "Cancelar",
    "fromLabel": "De",
    "toLabel": "Até",
    "customRangeLabel": "Custom",
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
  }});

$('#id_conversion_date').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  "locale": {
    "format": "DD/MM/YYYY",
    "separator": " - ",
    "applyLabel": "Aplicar",
    "cancelLabel": "Cancelar",
    "fromLabel": "De",
    "toLabel": "Até",
    "customRangeLabel": "Custom",
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
  }});
$('#id_meeting_date').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  "locale": {
    "format": "DD/MM/YYYY",
    "separator": " - ",
    "applyLabel": "Aplicar",
    "cancelLabel": "Cancelar",
    "fromLabel": "De",
    "toLabel": "Até",
    "customRangeLabel": "Custom",
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
  }});
$('#id_date_batismo').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  "locale": {
    "format": "DD/MM/YYYY",
    "separator": " - ",
    "applyLabel": "Aplicar",
    "cancelLabel": "Cancelar",
    "fromLabel": "De",
    "toLabel": "Até",
    "customRangeLabel": "Custom",
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
  }});


  });
